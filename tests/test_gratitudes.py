from lib.gratitudes import *

def test_add_gratitudes():
    grat = Gratitudes()
    grat.add("food")
    result = grat.format()
    assert result == "Be grateful for: food"


def test_more_added_gratitudes():
    grat = Gratitudes()
    grat.add("food")
    grat.add("joy")
    grat.add("happiness")
    result = grat.format()
    assert result == "Be grateful for: food, joy, happiness"