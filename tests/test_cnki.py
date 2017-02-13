#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from fixtures.common import *

def test_search_url(cnki):
    assert cnki.search_url == 'http://navi.cnki.net/KNavi/Common/Search/All'

def test_search_method(cnki):
    assert cnki.search_method == 'POST'

def test_search_headers(cnki):
    assert cnki.search_headers == {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

def test_search_body(cnki, journal, page):
    prefix = '{"StateID":"","Platfrom":"","QueryTime":"","Account":"knavi","ClientToken":"","Language":"","CNode":{"PCode":"SCDB","SMode":"","OperateT":""},"QNode":{"SelectT":"","Select_Fields":"","S_DBCodes":"","QGroup":[{"Key":"subject","Logic":1,"Items":[],"ChildItems":[{"Key":"txt","Logic":1,"Items":[{"Key":"txt_1","Title":"","Logic":1,"Name":"LY","Operate":"%","Value":"'
    postfix = '","ExtendType":0,"ExtendValue":"","Value2":""}],"ChildItems":[]}]}],"OrderBy":"","GroupBy":"","Additon":""}}'
    search_state_json =  prefix + journal.name + postfix
    def body():
        return    
    search_body = cnki.search_body(journal, page)
    assert 0 <= search_body['random'] < 1
    del search_body['random']
    assert search_body == {
        'SearchStateJson': search_state_json,
        'displaymode': 1,
        'pageindex': page,
        'pagecount': 10
    }

def test_article_url(cnki, journal_object, year, issue):
    name, obj = journal_object
    journal = Journal(name)
    journal.pykm = obj['pykm']
    existence_url = cnki.article_existence_url(journal, year, issue)
    assert existence_url == 'http://navi.cnki.net/KNavi/JournalDetail/GetIfFileExist?year=' + year + '&issue=' + issue + '&pykm=' + obj['pykm']
    list_url = cnki.article_list_url(journal, year, issue)
    assert list_url == 'http://navi.cnki.net/KNavi/JournalDetail/GetArticleList?year=' + year + '&issue=' + issue + '&pykm=' + obj['pykm'] + '&pageIdx=0'

