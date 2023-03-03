from numb3rs import validate


def main():
    test_valid_input()
    test_invalid_input()
    
    
def test_valid_input():
    assert validate('127.0.0.1') == True
    assert validate('255.255.255.255') == True

    
def test_invalid_input():
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    assert validate('cat') == False
    assert validate('256.0.0.0') == False
    assert validate('-1.0.0.0') == False
    assert validate('1.333.333.333') == False
    