from datetime import datetime
a= input("enter first date(YYYY-MM-DD):")
b= input("enter second date(YYYY-MM-DD):")
d1 = datetime.strptime(a, "%Y-%m-%d")
d2 = datetime.strptime(b, "%Y-%m-%d")
diff = d2 - d1
print(f"Difference between {a} and {b} is {diff.days} days.")