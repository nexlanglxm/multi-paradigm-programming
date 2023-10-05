# Write a program that prints all prime numbers smaller than 100.
# first, a function to define prime numbers
def is_prime(n):
    if n <= 1: 
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1,2):
        if n % i == 0:
            return False
        
    return True

print("all prime numbers smaller than 100:")
for number in range(2,100):
    if is_prime(number):
        print(number,end=" ")