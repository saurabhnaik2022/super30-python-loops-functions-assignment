# Q9: Student Marks Analyzer - FOR loop to compute all statistics in one pass
# Store marks of multiple students in a list. 
# Using loops, calculate highest marks, lowest marks, average marks, 
# number of students who passed, and number who failed. Consider 40 as the passing mark.
PASS_MARK = 40
marks = [78, 35, 92, 40, 56, 29, 67, 88]

highest = lowest = marks[0]
total = passed = failed = 0

for m in marks:
    total += m
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m
    if m >= PASS_MARK:
        passed += 1
    else:
        failed += 1

print("Marks:", marks)
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", round(total / len(marks), 2))
print("Passed:", passed)
print("Failed:", failed)
