list = [6, 5, 4, 7, 2, 3, 9]
first=list[0]

for i in range(len(list)):
    if i+1 < len(list)-1:
        list[i] = list[i+1]
    elif i == len(list)-1:
        list[i] = first

print(list)