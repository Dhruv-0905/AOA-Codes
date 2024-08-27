def prefix_function(pattern):
    m = len(pattern)
    π = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = π[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        π[q] = k
    return π

def kmp_match(text, pattern):
    n = len(text)
    m = len(pattern)
    π = prefix_function(pattern)
    i = 0
    for j in range(n):
        while i > 0 and pattern[i] != text[j]:
            i = π[i - 1]
        if pattern[i] == text[j]:
            i += 1
        if i == m:
            print("Pattern occurs with shift", j - m + 1)
            i = π[i - 1]

# Taking user input for text and pattern
text = input("Enter the text: ")
pattern = input("Enter the pattern to search: ")

# Calculate and print the prefix table
print("Prefix table:", prefix_function(pattern))

# Perform pattern matching
kmp_match(text, pattern)
