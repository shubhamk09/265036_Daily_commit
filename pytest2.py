import pytest


def func(x):
    return x + 5


@pytest.mark.one
def test_func():
    assert func(3) == 8


