# Q16: Student Grade Function - FUNCTION with validation, returns total/percentage/grade
# Create a function that accepts marks for five subjects, 
# calculates total and percentage, and returns a grade based on rules you define
# such as A, B, C, D, or Fail. Add appropriate validation for invalid marks.
def calculate_grade(marks):
    if len(marks) != 5:
        return "Error: exactly 5 subjects required"
    for m in marks:
        if m < 0 or m > 100:
            return f"Error: invalid mark {m} (must be 0-100)"

    total = 0
    for m in marks:
        total += m
    percentage = total / 5

    # Fail if any subject is below 40
    if min(marks) < 40:
        grade = "Fail"
    elif percentage >= 85:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 55:
        grade = "C"
    else:
        grade = "D"
    return total, percentage, grade


marks = []
for i in range(1, 6):
    marks.append(float(input(f"Marks for subject {i}: ")))

result = calculate_grade(marks)
if isinstance(result, str):
    print(result)
else:
    print(f"Total: {result[0]}/500 | Percentage: {result[1]:.2f}% | Grade: {result[2]}")
