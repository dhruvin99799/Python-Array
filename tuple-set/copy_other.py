#  WAP to get the array and copy it into the another array

n = int(input("enter the n:"))
a = {}
b = {}
for i in range(n):
    a[str(i)] = int(input("enter the value:"))

for i in range(len(a)):
    b[str(i)] = a[str(i)]

# print without index
# for i in range(len(b)):
#     print(b[str(i)])

# print with index
for i in b:
    print("a[",i,"]=",b[i])
    