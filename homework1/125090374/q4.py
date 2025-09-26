#check whether a number is prime or not
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#find the largest prime factor
def largest_prime_factor(n):
    for i in range(n, 1, -1):
        if is_prime(i):
            if n % i == 0:
                return i

num = int(input("Enter a positive integer: "))
print(f"The largest prime factor of {num} is: {largest_prime_factor(num)}")