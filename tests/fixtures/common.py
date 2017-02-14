#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from scrapy.http import Request, TextResponse

from core.cnki import CNKI, CNKIParser
from core.journal import Journal

journals = {
    'guan li shi jie': { 
        'name': '管理世界',
        'url': 'http://navi.cnki.net/KNavi/pubDetail?pubtype=journal&pcode=CJFD&baseid=GLSJ',
        'pykm': 'GLSJ'
    },
    'nan kai guan li ping lun': {
        'name': '南开管理评论',
        'url': 'http://navi.cnki.net/KNavi/pubDetail?pubtype=journal&pcode=CJFD&baseid=LKGP',
        'pykm': 'LKGP'
    }
}

articles = {
    'normal-article': {
        'title': '无绩效考核下外部独立董事薪酬的决定',
        'year': '2016',
        'issue': '02',
        'author': ['沈艺峰', '陈旋'],
        'organization': ['厦门大学管理学院'],
        'abstract': '本文主要研究在没有绩效考虑的情况下,上市公司外部独立董事的薪酬是如何决定的。本文对2005-2014年我国A股上市公司12821个样本的实证检验结果表明,无论是在一定地理范围内、同行业里或一定规模上,上市公司在外部独立董事薪酬决定时均存在显著的"互相看齐"效应,即出现向地理上的中间距离、同一或相关行业或中等规模公司看齐的现象。这既与我们在现实生活中外部独立董事薪酬所观察到的实际现象相吻合,也符合中国传统哲学在利益分配上的中庸思想。',
        'keywords': ['外部独立董事', '公司治理', '薪酬']
    },
    'article without author, abstract, etc.': {
        'title': '2016年总目录',
        'year': '2016',
        'issue': '12',
        'author': [],
        'organization': [],
        'abstract': '', 
        'keywords': []
    }
}

article_lists = {
    'normal article list': {
        'journal': '南开管理评论',
        'year': '2016',
        'issue': '02',
        'list': [
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602001&tableName=CJFDLAST2016',
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602002&tableName=CJFDLAST2016',
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602003&tableName=CJFDLAST2016',
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602004&tableName=CJFDLAST2016',
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602005&tableName=CJFDLAST2016',
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602006&tableName=CJFDLAST2016',
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602007&tableName=CJFDLAST2016',
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602008&tableName=CJFDLAST2016',
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602009&tableName=CJFDLAST2016',
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602010&tableName=CJFDLAST2016',
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602011&tableName=CJFDLAST2016',
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602012&tableName=CJFDLAST2016',
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602013&tableName=CJFDLAST2016',
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602014&tableName=CJFDLAST2016',
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602015&tableName=CJFDLAST2016',
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602016&tableName=CJFDLAST2016',
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602017&tableName=CJFDLAST2016',
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602019&tableName=CJFDLAST2016',
            'http://navi.cnki.net/KNavi/Common/RedirectPage?sfield=FN&dbCode=CJFD&filename=LKGP201602018&tableName=CJFDLAST2016'
        ]
    }
}

@pytest.fixture( params = journals )
def journal_data(request):
    return journals[request.param]

@pytest.fixture( params = articles )
def article_data(request):
    return articles[request.param]

@pytest.fixture( params = article_lists )
def article_list(request):
    return article_lists[request.param]

pages = [1, 3]

@pytest.fixture( params = pages )
def page(request):
    return request.param

years = [2015]
@pytest.fixture( params = years )
def year(request):
    return str(request.param)

issues = [1, 12]
@pytest.fixture( params = issues )
def issue(request):
    return '%2d' % request.param

@pytest.fixture
def cnki():
    return CNKI()

@pytest.fixture
def cnkiparser():
    return CNKIParser()

@pytest.fixture
def fake_search_response(journal_data):
    filename = 'search-response-%s.html' % journal_data['name']
    return (__file_as_response(filename, { 'journal': Journal(journal_data['name']) }), journal_data['url'])

def fake_exist_response(existence = True):
    url = 'http://www.example.com'
    req = Request(url)
    return TextResponse(url, request = req, body = str(existence)) 

@pytest.fixture
def fake_article_list_response(article_list):
    filename = '%s-%s-%s.html' % (article_list['journal'], article_list['year'], article_list['issue'])
    return (__file_as_response(filename), article_list['list'])

@pytest.fixture
def fake_article_response(article_data):
    meta = {
        'article': {
            'year': article_data['year'],
            'issue': article_data['issue']
        }
    }
    filename = 'article-' + article_data['title'] + '.html'
    return (__file_as_response(filename, meta), article_data)

def __file_as_response(filename, meta = {}):
    from os import path
    filepath = 'fake_files/' + filename
    current_dir = path.dirname( path.abspath( __file__ ) )
    fullpath = path.join(current_dir, filepath)
    with open(fullpath, 'r') as f:
        content = f.read()

    url = 'http://www.example.com'
    req =  Request(url, meta = meta)
    return TextResponse(url, request = req, body = content)

