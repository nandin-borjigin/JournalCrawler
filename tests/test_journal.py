import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from fixtures.common import journal_data
from core.journal import Journal 

def test_journal_name(journal_data):
    name, _ = journal_data
    journal = Journal(name)
    assert journal.name == name
    
