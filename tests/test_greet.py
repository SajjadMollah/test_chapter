from lib.greet import *

def test_greet_returns_name():
    result = greet("Will")
    assert result == f"Hello, Will!"