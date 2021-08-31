def IntervalIntersection(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)):
            if i!=j and arr[i][0]>=arr[j][0] and arr[i][1]<=arr[j][1]:
                return True
    return False


if __name__=="__main__":
    
    r = int(input())

    matrix = []
    for i in range(r):
       row = list(map(int, input().split()))
       matrix.append(row)

    if IntervalIntersection(matrix) == False:
        print("NO")
    else:
        print("YES")