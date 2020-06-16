count = 0
total = 0
average = 0
while True:
    num = input("Enter number:")
    try:
        f_num = float(num)
    except:
        if num == "done":
            print("Done")
            print(total, count, average)
            exit()
        else:
            print("Invalid input")
            continue

    count = count + 1
    total = total + f_num
    average = total / count
