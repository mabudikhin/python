numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 222]
primes = []
not_primes = []
for i in numbers:
    is_prime = True
    for d in range(2,i):
        if i % d == 0:
            is_prime = False
            break
    if i != 1:
        if is_prime and i != 1:
            primes.append(i)
        else:
            not_primes.append(i)
print('Не простые', not_primes)
print('Простые', primes)