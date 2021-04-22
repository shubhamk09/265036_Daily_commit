cube = lambda x: x ** 3


def fibonacci(n):
    fibo = [0, 1]
    for i in range(2, n):
        add = fibo[i - 1] + fibo[i - 2]
        fibo.append(add)
    return fibo


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

