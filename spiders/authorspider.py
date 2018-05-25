#导入相应的库和类
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from author.items import AuthorItem


#定义爬虫类
class author(CrawlSpider):
	name = 'author'
	start_urls = ['https://www.jianshu.com/recommendations/users?page=1']


#定义parse()函数
	def parse(self,response):	
		base_url = 'https://www.jianshu.com/u/'
		selector = Selector(response)
		infos = selector.xpath('//div[@class="col-xs-8"]')	#获取对应作者的列表
		for info in infos:
			author_url = base_url + info.xpath('div/a/@href').extract()[0].split('/')[-1]	#作者的链接
			author_name = info.xpath('div/a/h4/text()').extract()[0]	#作者的姓名
			article = info.xpath('div/div[@class="recent-update"]')[0]	#作者文章的信息
			#回调parse_item()函数
			yield Request(author_url,meta={'author_url':author_url,'author_name':author_name,},callback=self.parse_item)
			urls = ['https://www.jianshu.com/recommendations/users?page={}'.format(str(i)) for i in range(2,10)]
			for url in urls:
				yield Request(url,callback=self.parse)	#循环回调parse函数


#定义parse_item()函数
	def parse_item(self,response):	
		item = AuthorItem()	#实例化
		item['author_url']  = response.meta['author_url']
		item['author_name'] = response.meta['author_name']

		try:
			selector = Selector(response)
			focus = selector.xpath('//div[@class="info"]/ul/li[1]/div/a/p/text()').extract()[0]
			fans = selector.xpath('//div[@class="info"]/ul/li[2]/div/a/p/text()').extract()[0]
			article_num = selector.xpath('//div[@class="info"]/ul/li[3]/div/a/p/text()').extract()[0]
			write_num = selector.xpath('//div[@class="info"]/ul/li[4]/div/a/p/text()').extract()[0]
			like = selector.xpath('//div[@class="info"]/ul/li[5]/div/a/p/text()').extract()[0]
			item['style'] = style
			item['focus'] = focus
			item['fans'] = fans
			item['article_num'] = article_num
			item['write_num'] = write_num
			item['like'] = like
			yield item
		except IndexError:	#pass掉IndexError的错误
			pass
