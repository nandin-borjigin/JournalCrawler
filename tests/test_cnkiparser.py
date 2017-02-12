#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from core.journal import Journal
from fixtures.common import cnkiparser, journal_with_url, fake_search_response, fake_exist_response

def test_parse_search_response(cnkiparser, journal_with_url):
    name, url = journal_with_url
    response = fake_search_response(name)
    assert cnkiparser.parse_search_response(response) == url

def test_parse_article_existence(cnkiparser):
    response = fake_exist_response(True)
    assert cnkiparser.parse_article_existence(response)
    response = fake_exist_response(False)
    assert not cnkiparser.parse_article_existence(response)

