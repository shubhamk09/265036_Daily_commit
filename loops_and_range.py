i = 1
while i <= 5:
    print(i)
    i = i + 1

i = 0
while True:
    print(i)
    i = i + 1
    if i == 5:
        break
print("just")

i = 5
while True:
    print(i)
    i = i - 1
    if i <= 2:
        break

print("just")

i = 5
while True:
    print(i)
    i = i - 1
    if i == 2:
        print("skip 2")
        continue
    if i == 1:
        print("break")
        break

letters = ['a', 'b', 'c']

for l in letters:
    print(l)

listt = [2, 3, 4, 5, 6, 7]

for x in listt:
    if x % 2 == 1 and x > 4:
        print(x)
        break

numbers = list(range(10))
print(numbers)

numbers = list(range(3, 8))
print(numbers)

print(range(20) == range(0, 20))

# start, stop and step
numbers = list(range(3, 8, 2))
print(numbers)

for i in range(0, 20, 2):
    print(i)

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])


print(ord('a'))

c = ord('a')-32
print(chr(c))


st = "welcome"
st = st+'b'
print(st)
