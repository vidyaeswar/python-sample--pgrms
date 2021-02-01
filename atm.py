import sys 
lst= sys.argv
for i in lst:print(i)
accbal=100000
inp = int(input("\nEnter Option:"))
print(1,'balance \n')
print(2, "withdraw \n")
print(3,"depostie \n")
print(4,"deposite cheque \n")
print(5,"invalid\n")
if(inp==1):
    print("balance amount is:",accbal)
elif(inp==2):
    rs=int(input("enter the amount for widthdraw!!"))
    if rs>accbal:
        print("please check your balance")
    elif rs < accbal:
        print("remaining balanceis:",accbal)
elif(inp==3):
	cash=int(input("please enter the cash amount:"))
	accbal=accbal+cash
	print("balance is:",accbal)
elif(inp==4):
	chq=int(input("please enter cheque amount:"))
	accbal=accbal+chq
	print("balance is:",accbal)
else:print("invalid option")