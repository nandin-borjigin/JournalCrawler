import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from fixtures.common import *
from core.journal import Journal 

def test_journal_name(journal_name):
    journal = Journal(journal_name)
    assert journal.name == journal_name
    
