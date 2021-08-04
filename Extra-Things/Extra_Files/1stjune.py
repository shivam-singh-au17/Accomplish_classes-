

arr = [8, 8, 5, 3, 2, 8, 9, 7, 5, 3]
min = 1
newArr = []
for i in range(0, len(arr)):
    if arr[i] > min:
        newArr.append(arr[i])
        # arr.remove(arr[i])
print(newArr)
