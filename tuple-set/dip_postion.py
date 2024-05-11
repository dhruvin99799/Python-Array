n = int(input("enter the n:"))
a = {}

for i in range(n):
    a[str(i)] = int(input("enter the value"+str(i)+":"))

for i in a:
    print("a[",i,"]=",a[i])
    