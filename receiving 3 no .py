print("Read 3 numbers and check the second largest number")

a = int(input("a enter num: "))
b = int(input("b enter num: "))
c = int(input("c enter num: "))

if (a > b and a < c) or (a > c and a < b):
    print("a is second")
elif (b > a and b < c) or (b > c and b < a):
    print("b is second")
else:
    print("c is second")
