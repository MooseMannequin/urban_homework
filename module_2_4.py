numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers[1:15]:  # i = 2
    # print(numbers[i])
    for j in numbers[1:15]:  # j = 1,2,3,4
        #print(j)
        if j != i and i % j == 0:
            not_primes.append(i)
            break
        elif j != i and i % j != 0:
            continue
        else:
            primes.append(i)
            break
print(primes)
print(not_primes)