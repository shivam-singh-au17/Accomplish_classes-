

def adj(string1,n):
    for i in range(n):
        if string1[i] == "?":
            if i == 0:
                if string1[i + 1] != "1":
                    string1[i] = "1"
                elif string1[i + 1] != "2":
                    string1[i] = "2"
                else:
                    string1[i] = "3"
            elif i == n - 1:
                if string1[i - 1] != "1":
                    string1[i] = "1"
                elif string1[i - 1] != "2":
                    string1[i] = "2"
                else:
                    string1[i] = "3"
            else:
                if string1[i - 1] != "1" and string1[i + 1] != "1":
                    string1[i] = "1"
                elif string1[i - 1] != "2" and string1[i + 1] != "2":
                    string1[i] = "2"
                else:
                    string1[i] = "3"
    print("".join(string1))
    
input1 = input()
n1 = len(input1)
string1 = list(input1)
adj(string1,n1)

