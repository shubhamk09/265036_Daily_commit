words = ["Hello", "world", "!"]
print(words[0])

strr = ["string", 0, [1, 2, "number"], 4.56]
print(strr[2][2])

str = "Hello world!"
print(str[2])

words[0] = "no"
print(words[0])

nums = [1, 2, 3, 4, 5]
nums[3] = nums[1]
print(nums[3])

words = words + ["yes", "you", "are", "dumb"]
print(words)

nums = [1, 2, 3]
print(nums * 3)
print("string" in words)

nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])

print(4 not in nums)
print(not 4 in nums)

nums.append(36)

words = ["hello"]
words.append("world")
print(words[1])

print(len(words))

words.insert(0, "is")
print(words)

nums = [9, 8, 7, 6, 5]
nums.append(4)
nums.insert(2, 11)
print(len(nums))

print(nums.index(7))
print(max(nums))
print(min(nums))
print(nums.count(7))
nums.remove(7)
nums.reverse()


i=1
while i <= 5:
    print(i)
    i=i+1
