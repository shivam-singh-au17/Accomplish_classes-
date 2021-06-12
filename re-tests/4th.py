
def plusOne(digits):       
    b = [str(i) for i in digits]
    c = ''.join(b)
    d = int(c)+1
    new = list()
    for i in str(d):
        new.append(int(i))
    return new


def printres(nums):
    ans = ""
    for i in range(0, len(nums)):
        ans += str(nums[i]) + " "
    return ans


if __name__=="__main__":

    n = int(input())
    numArr = list(int(num) for num in input().strip().split())[:n]

    ans = plusOne(numArr)
    ans2 = printres(ans)
    print(ans2)