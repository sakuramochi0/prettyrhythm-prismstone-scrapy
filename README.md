# prettyrhythm-prismstone-scrapy
プリズムストーンリスト (http://www.prettyrhythm.jp/list/index.php) をインターネットアーカイブからスクレイピングするコード。プリズムストーンリストのページが壊れてしまっているので(2018/01/09現在)、正しく検索できるページを作るための準備として作りました。

## プリズムストーンリスト
- [prismstone.md](prismstone.md)

## コードのライセンス
- [GNU General Public License v3.0](LICENSE)

 ただし、プリズムストーンのデータ [prismstone.json](prismstone.json) と [prismstone.md](prismstone.md) を除く。

## 使い方

### `prismstone.json`, `brand.json` の作り方
1. [Python3](https://www.python.org/) をインストールする。
1. `$ pip install -r requirements.txt`
1. `$ scrapy runspider main.py -o prismstone.json`
1. `$ scrapy runspider brand.py -o brand.json`

### `prismstone.md`, `brand.md` に変換する方法
1. [Node.js](https://nodejs.org/ja/) をインストールする。
1. `$ npm install`
1. `$ npm run convert`

## バグ
- 同じアイテムを重複して取得してしまう問題があります。リポジトリにあるデータは、重複を手動で取り除いたものになっています。