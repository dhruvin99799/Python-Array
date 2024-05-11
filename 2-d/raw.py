m=[]
row=0
r=[]


for i in range (3):
    a=[]
    for j in range(3):
        j=int(input("Enter Number : ["+str(i)+"] ["+str(j)+"] : "))
        a.append(j)
    m.append(a)
for i in range(3):
    for j in range(3):
        row=row+m[i][j]
    r.append(row)
    row=0
for i in range(3):
    for j in range(3):
        print(m[i][j],end="  ")
    print(r[i],end=" ")
    print()

