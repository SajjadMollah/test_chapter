from lib.check_codeword import *

def test_check_codeword_isCorrect():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_ifClose():
    result = check_codeword("hearse")
    assert result == "Close, but nope."

def test_check_codeword_isWrong():
    result= check_codeword("Car")
    assert result == "WRONG!"
