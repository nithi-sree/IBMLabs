def compute_lcm(x, y):
    #select greater number
    if x>y:
        greater = x
    else:
        greater = y
    while True:
        if((greater % x) == 0 and (greater % y) == 0):
            lcm = greater
            break
        greater += 1
    return lcm


n1 = int(input("a : "))
n2 = int(input("b : "))
print(compute_lcm(n1, n2))
