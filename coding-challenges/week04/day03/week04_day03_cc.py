

#     Write a function which takes a list as an input from the user [using the input()
#     command] and returns the highest and the second highest elements of a list.
#     Ex:
#     Input 1:
#     1 2 3 4
#     Output 1:
#     3 4
#     Input 2:
#     1 2 3 8 7
#     Output 2:
#     7 8




def highest():

    l1 = input("Enter the list as space separated numbers: ")
    new_l1 = l1.split(" ")
    for idx in range(0, len(new_l1)):
        new_l1[idx] = int(new_l1[idx])

    m_l = max(new_l1)
    g = new_l1.remove(m_l)
    m_l2 = max(new_l1)
    s =  m_l , m_l2
    return list(s)
  
ans = highest()
print(ans)






#     Write a function called MaxSeq() which can take any number of inputs from the
#     user and returns the highest number in that sequence as the output.
#     [You cannot use the inbuilt function max() of python]
#     Ex:
#     Input 1:
#     11 2 3 4
#     Output 1:
#     11
#     Input 2:
#     1 2 3 8 7
#     Output 2:
#     8
#     Hint: https://www.programiz.com/python-programming/args-and-kwargs visit this
#     link to understand how to call a python function with multiple inputs.



def MaxSeq():
    l1 = input("Enter the list as space separated numbers: ")
    new_l1 = l1.split(" ")
    for idx in range(0, len(new_l1)):
        new_l1[idx] = int(new_l1[idx])

    max_num = new_l1[0]
    for i in range(0, len(new_l1)):
        if(new_l1[i] > max_num):
            max_num = new_l1[i]
    return max_num

ans2 = MaxSeq()
print(ans2)


