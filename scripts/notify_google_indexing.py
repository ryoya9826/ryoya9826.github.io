#!/usr/bin/env python3
"""push で変更されたページを Google Indexing API に通知するスクリプト。

対象:
  - _config.yml の collections に登録されたコレクション配下のファイル
    (permalink パターン /:collection/:path/ を前提とする)
  - _pages 配下のファイル (front matter の permalink を使用、sitemap: false は除外)

使い方:
  python scripts/notify_google_indexing.py <base_sha> <head_sha>

環境変数:
  GCP_INDEXING_SA_KEY: サービスアカウントキー(JSON文字列)
"""
import json
import os
import subprocess
import sys

import requests
import yaml
from google.auth.transport.requests import Request
from google.oauth2 import service_account

INDEXING_SCOPE = "https://www.googleapis.com/auth/indexing"
INDEXING_ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(REPO_ROOT, "_config.yml")


def load_site_config():
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_changed_files(base_sha, head_sha):
    """(status, path) のリストを返す。status は 'A'/'M'/'D' など。"""
    diff = subprocess.run(
        ["git", "diff", "--no-renames", "--name-status", base_sha, head_sha],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    changes = []
    for line in diff.splitlines():
        if not line.strip():
            continue
        status, path = line.split("\t", 1)
        changes.append((status[0], path))
    return changes


def strip_front_matter(text):
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}


def collection_url(site_url, collection_dir, collection_name, permalink_pattern, path):
    rel = path[len(collection_dir) + 1 :]
    rel_no_ext = os.path.splitext(rel)[0]
    url_path = permalink_pattern.replace(":collection", collection_name).replace(
        ":path", rel_no_ext
    )
    return site_url.rstrip("/") + url_path


def page_url(site_url, front_matter):
    if front_matter.get("sitemap") is False:
        return None
    permalink = front_matter.get("permalink")
    if not permalink:
        return None
    return site_url.rstrip("/") + permalink


def resolve_url(site_url, collections, status, path):
    for collection_name, meta in collections.items():
        collection_dir = f"_{collection_name}"
        if path == collection_dir or not path.startswith(collection_dir + "/"):
            continue
        permalink_pattern = (meta or {}).get("permalink", "/:collection/:path/")
        return collection_url(
            site_url, collection_dir, collection_name, permalink_pattern, path
        )

    if path.startswith("_pages/"):
        if status == "D":
            # 削除されたページの front matter はもう読めないため通知をスキップする
            return None
        full_path = os.path.join(REPO_ROOT, path)
        if not os.path.exists(full_path):
            return None
        with open(full_path, encoding="utf-8") as f:
            front_matter = strip_front_matter(f.read())
        return page_url(site_url, front_matter)

    return None


def build_notifications(site_url, collections, changes):
    notifications = {}
    for status, path in changes:
        if status not in ("A", "M", "D"):
            continue
        url = resolve_url(site_url, collections, status, path)
        if not url:
            continue
        notification_type = "URL_DELETED" if status == "D" else "URL_UPDATED"
        notifications[url] = notification_type
    return notifications


def get_credentials():
    key_json = os.environ.get("GCP_INDEXING_SA_KEY")
    if not key_json:
        raise SystemExit("環境変数 GCP_INDEXING_SA_KEY が設定されていません")
    info = json.loads(key_json)
    creds = service_account.Credentials.from_service_account_info(
        info, scopes=[INDEXING_SCOPE]
    )
    creds.refresh(Request())
    return creds


def notify(creds, url, notification_type):
    resp = requests.post(
        INDEXING_ENDPOINT,
        headers={
            "Authorization": f"Bearer {creds.token}",
            "Content-Type": "application/json",
        },
        json={"url": url, "type": notification_type},
        timeout=30,
    )
    return resp


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    base_sha, head_sha = sys.argv[1], sys.argv[2]

    config = load_site_config()
    site_url = config["url"]
    collections = config.get("collections", {})

    changes = get_changed_files(base_sha, head_sha)
    notifications = build_notifications(site_url, collections, changes)

    if not notifications:
        print("Indexing API に通知する対象のURLはありませんでした。")
        return

    creds = get_credentials()

    failures = []
    for url, notification_type in notifications.items():
        resp = notify(creds, url, notification_type)
        if resp.status_code == 200:
            print(f"OK  [{notification_type}] {url}")
        else:
            print(f"NG  [{notification_type}] {url} -> {resp.status_code} {resp.text}")
            failures.append(url)

    if failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
