source "https://rubygems.org"

# Jekyll 4 系でビルドし、GitHub Actions でデプロイする（.github/workflows/jekyll.yml）。
# ローカルでの確認:
#
#     bundle install
#     bundle exec jekyll serve --livereload
#
gem "jekyll", "~> 4.4"

# _config.yml の plugins に書いたものと揃える
group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-gist"
  gem "jekyll-paginate"
  gem "jekyll-redirect-from"
  gem "jekyll-sitemap"
end

# Ruby 3 系では webrick が標準添付でなくなったため、jekyll serve 用に追加する
gem "webrick", "~> 1.9"

# Windows 用
platforms :windows, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
  gem "wdm", "~> 0.2"
end
