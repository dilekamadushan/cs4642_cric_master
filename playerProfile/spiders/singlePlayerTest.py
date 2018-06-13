import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://www.espncricinfo.com/ci/content/player/caps.html?country=8;class=2'
    ]

    # cric_old_template.page-context-top.no-subnav div#ciHomeContent div#ciMainContainer div#ciHomeContentlhs div.pnl650M div.ciWPContainer div.ciPlayerbycapstable ul
    # body  # cric_old_template.page-context-top.no-subnav div#ciHomeContent div#ciMainContainer div#ciHomeContentlhs div.pnl650M div.ciWPContainer div.ciPlayerbycapstable ul li.sep ul li.ciPlayername a.ColumnistSmry
    def parse(self, response):
        for ref in response.css('div.ciPlayerbycapstable ul li.ciPlayername a::attr(href)'):
            yield response.follow(ref, self.parse_page)

    def parse_page(self, response):
        # for quote in response.css('div.quote'):
        AttributeList = response.css("p.ciPlayerinformationtxt b::text").extract()
        ValueList = response.css("p.ciPlayerinformationtxt span::text").extract()
        emptyJson = []

        for i in range(len(AttributeList)):
            tepStr = "{'"
            tepStr += AttributeList[i]
            tepStr += "':'"
            tepStr += ValueList[i]
            tepStr += "'}"
            emptyJson.append(tepStr)
        # cric_old_template.page-context-top.no-subnav div#ciHomeContent div#ciMainContainer div#ciHomeContentlhs div.pnl490M div.ciPlayernametxt div h3.PlayersSearchLink b
        yield {
            'name': response.css("h1::text").extract_first(),
            'country': response.css("div h3.PlayersSearchLink b::text").extract(),
            'player_ifo': emptyJson,
            'profile': response.css("p.ciPlayerprofiletext1::text").extract(),
            'odi_batting_matches':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[1]/tbody/tr[2]/td[2]/text()').extract()[
                    0].strip(),
            'odi_batting_innings':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[1]/tbody/tr[2]/td[3]/text()').extract()[
                    0].strip(),
            'odi_batting_NO':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[1]/tbody/tr[2]/td[4]/text()').extract()[
                    0].strip(),
            'odi_batting_runs':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[1]/tbody/tr[2]/td[5]/text()').extract()[
                    0].strip(),
            'odi_highest_score':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[1]/tbody/tr[2]/td[6]/text()').extract()[
                    0].strip(),
            'odi_batting_average':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[1]/tbody/tr[2]/td[7]/text()').extract()[
                    0].strip(),
            'odi_BF':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[1]/tbody/tr[2]/td[8]/text()').extract()[
                    0].strip(),
            'odi_SR':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[1]/tbody/tr[2]/td[9]/text()').extract()[
                    0].strip(),
            'odi_100':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[1]/tbody/tr[2]/td[10]/text()').extract()[
                    0].strip(),
            'odi_50':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[1]/tbody/tr[2]/td[11]/text()').extract()[
                    0].strip(),
            'odi_catches':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[1]/tbody/tr[2]/td[13]/text()').extract()[
                    0].strip(),
            'odi_stumps':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[1]/tbody/tr[2]/td[14]/text()').extract()[
                    0].strip(),

            'odi_bowling_matches':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[2]/tbody/tr[2]/td[2]/text()').extract()[
                    0].strip(),
            'odi_bowling_innings':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[2]/tbody/tr[2]/td[3]/text()').extract()[
                    0].strip(),
            'odi_bowling_balls':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[2]/tbody/tr[2]/td[4]/text()').extract()[
                    0].strip(),
            'odi_bowling_runs':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[2]/tbody/tr[2]/td[5]/text()').extract()[
                    0].strip(),
            'odi_bowling_wickets':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[2]/tbody/tr[2]/td[6]/text()').extract()[
                    0].strip(),
            'odi_BBI':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[2]/tbody/tr[2]/td[7]/text()').extract()[
                    0].strip(),
            'odi_BBM':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[2]/tbody/tr[2]/td[8]/text()').extract()[
                    0].strip(),
            'odi_bowling_average':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[2]/tbody/tr[2]/td[9]/text()').extract()[
                    0].strip(),
            'odi_bowling_econ':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[2]/tbody/tr[2]/td[10]/text()').extract()[
                    0].strip(),
            'odi_bowling_SR':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[2]/tbody/tr[2]/td[11]/text()').extract()[
                    0].strip(),
            'odi_bowling_4W':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[2]/tbody/tr[2]/td[12]/text()').extract()[
                    0].strip(),
            'odi_bowling_5W':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[2]/tbody/tr[2]/td[13]/text()').extract()[
                    0].strip(),
            'odi_bowling_10W':
                response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/table[2]/tbody/tr[2]/td[14]/text()').extract()[
                    0].strip(),
        }
