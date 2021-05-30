

def diagonalSameElment(arr):

    row = len(arr)  
    col = len(arr[0])  

    firstDiago = [];

    for i in range(0, row):
        for j in range(0, col):
            if i == j:
                firstDiago.append(arr[i][j])
    print(firstDiago)

    for k in range(0, len(firstDiago)):   
        if firstDiago[k] == firstDiago[k+1]:
            return "YES"
        else:
            return "NO"
        
        
if __name__=="__main__":
    
    mat = []
    for i in range(1):
       row = list(map(int, input().split()))
       mat.append(row)

    r = mat[0][0]
    c = mat[0][1]

    matrix = []
    for i in range(r):
       row = list(map(int, input().split()))
       matrix.append(row)
    
    result = diagonalSameElment(matrix)
    print(result)
