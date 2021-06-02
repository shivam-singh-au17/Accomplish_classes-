
# Q-1 ) Select the appropriate code that performs selection sort.


"""
# a)
        for j in range(n):
            min = j
            for k in range(j+1,n):
                if(arr[k] < arr[min]):
                    min = k
            temp = arr[min]
            arr[min] = arr[j]
            arr[j] = temp

# b)
        for j in range(n):
            min = j
            for k in range(j+1,n+1):
                if(arr[k] < arr[min]):
                    min = k
        temp = arr[min]
        arr[min] = arr[j]
        arr[j] = temp


# c)
        for j in range(n):
            min = j
            for k in range(j+1,n+1):
                if(arr[k] > arr[min]):
                    min = k
        int temp = arr[min]
        arr[min] = arr[j]
        arr[j] = temp


# d)
        for j in range(n):
            min = j
            for k in range(j+1,n+1):
                if(arr[k] > arr[min]):
                    min = k
        int temp = arr[min]
        arr[min] = arr[j]
        arr[j] = temp

"""



"""  
           ____________________________________________
           |                                           |
           |                                           |
           |          perfect choice => (a)            |
           |                                           |
           |___________________________________________|

"""





# Q-2 ) What is the worst case complexity of selection sort? (5 marks)


"""
    a) O(nlogn)
    b) O(logn)
    c) O(n)
    d) O(n^2)

"""


"""  
           ____________________________________________
           |                                           |
           |                                           |
           |          perfect choice => (d)            |
           |                                           |
           |___________________________________________|

"""





# Q-3 ) Write a program perform selection sort using an auxiliary (extra) list,
# and tell the time complexity and space complexity of your code. (5 marks)


def selection_sort(A):

    n = len(A)
    for i in range(n):
        min_ele = A[i]
        min_ele_idx = i
        for idx in range(i, len(A)):
            if A[idx] < min_ele:
                min_ele = A[idx]
                min_ele_idx = idx
        A[i], A[min_ele_idx] = A[min_ele_idx], A[i]
    return A


if __name__ == "__main__":

    A = [6, 7, 1, 2, 4, 5, 6]
    print(selection_sort(A))


"""  
           ____________________________________________
           |                                           |
           |     Time Complexity   =  O(N^2)           |
           |     Space Complexity  =  O(1)             |
           |                                           |
           |___________________________________________|

"""





# Q-4 )[BONUS QUESTION] Write a while loop implementation of selection
# sort? (5 marks)


def selection_sort(A):
   
    n = len(A)
    i = 0
    while (i < (n -1)) :
        min_ele = A[i]
        min_ele_idx = i
        j = i
        while ((j+1) < n ):
            j += 1
            if A[j] < min_ele:
                min_ele = A[j]
                min_ele_idx = j
        A[i], A[min_ele_idx] = A[min_ele_idx], A[i]

        i += 1

    return A


if __name__ == "__main__":

    A = [6, 7, 1, 2, 4, 5, 6]
    print(selection_sort(A))


"""  
           ____________________________________________
           |                                           |
           |     Time Complexity   =  O(N^2)           |
           |     Space Complexity  =  O(1)             |
           |                                           |
           |___________________________________________|

"""



# Marks distribution:
# Question 1,2 and 3 carry 5 marks each.
# Question 4 is a bonus question, that means if you leave that question you don't lose a mark, but
# if you solve it, you can extra 5 marks.
# Remark: maximum marks you can get is 15, bonus question helps only of you are not able to
# solve another question.




