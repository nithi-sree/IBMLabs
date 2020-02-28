#Dynamic Multiplication
colx = int(input("ColumnX: "))
rowx = int(input("RowX: "))
coly = int(input("ColumnY: "))
rowy = int(input("RowY: "))

A = []
B = []

print("Enter the Elements of First Matrix: ")
for i in range(rowx):
    x = []
    for j in range(colx):
        x.append(int(input()))
    A.append(x)

print("Enter the Elements of Second Matrix: ")
for i in range(coly):
    y = []
    for j in range(rowy):
        y.append(int(input()))
    B.append(y)

print("FirstMatrix: ", A)
print("SecondMatrix: ", B)

result = [[0 for j in range(len(B[0]))] for i in range(len(A))]

#through rows of x
for i in range(len(A)):
    #through columns of y
    for j in range(len(B[0])):
        #through rows of y
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]


for r in result:
    print(r)


'''
#Static Input
# Program to multiply two matrices using nested loops

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
'''