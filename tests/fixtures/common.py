#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from core.cnki import CNKI
from core.journal import Journal

journals = {
    '管理世界': 'http://navi.cnki.net/KNavi/pubDetail?pubtype=journal&pcode=CJFD&baseid=GLSJ',
}

@pytest.fixture( params = journals )
def journal_name(request):
    return request.param

@pytest.fixture( params = journals )
def journal(request):
    return Journal(request.param)

pages = [1, 3]

@pytest.fixture( params = pages )
def page(request):
    return request.param

@pytest.fixture
def cnki():
    return CNKI()

