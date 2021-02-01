primeflag=True
n=int(input("Enter the no. to check prime or not : "))
for i in range(2,n):
    if n%i==0:
        primeflag=False
if primeflag:
    print(n,"is prime no.")
else:
    print(n,"is not a prime No.")
