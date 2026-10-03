# Q15: Reusable Number Analysis - FUNCTION that RETURNS results (not just prints)
def analyze_number(number):
    # Sign
    if number > 0:
        sign = "Positive"
    elif number < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    # Even / Odd
    parity = "Even" if number % 2 == 0 else "Odd"

    # Prime check (only numbers > 1 can be prime)
    prime = number > 1
    for i in range(2, int(abs(number) ** 0.5) + 1):
        if number % i == 0:
            prime = False
            break

    return {"sign": sign, "parity": parity, "prime": "Prime" if prime else "Not Prime"}


n = int(input("Enter a number: "))
result = analyze_number(n)
print(f"{n} -> {result['sign']}, {result['parity']}, {result['prime']}")
