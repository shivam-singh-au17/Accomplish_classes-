

class Solution:

   def solve(self, start, end):
      ct = 0
      while(end / 2 >= start):

         if end % 2 == 1:
            end -= 1
            end = end // 2
            ct += 2
         else:
            end = end // 2
            ct += 1
      ct += (end - start)

      return ct


n = int(input())
m = int(input())
ob = Solution()

print(ob.solve(n,m))



