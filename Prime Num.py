def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

result = []
for num in range(100, 1000):
    digits = [int(d) for d in str(num)]
    if all(d in [2, 3, 5, 7] for d in digits):  # every digit prime
        if is_prime(num):                       # number itself prime
            if is_prime(sum(digits)):           # sum of digits prime
                result.append(num)

print(result)



