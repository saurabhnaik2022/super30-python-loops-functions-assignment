# Q3: Sum and Average without sum() - FOR loop to walk through every element
# Given a list of numbers, calculate the total and average using a loop. 
# Do not use Python's built-in sum() function.
numbers = [10, 20, 30, 40, 50]
total = 0
count = 0

for num in numbers:
    total += num
    count += 1

average = total / count
print("Numbers:", numbers)
print("Total:", total)
print("Average:", average)
