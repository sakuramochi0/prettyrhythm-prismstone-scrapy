import re
import scrapy


class PrismstoneSpider(scrapy.Spider):
    name = 'prismstone'
    start_urls = ['http://www.prettyrhythm.jp/list/index.php']
    start_time = '20170101000000'
    end_time = '20180101000000'

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_wayback_machine.WaybackMachineMiddleware': 5,
        },
        'WAYBACK_MACHINE_TIME_RANGE': (start_time, end_time),
    }

    def parse(self, response):
        series_urls = response.css('.season_btn a::attr(href)').extract()
        for url in series_urls:
            next_url = response.urljoin(url)
            yield scrapy.Request(next_url, callback=self.parse_series)

    def parse_series(self, response):
        categories = response.css('.resulteachbox')
        for cat in categories:
            category_name = cat.css('h5 img::attr(alt)').extract_first()
            for a in cat.css('a'):
                id_and_name = a.css('img::attr(alt)').extract_first()
                id, name = self._split_id_and_name(id_and_name)
                img_url = response.urljoin(a.css('::attr(href)').extract_first())
                stone = dict(
                    id=id,
                    name=name,
                    category_name=category_name,
                    img_url=img_url,
                )
                yield stone

    def _split_id_and_name(self, id_and_name):
        regex = r'([\w\-★]+)(.+)'
        id_and_name = id_and_name.replace('\u3000', ' ') # 全角スペースを半角スペースに置換
        m = re.search(regex, id_and_name, flags=re.ASCII)
        id, name = m.groups()
        name = name.strip() # よけいな余白を取り除く
        return (id, name)
