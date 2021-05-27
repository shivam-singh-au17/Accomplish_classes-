
#  Q - 1 ) Tell space complexity of following piece of code: (5 marks)

#       for i in range(n):
#           for j in range(n):
#               print(“Space complexity”)



"""  
           ____________________________________________
           |                                           |
           |                                           |
           |     Space Complexity  =  O(1)             |
           |                                           |
           |___________________________________________|

"""




"""
Q - 2 ) https://leetcode.com/problems/plus-one/
Leet code link :

"""


class Solution:
    def plusOne(self, digits):
        d_len = len(digits)
        for i in reversed(range(d_len)):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            else:
                digits[i] = 0
                
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits





"""
Q - 3) https://leetcode.com/problems/flipping-an-image/
Leet code link :

"""


class Solution:
    def flipAndInvertImage(self, image):
        
        arrInvert = []
        arrReverse = []
        for i in  image:
            i.reverse()
            arrInvert = []
            for j in i:
                if j == 0:
                    j = 1
                else:
                    j = 0
                arrInvert.append(j)
            arrReverse.append(arrInvert)
        return arrReverse
        





#    Q - 4 ) (Objective of this question is to make you utilise memory(space
#    better)) (2 marks)
#       Reverse an array of integers and do not use inbuilt functions like “reverse”,
#       don’t use shorts hands like “arr[::-1]”. Only use following approach:
#       swap first and last element,
#       then second and second last element,



def reverseArray(arr, n):
	for i in range(n//2):
		arr[i], arr[(n + ~i + 1) + ~1 + 1] = arr[(n + ~i + 1) + ~1 + 1],arr[i]

arr = [ 5, 3, 7, 2, 1, 6 ]
n = len(arr)
reverseArray(arr, n)

for i in range(n):
	print(arr[i],end=" ")



    