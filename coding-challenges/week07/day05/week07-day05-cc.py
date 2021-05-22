
# Question 1. Write a program using recursion to count the number of vowels in a string.


def isVowel(char):             
  char = char.lower()    
  vowels = "aeiou"                 

  if char in vowels:           
    return 1
  else:
      return 0

def countVowels(str):            
	count = 0
	for i in range(len(str)): 
		if isVowel(str[i]) :    
			count += 1
	return count 

                                        
string = input("Enter String: ")                
print("No Of V Present in String:", countVowels(string)) 


#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(N)                 |
#    | Space Complexity  =  O(N)                 |
#    |                                           |
#    |___________________________________________|




# Question 2. Write a program to find the fibonacci number in a string.


def fibonacciNum(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibonacciNum(n-1) + fibonacciNum(n-2)) 



nterms = int(input("Enter terms Fibon num: "))  

if nterms <= 0:  
   print("Enter Positive Integer")  
else:
    fiboNum = [] 
    for i in range(nterms):
        fiboNum.append(fibonacciNum(i))

    print("Fibonacci sequence:", fiboNum)  


#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(N)                 |
#    | Space Complexity  =  O(N)                 |
#    |                                           |
#    |___________________________________________|




# Question 3. Write a program to find the length of a string using recursion.


def string_length(str) :
	
	if str == '':
		return 0
	else :
		return 1 + string_length(str[1:])
	

str = input("Enter String: ")
print ("Length Of String:", string_length(str))


#    ____________________________________________
#    |                                           |
#    |                                           |
#    | Time Complexity   =  O(N)                 |
#    | Space Complexity  =  O(N)                 |
#    |                                           |
#    |___________________________________________|


