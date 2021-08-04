

import math

def solve(num):
    if num < 10:
        return num
    sum = 0
    value = math.floor(math.log(num, 10) + 1)
    print('value', value)

    while value > 0:
        sum += num % 10
        num //= 10
        value -= 1
        
    return solve(sum)


if __name__ == "__main__":

    num = int(input())
    print(solve(num))


