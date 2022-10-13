def isPrime(num):

    for x in range (2,int(num**0.5)+1):
        if num%x==0 :
            return False
    
    return True


def primes(number_of_primes):
    list = []
    if number_of_primes < 1:
        raise ValueError("Positive integers only")
    i=2
    while (len(list) < number_of_primes):
        if isPrime(i):
            list.append(i)
        i+=1

    return list
