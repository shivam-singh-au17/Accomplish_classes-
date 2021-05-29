"""
Find sum at odd and even places
https://www.hackerrank.com/contests/attainu-subrahmanyam-decmonth-test/challenges

"""



# n = int(input("enter n :"))

# for k in range(n):
#     str = input("enter num :")
#     numArr = []
#     for i in range(len(str)):
#         numArr.append(int(str[i]))

#     newArr = numArr
#     sumA = 0
#     for j in range(len(newArr)):
#         sumA = sumA + newArr[j]
#     print(sumA)





"""
Good Substring 
https://www.hackerrank.com/contests/attainu-subrahmanyam-decmonth-test/challenges

"""




# str = 'ababa'

# arrStr = []
# for i in range(0, len(str)):
#     subStr = ""
#     for j in range(i, len(str)):
#         subStr += str[j]
#         arrStr.append(subStr)

# dict = {}

# for i in arrStr:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1

# maxArr = []

# for key,value in dict.items():
#     if value >= 2:
#         maxArr.append(key)

# if maxArr == []:
#     print(-1)
# else:
#     keyLen = ""
#     for key in maxArr:
#         if len(key) > len(keyLen):
#             keyLen = key
#     print(keyLen)






"""
Sweet Dish
https://www.hackerrank.com/contests/attainu-subrahmanyam-decmonth-test/challenges

"""





# def solve(arr):
#     first = 0
#     second = 0 
#     for i in arr:
#         if second > first:
#             new = second
#         else:
#             new = first
        
#         first = second + i 
#         second = new
#     if second > first:
#         return second
#     else:
#         return first  

# testCase = int(input())

# for i in range(0,testCase):
#     n = int(input())
#     arr = list(map(int,input().split()))[:n]

#     print(solve(arr))







"""
Max Sum 7
https://www.hackerrank.com/contests/mock-test-kalam-batch/challenges

"""





# n = int(input())
# arr = list(map(int,input().split()))[:n]

# sumArr = 0
# for i in range(0, len(arr)):
#     sumArr += arr[i]

# SubArray = []
# for i in range(0, len(arr)):
#     subArr = 0
#     for j in range(i, len(arr)):
#         subArr += arr[j]
#         SubArray.append(subArr)


# temp = False
# for k in range(0, len(SubArray)):
#     if SubArray[k] > sumArr:
#         temp = True
    
# if sumArr < 0:
#     print('YES')
# else:
#     if temp == True:
#         print('YES')
#     else:
#         print('NO')





"""
Reducing String
https://www.hackerrank.com/contests/mock-test-kalam-batch/challenges

"""




# stri = input()
# def string(stri):
#     result = ""
#     count = 1
#     temp = stri[0]
#     for i in range(0, len(stri)):
#         if (stri[i] == temp):
#             count = count + 1   
#         else:
#             result += temp
#             count = 1
#             temp = stri[i]
           
#     result += temp
#     return result

# ans = string(stri)
# print(ans)





"""
Diagonal Difference
https://www.hackerrank.com/contests/aryabhata-fprt-july/challenges

"""




# def diagonalDifference(arr):

#     row = len(arr)
#     col = len(arr[0])

#     firstDiago = 0;
#     secondDiago = 0;

#     for i in range(0, row):
#         firstDiago += (arr[i][(col - i) - 1])
#         for j in range(0, col):
#             if i == j:
#                 secondDiago += (arr[i][j])
       
#     diff = firstDiago - secondDiago
#     return abs(diff)


# if __name__=="__main__":

#     arr = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 6],
#     [7, 8, 9, 9],
#     [2, 4, 1, 3]
# ]

# result = diagonalDifference(arr)
# print(result)







"""
The Social Distancing 1
849. Maximize Distance to Closest Person leetcode problem
https://www.hackerrank.com/contests/mock-test-kalam-batch/challenges

"""


# n = int(input())
# num_list = list(int(num) for num in input().strip().split())[:n]

# n = 7
# num_list = [1, 0, 1, 0, 0, 0, 1]

n = 4
num_list = [1, 0, 0, 0]

def maxDistToClosest(seats):
    people = (i for i, seat in enumerate(seats) if seat)
    prev, future = None, next(people)
    ans = 0
    for i, seat in enumerate(seats):
        if seat:
            prev = i
        else:
            while future is not None and future < i:
                future = next(people, None)
            left = float('inf') if prev is None else i - prev
            right = float('inf') if future is None else future - i
            ans = max(ans, min(left, right))
    return ans

ans = maxDistToClosest(num_list)
print(ans)

