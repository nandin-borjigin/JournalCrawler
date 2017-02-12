#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from scrapy.http import Request, TextResponse

from core.cnki import CNKI, CNKIParser
from core.journal import Journal

journals = {
    '管理世界': { 
        'url': 'http://navi.cnki.net/KNavi/pubDetail?pubtype=journal&pcode=CJFD&baseid=GLSJ',
        'pykm': 'GLSJ'
    },
    '南开管理评论': {
        'url': 'http://navi.cnki.net/KNavi/pubDetail?pubtype=journal&pcode=CJFD&baseid=LKGP',
        'pykm': 'LKGP'
    }
}

@pytest.fixture( params = journals )
def journal_name(request):
    return request.param

@pytest.fixture( params = journals )
def journal(request):
    return Journal(request.param)

@pytest.fixture( params = journals )
def journal_with_url(request):
    return (request.param, journals[request.param]['url'])

@pytest.fixture( params = journals )
def journal_object(request):
    return (request.param, journals[request.param])

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

def fake_search_response(journal_name):
    return __file_as_response('search-response-' + journal_name + '.html', { 'journal': Journal(journal_name) })

def fake_exist_response(existence = True):
    url = 'http://www.example.com'
    req = Request(url)
    return TextResponse(url, request = req, body = str(existence)) 

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

