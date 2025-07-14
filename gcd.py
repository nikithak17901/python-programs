# GCD of two numbers using Euclidean Algorithm

a = int(input("Enter num1: "))
b = int(input("Enter num2: "))

while b != 0:
    c = a % b
    a = b
    b = c

print("GCD is:", a)
