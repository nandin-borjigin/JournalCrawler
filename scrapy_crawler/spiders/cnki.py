# -*- coding: utf-8 -*-
import scrapy
from urllib import urlencode

from core.cnki import CNKI, CNKIParser
from core.journal import Journal


class CnkiSpider(scrapy.Spider):
    name = "cnki"
    allowed_domains = ["navi.cnki.net"]
    journal_names = ['管理世界', '南开管理评论', '中国工业经济', '中国软科学', '科研管理', '管理科学学报', '经济管理']
    years = [str(year) for year in range(2013, 2017)]
    issues = ["%02d" % issue for issue in range(1, 13)]
    cnki = CNKI()
    cnkiparser = CNKIParser()
    def start_requests(self):
        url = self.cnki.search_url
        method = self.cnki.search_method
        headers = self.cnki.search_headers
        for name in self.journal_names:
            journal = Journal(name)
            body = self.cnki.search_body(journal, 1)
            body = urlencode(body)
            meta = { 'journal': journal }
            yield scrapy.Request(url, method = method, headers = headers, body = body, meta = meta)

    def parse(self, response):
        journal_page_url = self.cnkiparser.parse_search_response(response)
        if journal_page_url == '': return
        import urlparse
        query = list(urlparse.urlparse(journal_page_url))[4]
        pykm = dict(urlparse.parse_qsl(query))['baseid']
        journal = response.meta['journal']
        journal.pykm = pykm
        year_issue = [(year, issue) for year in self.years for issue in self.issues]
        for (year, issue) in year_issue:
            url = self.cnki.article_existence_url(journal, year, issue)
            meta = {
                'journal': journal,
                'article': {
                    'year': year,
                    'issue': issue
                }
            }
            yield scrapy.Request(url, meta = meta, callback = self.parse_existence)

    def parse_existence(self, response):
        if self.cnkiparser.parse_article_existence(response):
            journal = response.meta['journal']
            article = response.meta['article']
            url = self.cnki.article_list_url(journal, article['year'], article['issue'])
            yield scrapy.Request(url, meta = response.meta, callback = self.parse_list)

    def parse_list(self, response):
        articles = self.cnkiparser.parse_article_list(response)
        for article in articles:
            self.logger.info(article)
            yield scrapy.Request(article, meta = response.meta, callback = self.parse_article)

    def parse_article(self, response):
        article = self.cnkiparser.parse_article(response)
        article['journal'] = response.meta['journal'].name
        yield article
