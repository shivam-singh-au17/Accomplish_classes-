
def findIndex(arr, n, target):

    sum = [arr[0]]
    idx = None

    if arr[0] <= target:
        idx = 0

    for i in range(1, n):

        sum.append(sum[i - 1] + arr[i])
        if sum[i] <= target:
            idx = i

    if idx == None:
        return -1

    return idx


if __name__=="__main__":
    
    inpu = list(map(int,input().split()))
    n = inpu[0]
    k = inpu[1]

    arr = list(map(int,input().split()))
    ans = findIndex(arr, n, k)
    print(ans)
    








# def MIP(arr,target):
#     sum=[arr[0]]
#     idx=None
#     if arr[0]<=target[1]:
#         idx=0
#     for i in range(1,target[0]):
#         sum.append(sum[i-1]+arr[i])
#         if sum[i]<=target[1]:
#             idx=i
#     if idx==None:
#         return -1
#     return idx

# target=list(map(int,input().split()))
# arr=list(map(int,input().split()))
# print(MIP(arr,target))
    
