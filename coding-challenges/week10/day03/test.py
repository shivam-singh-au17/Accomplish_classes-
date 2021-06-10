
# def binaryToDecimal(binary):
# 	value = 0
# 	i = 0
# 	while(binary != 0):

# 		dec = binary % 10
# 		value = value + dec * pow(2, i)
# 		binary = binary // 10
# 		i += 1

# 	print(value)	
	


# if __name__ == '__main__':
# 	binaryToDecimal(100)
# 	binaryToDecimal(101)
# 	binaryToDecimal(1001)




def DecimalToBinary(num):
	
    binary = ""
    while num > 0:
        rem = num % 2
        binary += str(rem)

        num = num // 2

    return binary[::-1]


if __name__ == '__main__':

    dec_val = 24
    ans = DecimalToBinary(dec_val)
    print(ans)


