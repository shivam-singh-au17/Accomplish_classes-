# data = [
#     [1, 2, 3],
#     [5, 6, 7],
#     [7, 8, 9]
# ]

# # for i in range(0, len(data)):
# #     for j in range(0, len(data)):
# #         print(data[i][j])

# for i in range(0, len(data)):
#     print(data[0][i])

Raw = int(input("Enter the number of rows:"))
Clm = int(input("Enter the number of columns:"))

mat = []

print("Enter the entries rowwise:")
a = [] 
for i in range(Raw):          
    for j in range(Clm):      
         a.append(int(input()))
    mat.append(a)

for i in range(Raw):
    for j in range(Clm):
        print(mat[i][j], end = " ")
    print()
