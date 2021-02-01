import sys
lst = sys.argv
for i in lst:print(i)
accbal = 10000
inp = int(input("\nEnter Option:"))
if (inp == 1):
    print("Balance Amount is:", accbal)
elif (inp == 2):
    rs = int(input("Enter Amount for Withdrawal:"))
    if rs > accbal:
        print("Please check Balance Amount!!!")
    elif rs < accbal:
        accbal = accbal - rs
        print("Remaining Balance is:", accbal)
elif (inp == 3):
    cash = int(input("Please Enter Cash Amount:"))
    accbal = accbal + cash
    print("Balance is:", accbal)
elif (inp == 4):
    chq = int(input("Please Enter Cheque Amount:"))   
    accbal = accbal + chq
    print("Balance is:", accbal)
else:print("Invalid Option!!!")

