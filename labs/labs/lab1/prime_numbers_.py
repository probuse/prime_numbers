def prime_numbers(n):
    "Generate prime numbers between 0 and n"
    while isinstance(n, int) and n > 0:
        prime = []
        def is_prime(number):
            "Tests if number is prime"
            if number == 1 or number == 0:
                return False
            for num in range(2, number):
                if number % num == 0:
                    return False
            return True
        
        def primes(num = 0):
            "Generator function yielding prime numbers"
            while True:
                if is_prime(num): yield num
                num += 1
        
        for number in primes():
            if number > n: break
            prime.append(number)
        return prime
    raise ValueError('argument needs to be a positive integer')
    
print prime_numbers(3)
