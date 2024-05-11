# WAP to get the array and display it in the reverse order

n = int(input("enter the n:"))
a = {}

for i in range(n):
    a[str(i)] = int(input("enter the value:"))

# for i in range(len(a)-1,-1,-1):
#     print(a[str(i)])

for key in range(len(a)-1,-1,-1):
    print(a[str(key)])
