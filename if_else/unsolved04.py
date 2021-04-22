import datetime as ds


dt = input("input date in format of yyyy-mm-dd\n")
dt = dt.split('-')

x = ds.datetime(int(dt[0]), int(dt[1]), int(dt[2]))
x = x + ds.timedelta(days=1)
print(x)

