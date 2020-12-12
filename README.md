# prettyrhythm-prismstone-scrapy
プリズムストーンリスト (http://www.prettyrhythm.jp/list/index.php) のストーンの情報を、インターネットアーカイブからスクレイピングするコード。プリズムストーンリストのページが壊れてしまっているので(2018/01/09現在)、正しく検索できるページを作るための準備として作りました。

2020年12月13日に確認したら、ウェブサイトのプリズムストーンリストのページが消されてしまっているみたいでした。画像のURLにもアクセスできなくなってしまったので、Google Cloud StorageのURLを使用したリストを作成しました。

## プリズムストーンリスト

- 閲覧用: [prismstone_with_brand_gcs.md](prismstone_with_brand_gcs.md)
- GitHub Pages hosted JSON: https://sakuramochi0.github.io/prettyrhythm-prismstone-scrapy/prismstone_with_brand_gcs.json
- You can also use the image mirror storage created for the archive: https://storage.googleapis.com/prettyrhythm-prismstone/
  - i.e.: https://storage.googleapis.com/prettyrhythm-prismstone/s05-rad-03r-l.gif

## コードのライセンス

- [GNU General Public License v3.0](LICENSE)

 ただし、プリズムストーンのデータ `*.json` と `*.md` を除く。

## 使い方

### `*.json` の作り方

1. [Python3](https://www.python.org/) をインストールする。
1. `$ pip install -r requirements.txt`
1. `$ scrapy runspider main.py -o prismstone.json`
1. `$ scrapy runspider brand.py -o brand.json`

### `*.json` を `*.md` に変換する方法

1. [Node.js](https://nodejs.org/ja/) をインストールする。
1. `$ npm install`
1. `$ npm run convert`

## バグ

- 同じアイテムを重複して取得してしまう問題があります。リポジトリにあるデータは、重複を手動で取り除いたものになっています。
