
"""
Q - 1) Write a program to print sum of right diagonal of a matrix: (5 marks)

"""





matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 6],
    [7, 8, 9, 9],
    [2, 4, 1, 3]
]


def sumOfRightDiagonal(matrix):
    row = len(matrix)
    col = len(matrix[0])
    rightDiagonalSum = 0

    for i  in range(row):
        for j in range(col):
            if i == row-j-1:
                rightDiagonalSum += matrix[i][j]

    return rightDiagonalSum


result = sumOfRightDiagonal(matrix)
print("sum of right diagonal :=>",result)







"""
Q - 2) Write a program to print sum of border elements of a square Matrix
(5 marks)

"""




matrix = [
    [1, 2, 3, 4],
    [4, 5, 6, 5],
    [7, 8, 9, 6],
    [4, 9, 8, 7]
]



def sumOfBorder(matrix):

    row = len(matrix)
    col = len(matrix[0])

    BorderSum = 0

    for i  in range(0, row):
        for j in range(0, col):
            if i == 0 or  j == 0 or i == row - 1 or j == col - 1:
                BorderSum += matrix[i][j]

    return BorderSum


result = sumOfBorder(matrix)
print("sum of border elements :=>",result)








"""
Q - 3) Write a function to return sum of rows of a matrix as a list: (5 marks)

"""



matrix = [
[1,  2,  3,  4 ],
[5,  6,  7,  8 ],
[9,  10, 11, 12],
[13, 14, 15, 16]
]



def sumOfRows(matrix):

    row = len(matrix)
    col = len(matrix[0])

    rowsSumArr = []
    for i in range(1, row + 1):
        rowsSum = 0
        for j  in range(0, col):
            rowsSum += matrix[i - 1][j]
        rowsSumArr.append(rowsSum)
    return rowsSumArr


result = sumOfRows(matrix)
print("sum of rows of a matrix :=>",result)




