a = int(input("Please enter the 1st integer: "))
b = int(input("Please enter the 2nd integer: "))

if a == 0 and b == 0:
    print("Both numbers are zero.")
elif a * b > 0:
    print("Both numbers have the same sign.")
else:
    print("The numbers have different signs.")
