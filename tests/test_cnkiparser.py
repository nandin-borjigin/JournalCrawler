#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from core.journal import Journal
from fixtures.common import cnkiparser, journal_with_url, fake_search_response

def test_parse_search_response(cnkiparser, journal_with_url):
    name, url = journal_with_url
    response = fake_search_response(name)
    assert cnkiparser.parse_search_response(response) == url

    
