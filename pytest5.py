import pytest


@pytest.fixture
def numbers():
    a = 10
    b = 20
    c = 30
    return [a, b, c]


def test_numbers(numbers):
    x = 10
    assert numbers[0] == 10
