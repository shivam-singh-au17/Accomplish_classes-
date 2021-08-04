# b_num = input()
b_num = '001010111'
num = list(b_num)



def string(stri):
    count = 0
    temp = '1'
    for i in range(0, len(stri)):
        if (stri[i] == temp):
            count = count + 1
        if count == 2:
            return stri[:i], stri[i:]
           
ans = string(num)
ans3 = list(ans)

def string1st(stri):
    count = 0
    temp = '0'
    for i in range(0, len(stri)):
        if (stri[i] == temp):
            count = count + 1
    return count


def string2nd(stri):
    count = 0
    temp = '1'
    for i in range(0, len(stri)):
        if (stri[i] == temp):
            count = count + 1
    return count
        
res2 = string1st(ans3[0]) 

res3 = string2nd(ans3[1])

print(res2 + res3)





# def binaryToDecimal(num):
#     value = 0
#     for i in range(len(num)):
#         digit = num.pop()
#         if digit == '1':
#             value = value + pow(2, i)
#     return value

# ans2 = binaryToDecimal(ans3[0])
# print(ans2)
# ans2 = binaryToDecimal(ans3[1])
# print(ans2)