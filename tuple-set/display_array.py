n = int(input("enter the n:"))
a = {}
for i in range(n):
    a[str(i)] = int(input("enter the value:"))

for i in range(len(a)):
    print(a[str(i)])