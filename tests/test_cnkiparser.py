#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from core.journal import Journal
from fixtures.common import cnkiparser, search_response, exist_response, article_list_response, article_response

def test_parse_search_response(cnkiparser, search_response):
    response, answer = search_response
    assert cnkiparser.parse_search_response(response) == answer

def test_parse_article_existence(cnkiparser, exist_response):
    response, answer = exist_response
    assert cnkiparser.parse_article_existence(response) == answer

def test_parse_article_list(cnkiparser, article_list_response):
    response, answer = article_list_response
    assert cnkiparser.parse_article_list(response) == answer

def test_parse_article(cnkiparser, article_response):
    response, answer = article_response
    assert cnkiparser.parse_article(response) == answer
