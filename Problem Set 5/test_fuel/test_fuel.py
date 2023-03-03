from fuel import convert, gauge
import pytest


def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('cat/dog')


def test_fuel():
    assert convert('1/4') == 25
    assert gauge(25) == '25%'
    assert gauge(100) == 'F'
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'
