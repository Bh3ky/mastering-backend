import pytest 

from app.validators.validators import (
    validate_name
)

from app.validators.validators import (
    validate_pin
)

from app.validators.validators import (
    validate_amount
)


def test_valid_name():

    assert (
        validate_name("Brian") == "Brian"
    )


def test_empty_name():

    with pytest.raises(Exception):

        validate_name("")


def test_valid_pin():

    assert (
        validate_pin("1234") == "1234"
    )


def test_invalid_pin_length():

    with pytest.raises(Exception):

        validate_pin("12")


def test_invalid_pin_letters():

    with pytest.raises(Exception):

        validate_pin("abcd")


def test_valid_amount():

    assert (
        validate_amount(100) == 100
    ) 


def test_negative_amount():

    with pytest.raises(Exception):

        validate_amount(-100)