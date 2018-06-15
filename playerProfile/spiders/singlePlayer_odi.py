import scrapy


class QuotesSpider(scrapy.Spider):
    name = "odi"
    start_urls = [
        'http://www.espncricinfo.com/ci/content/player/caps.html?country=8;class=2'
    ]

    def parse(self, response):
        for ref in response.css('div.ciPlayerbycapstable ul li.ciPlayername a::attr(href)'):
            yield response.follow(ref, self.parse_page)

    def parse_page(self, response):

        emptyJson = []

        tepStr = "{'"
        tepStr += response.xpath(
            '/html/body/div[4]/div[1]/div[1]/div[4]/div[2]/div/p[2]/b/text()').extract_first()
        tepStr += "':'"
        tepStr += response.xpath(
            '/html/body/div[4]/div[1]/div[1]/div[4]/div[2]/div/p[2]/span/text()').extract_first()
        tepStr += "'}"
        emptyJson.append(tepStr)

        tepStr = "{'"
        tepStr += response.xpath(
            '/html/body/div[4]/div[1]/div[1]/div[4]/div[2]/div/p[3]/b/text()').extract_first()
        tepStr += "':'"
        tepStr += response.xpath(
            '/html/body/div[4]/div[1]/div[1]/div[4]/div[2]/div/p[3]/span/text()').extract_first()
        tepStr += "'}"
        emptyJson.append(tepStr)

        tepStr = "{'"
        tepStr += response.xpath(
            '/html/body/div[4]/div[1]/div[1]/div[4]/div[2]/div/p[4]/b/text()').extract_first()
        tepStr += "':'"
        tepStr += response.xpath(
            '/html/body/div[4]/div[1]/div[1]/div[4]/div[2]/div/p[4]/span/text()').extract_first()
        tepStr += "'}"
        emptyJson.append(tepStr)

        tepStr = "{'"
        tepStr += response.xpath(
            '/html/body/div[4]/div[1]/div[1]/div[4]/div[2]/div/p[5]/b/text()').extract_first()
        tepStr += "':'"
        tepStr += response.xpath(
            '/html/body/div[4]/div[1]/div[1]/div[4]/div[2]/div/p[5]/span/text()').extract_first()
        tepStr += "'}"
        emptyJson.append(tepStr)

        tepStr = "{'"
        tepStr += response.xpath(
            '/html/body/div[4]/div[1]/div[1]/div[4]/div[2]/div/p[6]/b/text()').extract_first()
        tepStr += "':'"
        tepStr += response.xpath(
            '/html/body/div[4]/div[1]/div[1]/div[4]/div[2]/div/p[6]/span/text()').extract_first()
        tepStr += "'}"
        emptyJson.append(tepStr)

        tepStr = "{'"
        tepStr += response.xpath(
            '/html/body/div[4]/div[1]/div[1]/div[4]/div[2]/div/p[7]/b/text()').extract_first()
        tepStr += "':'"
        tepStr += response.xpath(
            '/html/body/div[4]/div[1]/div[1]/div[4]/div[2]/div/p[7]/span/text()').extract_first()
        tepStr += "'}"
        emptyJson.append(tepStr)

        yield {
            'name': response.css("h1::text").extract_first(),
            'country': response.css("div h3.PlayersSearchLink b::text").extract(),
            'player_ifo': emptyJson,
            # 'basic_info': basicInfoStr,
            # "'" + response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/div[2]/div/p[5]/b').extract() + "'":
            #     response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/div[2]/div/p[5]/span').extract(),
            # "'" + response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/div[2]/div/p[6]/b').extract() + "'":
            #     response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/div[2]/div/p[6]/span').extract(),
            # "'" + response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/div[2]/div/p[7]/b').extract() + "'":
            #     response.xpath('/html/body/div[4]/div[1]/div[1]/div[4]/div[2]/div/p[7]/span').extract(),

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
