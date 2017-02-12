#coding: utf-8
import random

class CNKI(object):
    def __init__(self):
        self.search_url = 'http://navi.cnki.net/KNavi/Common/Search/All'
        self.search_method = 'POST'
        self.search_headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

    def search_body(self, journal, page):
        prefix = '{"StateID":"","Platfrom":"","QueryTime":"","Account":"knavi","ClientToken":"","Language":"","CNode":{"PCode":"SCDB","SMode":"","OperateT":""},"QNode":{"SelectT":"","Select_Fields":"","S_DBCodes":"","QGroup":[{"Key":"subject","Logic":1,"Items":[],"ChildItems":[{"Key":"txt","Logic":1,"Items":[{"Key":"txt_1","Title":"","Logic":1,"Name":"LY","Operate":"%","Value":"'
        postfix = '","ExtendType":0,"ExtendValue":"","Value2":""}],"ChildItems":[]}]}],"OrderBy":"","GroupBy":"","Additon":""}}'
        return {
            'SearchStateJson': prefix + journal.name + postfix,
            'displaymode': 1,
            'pageindex': page,
            'pagecount': 10,
            'random': random.random()
        }

    
