import pytest
from lib.password_checker import *

def test_password_less_than_8():
    pw = PasswordChecker()
    with pytest.raises(Exception) as e:
        pw.check("1234567")
    error_txt = str(e.value)
    assert error_txt == "Invalid password, must be 8+ characters."

def test_password_more_than_8():
    pw = PasswordChecker()
    result = pw.check("12345678")
    assert result == True