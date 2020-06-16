# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and
# put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
while True:
    s_num = input("Enter an integer: ")
    if s_num == "done":
        break
    try:
        f_num = float(s_num)
    except:
        print("Invalid input")
        continue
    try:
        if f_num != int(f_num):
            raise Exception()
    except:
        print("Enter an integer and not a decimal")

    if largest is None or largest < f_num:
        largest = int(f_num)
    if smallest is None or smallest > f_num:
        smallest = int(f_num)

print("Maximum is", largest)
print("Minimum is", smallest)

# isinstance(i, float)
