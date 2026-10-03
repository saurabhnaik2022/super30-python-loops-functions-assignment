# Q8: Pattern - NESTED for loops (outer = rows, inner = numbers in each row)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = int(input("Enter N: "))

for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()
