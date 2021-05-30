
def SubArray(items):

    dict_L = {}    # value & first index
    dict_R = {}    # value & last index
    count = {}     # value & count(how many time this value occur)

    for index, value in enumerate(items):
        if value not in dict_L: 
            dict_L[value] = index
            
        dict_R[value] = index
        count[value] = count.get(value, 0) + 1  # If its value comes again, make it plus one otherwise give zero

    ans = len(items)
    temp = max(count.values())

    for i in count:
        if count[i] == temp:
            ans = min(ans, dict_R[i] - dict_L[i] + 1)

    return ans



if __name__=="__main__":

    n = 6
    numArr = [1, 2, 3, 4, 3, 1]

    # n = int(input())
    # numArr = list(int(num) for num in input().strip().split())[:n]
    
    result = SubArray(numArr)
    print(result)

    