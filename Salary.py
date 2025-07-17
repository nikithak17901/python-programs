names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
memo = [0, 1, 1, 1, 2, 2, 1, 2, 1, 2]
salary = [1000, 2000, 3000, 4500, 2000, 5000, 1500, 2300, 1300, 1100]
data = list(zip(names, memo, salary))
removed1 = []
removed2 = []

# Remove those with salary > 4000
for i in data:
    if i[2] > 4000:
        removed1.append(i)

# Remaining with salary < 4000
remaining = [i for i in data if i[2] < 4000]
a = sorted(remaining, key=lambda x: x[2], reverse=True)

# Remove up to 3 with memo >= 2
for i in a:
    if i[1] >= 2:
        removed2.append(i)
    if len(removed2) > 3:
        break

final = removed1 + removed2
for i in final:
    print(f"{i[0]}: Memo {i[1]}, Salary {i[2]}")