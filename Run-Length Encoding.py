ben = "aaabbccccaa"
c = 1
res = ""
for i in range(1, len(ben)):
    if ben[i] == ben[i-1]:
        c += 1
    else:
         res += ben[i-1] + str(c)
        c = 1
res += ben[-1] + str(c)
print(res)