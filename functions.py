import random

from math import pi

from math import sqrt as sq


def fun():
    print("spam")
    print("spam")
    print("spam")


fun()


def print_word_with_exclamation(word):
    print(word + "!")


print_word_with_exclamation("spam")


def print_double(x):
    print(2 * x)


print_double(3)


def print_multiply(x, y):
    print(y * x)


print_multiply(2, 6)


def even(x):
    if x % 2 == 0:
        print("Yes")
    else:
        print("No")


even(2)

operation = even

operation(5)


def square(x):
    return x * x


def test(func, x):
    print(func(x))


test(square, 42)


for i in range(5):
    value = random.randint(1, 6)
    print(value)


print(pi)

print(sq(16))
