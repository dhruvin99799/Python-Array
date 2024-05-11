from array import *

arr = array('i',[])
s=set(arr)
n = int(input("Enter Length Of Array : "))
for i in range(n):
    x = int(input("Enter the value : "))
    arr.append(x)

    print(arr)

val = int(input("Enter Value For Search : "))

k = 0

for e in arr:
    if e==val:
        print(k)
        break
    k+=1
        