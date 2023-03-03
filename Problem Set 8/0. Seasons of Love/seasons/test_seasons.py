from datetime import date
from pytest import raises
from seasons import date_checking, no_of_days


def test_date():
    assert date_checking('2010-12-01') == date(2010, 12, 1)
    with raises(SystemExit):
        date_checking('December 1, 2000')
    assert no_of_days(date(2022, 12, 4)) == 'One hundred sixteen thousand, six hundred forty minutes'
