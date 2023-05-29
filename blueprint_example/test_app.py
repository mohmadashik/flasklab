import app 
import pytest
from flask import session

@pytest.fixture
def test_app():
    with app.app_context():
    # with app.test_request_context():
        yield app  

def test_check(test_app):
    assert 1==1
    session['ashik']=2
