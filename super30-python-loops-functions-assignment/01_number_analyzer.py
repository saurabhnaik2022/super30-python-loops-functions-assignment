# Q1: Number Analyzer - FOR loop because we know the range (1..N) in advance
# Take a number N from the user. Print all numbers from 1 to N, 
# identify whether each number is even or odd, and
# finally display the total count of even and odd numbers.

n = int(input("Enter N: "))
even_count = odd_count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, "is Even")
        even_count += 1
    else:
        print(i, "is Odd")
        odd_count += 1

print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)
