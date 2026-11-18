An academic website for Ryoya Ando, based on the academicpages template (https://github.com/academicpages/academicpages.github.io).

## ビルドとデプロイ

Jekyll 4 でビルドし、GitHub Actions（`.github/workflows/jekyll.yml`）で GitHub Pages にデプロイする。

- `master` に push すると、ビルドしてデプロイする
- `master` 向けの PR では、ビルドが通るかだけを確認する
- リポジトリの Settings → Pages の Source は「GitHub Actions」にしておく

## ローカルでの確認

Ruby 3.3 と Bundler を用意して、次を実行する。

```bash
bundle install
bundle exec jekyll serve --livereload --config _config.yml,_config.dev.yml
```

http://localhost:4000 で確認できる。

Docker を使う場合は次のとおり。`JEKYLL_ENV=docker` を指定しないと、`jekyll serve` が URL を `http://0.0.0.0:4000` に書き換え、localhost で開いたページからフォントなどが読めなくなる。

```bash
docker run --rm -it -p 4000:4000 -e JEKYLL_ENV=docker -v "$PWD":/srv/site -w /srv/site ruby:3.3 \
  sh -c "bundle install && bundle exec jekyll serve --host 0.0.0.0 --config _config.yml,_config.dev.yml"
```

## JavaScript の再生成

`assets/js/_main.js` やプラグインを変更したときは、`assets/js/main.min.js` を作り直してコミットする。

```bash
npm install
npm run build:js
```
