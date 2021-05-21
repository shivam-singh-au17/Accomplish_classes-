


def upperbound(A, target):
    n = len(A)
    left = 0
    right = n - 1
    ans = -1
    while left <= right:
        mid = (left + right) >> 1      # or (left + right) // 2
        if A[mid] == target:
            ans = mid
            left = mid + 1
        elif A[mid] > target:
            right = mid - 1
        elif A[mid] < target:
            left = mid + 1
    return ans


if __name__ == "__main__":
    A = [1,2,2,2,3,3,5,5,5,6,6,7,7]
    x = 4
    print(upperbound(A, x))