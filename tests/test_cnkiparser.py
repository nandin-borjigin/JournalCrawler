#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from core.journal import Journal
from fixtures.common import cnkiparser, journal_data, article_data
from fixtures.common import fake_search_response, fake_exist_response, fake_article_list_response, fake_article_response

def test_parse_search_response(cnkiparser, journal_data):
    response = fake_search_response(journal_data['name'])
    assert cnkiparser.parse_search_response(response) == journal_data['url']

def test_parse_article_existence(cnkiparser):
    response = fake_exist_response(True)
    assert cnkiparser.parse_article_existence(response)
    response = fake_exist_response(False)
    assert not cnkiparser.parse_article_existence(response)

def test_parse_article_list(cnkiparser):
    response, answer = fake_article_list_response()
    assert cnkiparser.parse_article_list(response) == answer

def test_parse_article(cnkiparser, article_data):
    response, answer = fake_article_response(article_data)
    assert cnkiparser.parse_article(response) == answer
