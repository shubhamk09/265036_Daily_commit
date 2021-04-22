import sys

# list = [6, 5, 4, 7, 2, 3, 9]
list = [1, 1]
min_number = min(list)
second_minimum = 0
list.sort()

for i in list:
    if i != min_number and i > min_number:
        second_minimum = i
        break
if second_minimum != 0:
    print(second_minimum)
else:
    print("Second Minimum does not exist")


