import pytest
from parenthetics import check_parenthetics


def test_type_not_string():
    with pytest.raises(TypeError):
        check_parenthetics(1)


def test_type_string():
    check_parenthetics("string")


def test_open():
    str = "(One(Two(Three)Two)One"
    assert check_parenthetics(str) == 1


def test_balanced():
    str = "(One(Two(Three)Two)One)"
    assert check_parenthetics(str) == 0


def test_broken():
    str = "(One(Two(Three)Two)One)Zero)"
    assert check_parenthetics(str) == -1
