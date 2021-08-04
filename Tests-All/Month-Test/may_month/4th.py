

def minDeletions(s):
   
    M_del = 0
    dic = set()
    for i in set(s):
        count = s.count(i)
        while count in dic and count != 0:
            count -= 1
            M_del += 1
        dic.add(count)
    return M_del


if __name__ == '__main__':
	
	str = input()
	print(minDeletions(str))




