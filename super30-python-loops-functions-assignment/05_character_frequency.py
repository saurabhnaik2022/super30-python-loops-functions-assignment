# Q5: Character Frequency - FOR loop + dictionary to store counts
# Take a string from the user and calculate how many times each character occurs. 
# Example: "banana" should identify the frequencies of b, a, and n.
text = input("Enter a string: ")
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch, count in freq.items():
    print(f"'{ch}' -> {count}")
