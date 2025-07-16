legs=int(input("enter total num of legs:"))
heads=int(input("enter total num of heads:"))
flag=False
for hen in range(heads):
    cow=heads-hen
    if(cow*4+hen*2==legs):
        print("COWS:",cow)
        print("HENS:",hen)
        flag=True 
        break 
if(not flag):
    print("No solution")