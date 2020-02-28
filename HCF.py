def compute_hcf(x, y):
    # smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if(x % i == 0) and (y % i == 0):
            hcf = i
    return hcf


n1 = int(input("a : "))
n2 = int(input("b : "))
print(compute_hcf(n1, n2))
