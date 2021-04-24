
# a. Print the following pattern after taking in the line number as input from the user: 


n = int(input("enter any odd number of lines: "))
for line_number in range(1, n+1):
    if line_number <= (n//2 + n%2):
        print(" "*(n-line_number),"*"*(2*line_number -1))
        
for line_number in range(n, 0, -1):
    if line_number <= (n//2):
        print(" "*(n-line_number),"*"*(2*line_number -1))


                        

# b. perform the same task as given above but using one for loop only instead of 2



n= int(input("enter any odd number of lines: "))
for line_number in range(1,n+1):
  if line_number <= (n//2 + n%2):
    print(" "*((n//2)-line_number+1),"*"*(2*line_number-1))
  else:
    print(" "*(line_number-(n//2)-1),"*"*(2*(n-line_number)+1))

    