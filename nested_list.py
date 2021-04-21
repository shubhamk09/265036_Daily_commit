import sys
records=[]
for _ in range(int(input())):
    data=[]
    name = input()
    score = float(input())
    data.append(name)
    data.append(score)
    records.append(data)

second = records[0][1]
min = records[0]
for i in records:
    if i[1] <= min[1]:
        if second<i[1]:
            second = min[1]
        min = i

    elif i[1] < second:
        second = i[1]
    print(min)
    print(second)

print(min)

for i in records:
    if i[1] == second:
        print(i[0])

i=len(records)-1
while i>=0:
    if records[i][1] == second:
        print(records[i][0])
    i -= 1

