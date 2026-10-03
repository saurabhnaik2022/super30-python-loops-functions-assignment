# Q14: Own sum() - FUNCTION so the logic is reusable; FOR loop inside to add items
# def my_sum(numbers)
# It should accept a list of numbers and return their sum
# without using Python's built-in sum().
def my_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


print(my_sum([1, 2, 3, 4, 5]))      # 15
print(my_sum([10.5, 20.5]))         # 31.0
print(my_sum([]))                   # 0
