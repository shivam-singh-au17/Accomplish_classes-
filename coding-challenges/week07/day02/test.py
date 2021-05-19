list1 = ["apple", "banana", "orange", "mango"]

traget = "apple"

def findFruits(items):
    for i in items:
        if i == traget:
            return True
    return False

ans = findFruits(list1)
print(ans)





def binarySearch(A, target):
    left = 0
    right = len(A) - 1

    while left <= right:
        mid = (left + right) // 2

        if A[mid] == target:
            return mid
        elif A[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


if __name__=="__main__":
    A = [1, 22, 44, 55, 66, 77, 88, 120, 135, 151]
    target = 55

    ans = binarySearch(A, target)
    print(ans)



def findLB(A, target):
    prev = -1
    for i in range(len(A)):
        if A[i] == target:
            return i
        elif A[i] > target:
            return prev
        prev = i


if __name__=="__main__":
    A = [1, 1, 1, 2, 2, 4, 4, 4, 5, 6]
    target = 5

    ans = findLB(A, target)
    print(ans)