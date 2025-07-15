a=int(input("enter num of rows"))
for i in range(a):
    for i in range(a-i):
        print("*",end="")
    print()