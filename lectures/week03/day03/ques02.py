"""

b. perform the same task as given above but using one for loop only instead of 2. 

"""


# n= int(input("Enter the number of lines you want: "))
# for i in range(1,n+1):
#   if i<=(n//2)+1:
#     print(" "*((n//2)-i+1),"*"*(2*i-1))
#   else:
#     print(" "*(i-(n//2)-1),"*"*(2*(n-i)+1))


    # n = input("enter in number of lines: ")
# n = int(n)
# for line_number in range(1, n+1):
#   if line_number <= (n//2 + n%2):
#     print(" "*(n-line_number),"*"*(2*line_number -1))
#   else:
#      print(" "*((line_number- (n//2)- 1) + n%2 +1),"*"*(2*(n+1-line_number)-1))
   

num = 9
for i in range(1, num+1):
  i = i - (num//2 +1)
  if i < 0:
    i = -i
    print(" " * i + "*" * (num - i*2) + " "*i)


  
  
    
  
