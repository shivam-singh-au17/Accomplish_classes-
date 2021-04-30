# [All questions need to be solved using both for and while loop]

# 1. Write code for the following sequence by taking line number as user input: 

#                            n=5
#                                  **
#                                   **
#                                    **
#                                   **
#                                  **


#              n=3
#                   **
#                    **
#                   ** 



n = int(input("enter any number of lines: "))
for line_number in range(n, 0, -1):
    if line_number <= (n//2 + n%2):
        print(" "*(n-line_number),"*"*2)
        
for line_number in range(1, n+1):
    if line_number <= (n//2):
        if n % 2 == 0:
            print(" "*(n-line_number),"*"*2)
        else:
            print(" "*(n-line_number - 1),"*"*2)




# 2. Write code for the following sequence by taking line number as user input.

#                               n = 3
#                                         1
#                                        121
#                                       12321


#                   n = 4
#                              1
#                             121
#                            12321
#                           1234321 



num = int(input("Enter your number: "))
odd = 1
space = num - 1
for i in range(1, num+1):
    k=0
    for j in range(1, space+1):
        print(" ",end='')
    for j in range(1, odd+1):
        if(j<=i):
            k=k+1
        else:
            k=k-1
        print(k,end="")
    print()
    odd=odd + 2
    space= space - 1




# 3. Write code for the following sequence by taking line number as user input
#                               n = 3
#                                        1
#                                       121
#                                        1

#             n = 5
#                      1
#                     121
#                    12321
#                     121
#                      1 



num = int(input("Enter your number: "))
i = 0
while i < num:
    if i <= (num // 2 ):
        print("  "*(num-i),end=" ")
        j = 0
        while j - 1 < i*2:
            if (j+1) > (i+1):
                print((i*2)-j+1 ,end=" ")
            else:
                print(j+1,end=" ")
            j += 1
        print()
        i += 1
    else:
        i = num//2 - 1
        while i > -1:
            print("  "*(num-i),end=" ")
            j = 0
            while j - 1 < i*2:
                if (j+1) > (i+1):
                    print((i*2)-j+1 ,end=" ")
                else:
                    print(j+1,end=" ")
                j += 1
            print()
            i -= 1
        break       




# 4. Write code for the following sequence by taking line number as user input, [using a single loop only]

#                n = 5 
#                        1
#                        21
#                        321
#                        21
#                        1 



n = int(input("enter any odd number of lines: "))
for i in range(1, n+1):
    if i <= (n//2 + n%2):
        for j in range(i, 0, -1):
            print(j, end="")
        print()
for i in range(n, 0, -1):
    if i <= (n//2):
        for j in range(i, 0, -1):
            print(j, end="")
        print()




# 5. Write a function that takes line number as input (with default value of 5) and prints the following pattern.

#                                 n=3
#                                      .....
#                                      .. ..
#                                      . .
#                                      .. ..
#                                      .....


#             n = 5
#                     .......
#                     ... ...
#                     .. ..
#                     . .
#                     .. ..
#                     ... ...
#                     ....... 


def dot_pattern():
    
    n = int(input("Enter any number: "))
    print("."*(n+2))
    for i in range(n, 0, -1):
        if i <= (n//2 + n%2):
            print("."*i,"."*i)
    for i in range(2, n):
        if i <= (n//2 + n%2):
            print("."*i,"."*i)
    print("."*(n+2))

    
dot_pattern()




