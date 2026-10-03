# Q7: Prime Number Finder - NESTED for loops (outer = each number, inner = divisor check)
# Ask the user for a starting and ending number. 
# Print all prime numbers within that range using nested loops.
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print(f"Primes between {start} and {end}:")
for num in range(max(start, 2), end + 1):
    is_prime = True
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()
