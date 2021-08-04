
def checkValidOrNot(arr, n):

    temp = 0

    for i in range (0, n):
        if (arr[i]):
            temp = temp + 1
        else:
            temp = temp - 1
        if (temp < 0):
            return False

    return True


testCases = int(input())

for i in range(0,testCases):
    
    n = int(input())
    arr = list(map(int,input().split()))

    if (checkValidOrNot(arr, n)):
        print("Valid")
    else:
        print("Invalid")
        
        
        