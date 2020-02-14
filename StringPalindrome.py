my_str = input("Enter the string: ")

inpStr = my_str.casefold()

rev_str = reversed(inpStr)

print(rev_str)

if list(inpStr) == list(rev_str):
    print(f"{my_str} is a Palindrome.")
else:
    print(f"{my_str} is a Palindrome.")
