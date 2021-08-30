sum=0
while True:
    number=input("Enter the number: ")
    if number=="Stop":
        print("{:.3f}".format(sum))
        break
    else:
        try:
            number = float(number)
        except ValueError:
            print("Incorrect number!")
            continue
        else:
            sum+=number