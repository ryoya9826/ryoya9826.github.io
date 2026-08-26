# Google Indexing API 連携

`master` への push で `_publications` / `_preprints` / `_talks` / `_books` / `_theses` /
`_teaching` / `_miscellaneous` / `_pages` 配下に変更があった場合、変更されたページのURLを
Google Indexing API に通知する ([`.github/workflows/notify-google-indexing.yml`](../.github/workflows/notify-google-indexing.yml))。

> [!NOTE]
> Indexing API は本来 JobPosting / BroadcastEvent 構造化データ用のAPIであり、
> 一般ページへの通知はGoogle非公式の用法である。

## セットアップ（初回のみ）

1. 対象のGCPプロジェクトで **Indexing API** を有効化する
   （APIとサービス → ライブラリ → "Web Search Indexing API" を検索）
2. サービスアカウント（例: `indexing@<project-id>.iam.gserviceaccount.com`）の
   **JSON鍵を発行**してダウンロードする（手順は下記「JSON鍵の発行手順」参照）
3. [Search Console](https://search.google.com/search-console) の対象プロパティの
   設定 → ユーザーと権限 → 上記サービスアカウントを **所有者** として追加する
4. このリポジトリの Settings → Secrets and variables → Actions で、
   シークレット名 `GCP_INDEXING_SA_KEY` にダウンロードしたJSON鍵の中身をそのまま貼り付ける
   （手順は下記「GitHub Secretsへの登録手順」参照）

### JSON鍵の発行手順

1. [Google Cloud Console](https://console.cloud.google.com/) にアクセスし、右上のプロジェクト選択メニューで対象のプロジェクト（例: `indexing-408907`）を選択する
2. 左側のナビゲーションメニュー →「IAMと管理」→「サービスアカウント」を開く
   （検索窓に "service accounts" と入力しても出てくる）
3. 一覧から対象のサービスアカウント（例: `indexing@indexing-408907.iam.gserviceaccount.com`）をクリックする
4. サービスアカウントの詳細画面の上部タブから **「鍵」（KEYS）** を選択する
5. 「鍵を追加」（ADD KEY）→「新しい鍵を作成」（Create new key）をクリックする
6. キーのタイプで **「JSON」**（デフォルト）を選択したまま「作成」（CREATE）をクリックする
   → JSONファイルが自動的にブラウザのダウンロードフォルダに保存される
   （ファイル名は `<project-id>-xxxxxxxxxxxx.json` の形式）

> [!WARNING]
> ダウンロードしたJSONファイルは秘密鍵そのもの。公開リポジトリへのコミットや
> チャット・Slack等への貼り付けは絶対に行わないこと。GitHub Secretsへの登録後は
> ローカルのダウンロードフォルダに残さず、安全な場所へ移動するか削除する。
> 使わなくなった古い鍵は同じ「鍵」タブから削除しておく。

### GitHub Secretsへの登録手順

1. ダウンロードしたJSONファイルを開き、中身をすべて（`{` から `}` まで）コピーする
2. このリポジトリのGitHubページを開き、「Settings」タブ →左メニュー
   「Secrets and variables」→「Actions」を開く
3. 「New repository secret」をクリックする
4. **Name** に `GCP_INDEXING_SA_KEY` と入力する
5. **Secret** にコピーしたJSONの中身をそのまま貼り付ける
6. 「Add secret」で保存する

## 動作の仕組み

- コレクション配下のファイルは `_config.yml` の `permalink: /:collection/:path/` 規則からURLを算出する
- `_pages` 配下のファイルは front matter の `permalink` を直接使用する
  （`sitemap: false` が指定されたページは通知対象から除外する）
- 追加・更新されたファイルは `URL_UPDATED`、削除されたファイルは `URL_DELETED` として通知する

## 制限

- Indexing API のデフォルトクォータは1日あたり200リクエスト
