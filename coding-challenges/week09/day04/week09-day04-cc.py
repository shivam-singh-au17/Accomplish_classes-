
"""
Q-1 ) Find whether an array is subset of another array:(5 marks)
Examples:
Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1}
Output: arr2[] is a subset of arr1[]
Input: arr1[] = {1, 2, 3, 4, 5, 6}, arr2[] = {1, 2, 4}
Output: arr2[] is a subset of arr1[]
Input: arr1[] = {10, 5, 2, 23, 19}, arr2[] = {19, 5, 3}
Output: arr2[] is not a subset of arr1[]

"""





def findSubsetArr(arr1, arr2):
    count = 0
    temp = False
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            if arr1[i] == arr2[j]:
                count = count + 1
            if count == len(arr2):
                temp = True
    if temp == True:
        print("arr2[] is subset of arr1[]")
    else:
        print("arr2[] is not a subset of arr1[]")



if __name__ == "__main__":
	
	# arr1 = [11, 1, 13, 21, 3, 7]
	# arr2 = [11, 3, 7, 1]

	arr1 = [10, 5, 2, 23, 19]
	arr2 = [19, 5, 3]

	findSubsetArr(arr1, arr2)





"""
Q-2 )Sort an array of 0s, 1s and 2s:(5 marks)
Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that
sorts the given array. The functions should put all 0s first, then all 1s and all 2s in
last.
Examples:
Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}
Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}

"""





def sortArray(arr):
	left = 0
	right = len(arr) - 1
	mid = 0
	while mid <= right:
		if arr[mid] == 0:
			arr[left], arr[mid] = arr[mid], arr[left]
			left = left + 1
			mid = mid + 1
		elif arr[mid] == 1:
			mid = mid + 1
		else:
			arr[mid], arr[right] = arr[right], arr[mid]
			right = right - 1
	return arr
	


if __name__ == "__main__":
	
    # arr = [0, 1, 2, 0, 1, 2]
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

    arr = sortArray( arr)
    print(arr)





"""
Q-3 ) Sort an array in wave form :(5 marks)
Given an unsorted array of integers, sort the array into a wave like array. An
array ‘arr[0..n-1]’ is sorted in wave form if arr[0] >= arr[1] <= arr[2] >= arr[3] <=
arr[4] >= …..
Examples:
Input: arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
Output: arr[] = {10, 5, 6, 2, 20, 3, 100, 80} OR
{20, 5, 10, 2, 80, 6, 100, 3} OR
any other array that is in wave form

"""





def arrWaveForm(arr):
    arr.sort()
    for i in range(0, (len(arr) - 1), 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr



if __name__ == "__main__":
    arr = [10, 5, 6, 3, 2, 20, 100, 80]
    result = arrWaveForm(arr)
    print(arr)
	



