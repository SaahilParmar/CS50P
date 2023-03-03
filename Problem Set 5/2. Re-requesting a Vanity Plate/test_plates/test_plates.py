from plates import is_valid


def main():
    test_valid_plates()
    test_invalid_plates()


def test_valid_plates():
    assert is_valid('AA') == True
    assert is_valid('AAAAAA') == True
    assert is_valid('AAA123') == True
    assert is_valid('cs50') == True

    
def test_invalid_plates():
    assert is_valid('a') == False
    assert is_valid('aaaaaaa') == False
    assert is_valid('PI3.14') == False
    assert is_valid('123456') == False
    assert is_valid('CS05') == False
    assert is_valid('AB12CD') == False
