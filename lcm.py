a = int(input("ENTER a num: "))
b = int(input("ENTER a num: "))

if a > b:
    big = a
else:
    big = b

while True:
    if big % a == 0 and big % b == 0:
        print("LCM is:", big)
        break
    big += 1
