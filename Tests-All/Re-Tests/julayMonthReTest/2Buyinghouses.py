




def solve(prices, k):
    prices.sort()
    total = 0
    for i, price in enumerate(prices):
        total += price
        if total > k:
            return i
    return len(prices)


if __name__=="__main__":
    
    inpu = list(map(int,input().split()))
    n = inpu[0]
    k = inpu[1]

    arr = list(map(int,input().split()))
    ans = solve(arr, k)
    print(ans)




    