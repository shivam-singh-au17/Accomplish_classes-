def N_Shows(arr):

    temp = float('-inf') 
    shifted = 0 
    for startingTime, EndingTime in sorted(arr, key = lambda x: x[1]):
        if startingTime < temp:
            shifted += 1
        else:
            temp = EndingTime

    num = len(arr)
    ans = num - shifted
    return ans



if __name__=="__main__":
    
    r = int(input())

    matrix = []
    for i in range(r):
       row = list(map(int, input().split()))
       matrix.append(row)

    print(N_Shows(matrix))