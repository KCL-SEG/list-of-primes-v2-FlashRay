import math

def primes(number_of_primes):
    list = []
    for x in range (2, number_of_primes):
        for y in range (2,int(math.sqrt(x)+1)):
            if x%y==0 :
                break
        else:
            list.append(x)
    return list
