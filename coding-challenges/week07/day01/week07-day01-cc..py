# Question 1 :
# ----------------
# Given a decimal Number , Write a program to convert Decimal to Binary
# number.
# Input : 10 (decimal)
# Output: - 1010
# Explanation:
# As, discussed in class , We can do %2 and //2 approach till the number is
# positive and store the remainder and then reverse the same.
# Sample :
# def Decimal_to_Binary(number):
# #write code here



no = int(input("Write your number converted to Binery: "))

def Decimal_to_Binary(number):
    binary_string = ""
    while number > 0:
        rem = number % 2
        binary_string += str(rem)
        number = number // 2
    return binary_string[::-1]

ans = Decimal_to_Binary(no)
print("The binary value is:",ans)

#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(N^2)                 |
#    | Space Complexity  =  O(M)                 |
#    |                                           |
#    |___________________________________________|


# --------------------------------------------------------------------------------------------------------

# Questions:2
# Write a program to convert Binary number (given as list) to decimal
# Integer
# Input: [1,0,1]
# Output: 5
# Explanation : -
# def Convert_Binary_to_Decimal(list1):
# #write code here



# 1st mathod
# def binaryToDecimal(n):
# 	num = n;
# 	binary_number = 0;
# 	base = 1;
# 	temp = num;
# 	while(temp):
# 		last_digit = temp % 10;
# 		temp = int(temp / 10);
		
# 		binary_number += last_digit * base;
# 		base = base * 2;
# 	return binary_number;

# num = 111;
# print(binaryToDecimal(num));



# 2nd mathod
b_num = list(input("Enter Binary number without spaces: "))

def binaryToDecimal(b_num):
    value = 0
    for i in range(len(b_num)):
    	digit = b_num.pop()
    	if digit == '1':
    		value = value + pow(2, i)
    return value

ans2 = binaryToDecimal(b_num)
print("The decimal value is:", ans2)




#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(N)                 |
#    | Space Complexity  =  O(M)                 |
#    |                                           |
#    |___________________________________________|


# --------------------------------------------------------------------------------------------------------

# Question : 3 -
# ------------------
# Given an integer array , every element is repeated TWICE , except one
# element , Find that element ?
# Input : - [1 , 2 , 1, 2 ,4 , 3 ,4 ,3]
# Output: - 3
# Explanation : HINT : - Use XOR operator ;



num = [1 , 2 , 1, 2 ,4, 3, 3]

def findElement(no):
    result = 0
    for i in range(len(no)):
        # return result ^ no[i]
        result = result ^ no[i] 
    return result

ans3 = findElement(num)
print("Output: -",ans3)


#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(N)                 |
#    | Space Complexity  =  O(M)                 |
#    |                                           |
#    |___________________________________________|


# ----------------------------------------------------------------