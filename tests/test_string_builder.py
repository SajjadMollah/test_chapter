from lib.string_builder import *

def test_string_builder_add():
    sb = StringBuilder()
    sb.add("hello")
    result = sb.output()
    assert result == "hello"

def test_string_builder_add_extended():
    sb = StringBuilder()
    sb.add("hello")
    sb.add(" ")
    sb.add("user!")
    result = sb.output()
    assert result == "hello user!"

def test_string_builder_size():
    sb = StringBuilder()
    sb.add("hello")
    result = sb.size()
    assert result == 5

def test_string_builder_size_extended():
    sb = StringBuilder()
    sb.add("hello")
    sb.add(" ")
    sb.add("user!")
    result = sb.size()
    assert result == 11
    
