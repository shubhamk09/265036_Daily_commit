try:
    num1=10
    num2=0
    print(num1/num2)
    print("Done")
except ZeroDivisionError:
    print("An error occured")
    print("Due to zero division")
except (ValueError, TypeError):
    print("Error")
except:
    print("some error occured")
#     optional raise
    raise
finally:
    print("this code runs no matter what.")

print(1)
# paranthesis or arguments are optionals
raise ValueError("Just a value error")
print(2)