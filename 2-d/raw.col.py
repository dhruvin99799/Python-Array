m=[]
row=0
r=[]
c=[]
col=0
s=0

for i in range (3):
    a=[]
    for j in range(3):
        j=int(input("Enter Number : ["+str(i)+"] ["+str(j)+"] : "))
        a.append(j)
    m.append(a)
for i in range(3):
    for j in range(3):
        row=row+m[i][j]
        col=col+m[j][i]
    r.append(row)
    c.append(col)
    s=s+row
    row=0
    col=0
c.append(s)
for i in range(3):
    for j in range(3):
        print(m[i][j],end="  ")
    print(r[i],end=" ")
    print()

for i in range(4):
    print(c[i],end=" ")
