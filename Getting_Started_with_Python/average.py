count = 0
total = 0
while True:
    num = input("Enter number:")
    if num == "done":
        print("Done")
        break
    try:
        f_num = float(num)
    except:
        print("Invalid input")
        continue
    count = count + 1
    total = total + f_num
print(total, count, total / count)
