import pytest
from lib.present import *

def test_wrap_and_unwrap():
    gift1 = Present()
    gift1.wrap("Dog")
    result = gift1.unwrap()
    assert result == "Dog"

def test_wrap_error():
    gift1 = Present()
    gift1.wrap("cat")
    with pytest.raises(Exception) as e:
        gift1.wrap("dog")
    error_txt = str(e.value)
    assert error_txt == "A contents has already been wrapped."

def test_unwrap_error():
    gift1 = Present()
    with pytest.raises(Exception) as e:
        gift1.unwrap()
    error_txt = str(e.value)
    assert error_txt == "No contents have been wrapped."


    


    

