
def solveArr(nums):
   evens = [num for num in nums if num % 2 == 0]
   odds = [num for num in nums if num % 2 != 0]
   evens.sort()
   odds.sort(reverse=True)
   even_i = 0
   odd_i = 0
   for index in range(len(nums)):
      if nums[index] % 2 == 0:
         nums[index] = evens[even_i]
         even_i += 1
      else:
         nums[index] = odds[odd_i]
         odd_i += 1
   return nums


def printres(nums):
    ans = ""
    for i in range(0, len(nums)):
        ans += str(nums[i]) + " "
    return ans



if __name__=="__main__":
    n = int(input())
    numArr = list(int(num) for num in input().strip().split())[:n]

    ans = solveArr(numArr)
    ans2 = printres(ans)
    print(ans2)

