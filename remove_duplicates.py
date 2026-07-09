# Remove duplicates from list while preserving order

# Approach 1: Using list (O(n^2))

num = [1, 2, 3, 2, 4, 1]

unique = []

for element in num:
    if element not in unique:
        unique.append(element)

print("Unique elements:", unique)


# Approach 2: Using set (Optimized - O(n))

unique = []
seen = set()

for element in num:
    if element not in seen:
        unique.append(element)
        seen.add(element)

print("Unique elements (optimized):", unique)
