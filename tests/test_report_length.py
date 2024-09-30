from lib.report_length import *

def test_report_length_5():
    result = report_length("hello")
    assert result == "This string was 5 characters long."



def test_report_length_3():
    result = report_length("cow")
    assert result == "This string was 3 characters long."





def test_report_length_nums():
    result = report_length("12345")
    assert result == "This string was 5 characters long."
    
