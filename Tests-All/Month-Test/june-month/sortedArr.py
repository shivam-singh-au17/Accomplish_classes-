

# def sortSquare(arr, n):

# 	for i in range(n):
# 		arr[i]= arr[i] * arr[i]
# 	arr.sort()


# # arr = [-6, -3, -1, 2, 4, 5]
# arr = [-9, -2, 0, 2, 3]
# n = len(arr)


# sortSquare(arr, n)

# for i in range(n):
# 	print(arr[i], end = " ")




def sortSquare(arr, n):

    for i in range(n):
        arr[i]= arr[i] * arr[i]

    arr.sort()



if __name__=="__main__":

    n = int(input())
    numArr = list(int(num) for num in input().strip().split())[:n]

    sortSquare(numArr, n)

    for i in range(n):
        print(numArr[i], end = " ")

        