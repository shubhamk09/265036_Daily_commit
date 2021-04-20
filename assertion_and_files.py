# its a sanity check

print(1)
assert 2 * 2 == 4
print(2)
assert 2 * 2 == 8

temp = -10
assert (temp < 0), "colder than absolute zero"

myfile = open("filename.txt", "r")
count = myfile.read()
# Number of bytes to read
count = myfile.read(16)
print(count)
# To retrieve each line in a file, The write method returns the number of bytes written to a file, if successful.
print(myfile.readlines())

myfile.close()

file = open("filename.txt", "r")

for line in file:
    print(line)

file.close()

file = open("filename.txt", "w")

myfile.write("This has been written to a file")

file.close()

try:
    f = open("filename.txt")
    print(f.read())
finally:
    f.close()

with open("filename.txt") as f:
    print(f.read())
