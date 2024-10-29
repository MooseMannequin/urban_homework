def is_prime(func):
    def wrapper(*args):
        summ = func(*args)
        prime = True
        if summ > 1:
            for i in range(2, summ):
                    if summ % i == 0:
                        prime = False
                        print('Составное')
                        break
            if prime == True:
                print('Простое')
        return summ
    return wrapper



@is_prime
def sum_three(one, two, three):
    summ = one + two + three
    return summ

result = sum_three(2, 3, 6)
print(result)