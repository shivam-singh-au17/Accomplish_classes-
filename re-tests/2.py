

def runningSum(nums):
    sum = 0
    for i,n in enumerate(nums):
        sum += n
        nums[i] = sum        
    return nums


def printres(nums):
    ans = ""
    for i in range(0, len(nums)):
        ans += str(nums[i]) + " "
    return ans



if __name__=="__main__":

    n = int(input())
    numArr = list(int(num) for num in input().strip().split())[:n]

    ans = runningSum(numArr)
    ans2 = printres(ans)
    print(ans2)