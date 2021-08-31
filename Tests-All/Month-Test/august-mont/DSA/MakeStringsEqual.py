
def stringsEqual(str1, str2):

    addStr = str1 + str2
    obj = {}

    for key in addStr:
        if key not in obj:
            obj[key] = 1
        else:
            obj[key] += 1

    for k in obj:
        if obj[k] % 2 != 0:
            return False

    return True



if __name__ == '__main__':

    str1 = input()
    str2 = input()

    if  stringsEqual(str1, str2) == True:
        print("YES")
    else:
        print("NO")