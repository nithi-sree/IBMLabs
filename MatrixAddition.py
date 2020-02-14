col = int(input("Column: "))
row = int(input("Row: "))

A = []
B = []

for i in range(row):
    x = []
    for j in range(col):
        x.append(int(input()))
    A.append(x)

for i in range(row):
    y = []
    for j in range(col):
        y.append(int(input()))
    B.append(y)

print("FirstMatrix: ",A)
print("SecondMatrix: ",B)

result = []
for i in range(row):
    z=[]
    for j in range(col):
        print(A[i][j]+B[i][j])
# for i in range(row):
#     z = []
#     for j in range(col):
#         z.append(A[i][j]+B[i][j])
#     result.append(z)
# print(result)




