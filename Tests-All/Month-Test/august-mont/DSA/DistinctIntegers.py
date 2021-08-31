
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    # Write your code here
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0 for i in range(n)]
    dist = dict()
    dist[a[0]] = True
    dp[0] = 1
    
    for i in range(1, n):
        if a[i] not in dist:
            dist[a[i]] = True
            dp[i] += 1
        
        dp[i] += dp[i - 1]
    
    ans = []
    
    for i in range(q):
        query = int(input())
        ans.append(dp[query - 1])
    print(*ans, sep=" ")