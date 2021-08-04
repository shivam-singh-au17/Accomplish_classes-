 
stri = 'aaaaaabbbccccaaaaddf'

def string(stri):
    result = ""
    count = 1
    temp = stri[0]
    for i in range(0, len(stri)):
        if (stri[i] == temp):
            count = count + 1   
        else:
            result += temp
            count = 1
            temp = stri[i]
           
    result += temp
    return result

ans = string(stri)
print(ans)