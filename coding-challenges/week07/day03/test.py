arr = [1, 2, 3, 4, 5]
count = 0
for i in range(0, len(arr), 2):
    count += arr[i]
count1 = 0
for i in range(0, len(arr), 3):
    count1 += arr[i]
    
count2 = 0
for i in range(0, len(arr), 4):
    count2 += arr[i]
    
count3 = 0
for i in range(0, len(arr), 5):
    count3 += arr[i]
if count3 > count and count3 > count1 and count3 > count2:
    print(count3)
elif count2 > count and count2 > count1 and count2 > count3:
    print(count2)
elif count1 > count and count1 > count2 and count1 > count3:
    print(count1)
else:
    print(count)
