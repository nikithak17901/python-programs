names = []
for i in range(5):
    a = input("Enter name {}: ".format(i+1))
    names.append(a)

index = 1  
for i in names:
    print("{}. Mr/Ms {}".format(index, i))
    index += 1
