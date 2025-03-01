print("=" * 60)
print(" DAY 3 - PRIME NUMBER CHECKER ".center(60, "-"))
print("=" * 60)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False 
    return True

num = int(input ("Enter a Number: ")) 
if is_prime(num):
    print(f"Yes {num} is a prime number!")  
else:
    print(f"No {num} is not a a prime number!")       

print("=" * 60)
print("Odd or Even Number Detector " .center(60, "-"))
print("=" * 60)


number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an even number!")
else:
    print(f"{number} is an odd number!")



print("=" * 60)
print("END OF CHALLENGE" .center(60, "-"))
print("=" * 60)




   