arr = [10, 20, 4, 45, 99]
largest = arr[0]
second_lar = float('-inf')
for element in arr:
    if element > largest:
        second_lar = largest
        largest = element
    elif element > second_lar and element != largest:
        second_lar = element

print(second_lar)
