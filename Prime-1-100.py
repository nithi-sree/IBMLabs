for num in range(2, 101):
    count = 0
    for i in range(2, num//2 + 1):
        if (num % i) == 0:
            count = 1
            break
    if count == 0:
        print(num, end=" ")


print()
flag = 0
print(2, end=" ")
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            flag = 0
            break
        else:
            flag = 1
    if flag == 1:
        print(i, end=" ")
