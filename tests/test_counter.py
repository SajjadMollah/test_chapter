from lib.counter import *

def test_counter_add():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."



def test_counter_add():
    counter = Counter()
    counter.add(5)
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 15 so far."