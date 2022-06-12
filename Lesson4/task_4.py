arr = [8, 4, 56, 34, 8, 43, 4, 34, 7, 98, 4, 8]
arr1 = []
for el in arr:
    if arr.count(el) > 2:
        arr1.append(el)
print(arr)
print(arr1)