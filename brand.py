import re
import scrapy
from main import PrismstoneSpider


class PrismstoneBrandSpider(PrismstoneSpider):
    """ID とブランドだけを抽出する spider"""
    name = 'prismstone_brand'

    def parse_series(self, response):
        href = response.css('a.tablink2::attr(href)').extract_first() # 「ブランド別に並べる」ボタンのリンク
        next_url = response.urljoin(href)
        yield scrapy.Request(next_url, callback=self.parse_brand)

    def parse_brand(self, response):
        categories = response.css('.resulteachbox')
        for category in categories:
            brand = category.css('h5 img::attr(alt)').extract_first()
            for a in category.css('a'):
                id_and_name = a.css('img::attr(alt)').extract_first()
                id, _ = self._split_id_and_name(id_and_name)
                stone = dict(
                    id=id,
                    brand=brand,
                )
                yield stone

    def _split_id_and_name(self, id_and_name):
        regex = r'([\w\-★]+)(.+)'
        id_and_name = id_and_name.replace('\u3000', ' ')  # 全角スペースを半角スペースに置換
        m = re.search(regex, id_and_name, flags=re.ASCII)
        id, name = m.groups()
        name = name.strip()  # よけいな余白を取り除く
        return (id, name)
