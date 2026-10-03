# Q2: Multiplication Table - FOR loop with a fixed, then user-defined, range
# Take a number from the user and print its multiplication table from 1 × N through 10 × N 
# using a for loop. Then modify the program so the ending range can also be supplied by the user.
n = int(input("Enter a number: "))

print("--- Table up to 10 ---")
for i in range(1, 11):
    print(f"{i} x {n} = {i * n}")

end = int(input("Enter the ending range: "))
print(f"--- Table up to {end} ---")
for i in range(1, end + 1):
    print(f"{i} x {n} = {i * n}")
