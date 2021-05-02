

#     You are given an integer, n. Your task is to print an alphabet rangoli of size .
#     (Rangoli is a form of Indian folk art based on creation of patterns.)
#     Different sizes of alphabet rangoli are shown below:

#     #size 3
#            ----c----
#            --c-b-c--
#            c-b-a-b-c

#     #size 5
#            --------e--------
#            ------e-d-e------
#            ----e-d-c-d-e----
#            --e-d-c-b-c-d-e--
#            e-d-c-b-a-b-c-d-e

#     #size 10
#            ------------------j------------------
#            ----------------j-i-j----------------
#            --------------j-i-h-i-j--------------
#            ------------j-i-h-g-h-i-j------------
#            ----------j-i-h-g-f-g-h-i-j----------
#            --------j-i-h-g-f-e-f-g-h-i-j--------
#            ------j-i-h-g-f-e-d-e-f-g-h-i-j------
#            ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
#            --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
#            j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j

#     The center of the rangoli has the first alphabet letter a, and the boundary has
#     the alphabet letter (in alphabetical order).
print() #for space





n = int(input("Enter Rngoli Size Number: "))
print() #for space
# albt = list(map(chr,range(97,123)))

albt = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
'x', 'y', 'z']

for i in range(n-1,-1,-1):
    for j in range(2*i):
        print(end="-")
    for j in range(n-1,i-1,-1):
        if i != (n-1):
            print(albt[j],end="-")
        else:
            print(albt[j],end="")
    for j in range(1,n-i):
        if j != (n-i-1):
            print(albt[j+i],end="-")
        else:
            print(albt[j+i],end="")
    for j in range(2*i):
        print(end="-")
    print()





print() #for space
#     [Hint: Use the chr() and ord() function in python and then try to build this
#     pattern]

#     Sample Input
#                   5
#     Sample Output
#                  --------e--------
#                  ------e-d-e------
#                  ----e-d-c-d-e----
#                  --e-d-c-b-c-d-e--
#                  e-d-c-b-a-b-c-d-e
#                  --e-d-c-b-c-d-e--
#                  ----e-d-c-d-e----
#                  ------e-d-e------
#                  --------e--------

    



n = int(input("Enter Rngoli size Number: "))
print() #for space


for i in range(n):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))

for i in range(n-1):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))





print() #for space
#     You are given an integer, n. Your task is to print an alphabet rangoli of size .
#     (Rangoli is a form of Indian folk art based on creation of patterns.)
#     Different sizes of alphabet rangoli are shown below:

#     #size 3
#            ----c----
#            --c-b-c--
#            c-b-a-b-c
#            --c-b-c--
#            ----c----

#     #size 5
#            --------e--------
#            ------e-d-e------
#            ----e-d-c-d-e----
#            --e-d-c-b-c-d-e--
#            e-d-c-b-a-b-c-d-e
#            --e-d-c-b-c-d-e--
#            ----e-d-c-d-e----
#            ------e-d-e------
#            --------e--------

#     #size 10
#             ------------------j------------------
#             ----------------j-i-j----------------
#             --------------j-i-h-i-j--------------
#             ------------j-i-h-g-h-i-j------------
#             ----------j-i-h-g-f-g-h-i-j----------
#             --------j-i-h-g-f-e-f-g-h-i-j--------
#             ------j-i-h-g-f-e-d-e-f-g-h-i-j------
#             ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
#             --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
#             j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
#             --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
#             ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
#             ------j-i-h-g-f-e-d-e-f-g-h-i-j------
#             --------j-i-h-g-f-e-f-g-h-i-j--------
#             ----------j-i-h-g-f-g-h-i-j----------
#             ------------j-i-h-g-h-i-j------------
#             --------------j-i-h-i-j--------------
#             ----------------j-i-j----------------
#             ------------------j------------------

#     The center of the rangoli has the first alphabet letter a, and the boundary has
#     the alphabet letter (in alphabetical order).





n = int(input("Enter Rngoli Size Number: "))
print() #for space
# albt = list(map(chr,range(97,123)))

albt = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
'x', 'y', 'z']

for i in range(n-1,0,-1):
    for j in range(2*i):
        print(end="-")
    for j in range(n-1,i-1,-1):
        if i != (n-1):
            print(albt[j],end="-")
        else:
            print(albt[j],end="")
    for j in range(1,n-i):
        if j != (n-i-1):
            print(albt[j+i],end="-")
        else:
            print(albt[j+i],end="")
    for j in range(2*i):
        print(end="-")
    print()

for i in range(n):
    for j in range(2*i):
        print(end="-")
    for j in range(n-1,i-1,-1):
        if i != (n-1):
            print(albt[j],end="-")
        else:
            print(albt[j],end="")
    for j in range(1,n-i):
        if j != (n-i-1):
            print(albt[j+i],end="-")
        else:
            print(albt[j+i],end="")
    for j in range(2*i):
        print(end="-")
    print()





print() #for space
#     [Hint: Use the chr() and ord() function in python and then try to build this
#     pattern]
#     Constraints: Use a single while loop to solve this question

#     Sample Input
#                   5

#     Sample Output
#                   --------e--------
#                   ------e-d-e------
#                   ----e-d-c-d-e----
#                   --e-d-c-b-c-d-e--
#                   e-d-c-b-a-b-c-d-e
#                   --e-d-c-b-c-d-e--
#                   ----e-d-c-d-e----
#                   ------e-d-e------
#                   --------e--------





n = int(input("Enter Rngoli size Number: "))
print() #for space

i = 0
while i < n:
    s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))
    i = i + 1
i = 0
while i < (n -1):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))
    i = i + 1


print()  #for space

