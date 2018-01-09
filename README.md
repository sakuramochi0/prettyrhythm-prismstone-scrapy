# prettyrhythm-prismstone-scrapy
プリズムストーンリスト (http://www.prettyrhythm.jp/list/index.php) をインターネットアーカイブからスクレイピングするコード。プリズムストーンリストのページが壊れてしまっているので(2018/01/09現在)、正しく検索できるページを作るための準備として作りました。

## ライセンス
[GNU General Public License v3.0](LICENSE)

## 使い方

### `prismstone.json` の作り方
1. Python3 をインストールする。
1. `$ pip install -r requirements.txt`
1. `$ scrapy runspider main.py -o prismstone.json`

### `prismstone.md` に変換する方法
1. nodejs をインストールする。
1. `$ npm install`
1. `$ npm run convert`