from bank import value


def test_greetings():
    assert value('hello saahil') == 0
    assert value('Hello Saahil') == 0
    assert value('hi') == 20
    assert value('Hey') == 20
    assert value('good morning') == 100
    assert value('What\'s up?') == 100
