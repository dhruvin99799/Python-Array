m=[]
c=[]
col=0

for i in range (3):
    a=[]
    for j in range(3):
        j=int(input("Enter Number : ["+str(i)+"] ["+str(j)+"] : "))
        a.append(j)
    m.append(a)
for i in range(3):
    for j in range(3):
        col=col+m[j][i]
    c.append(col)
    col=0
for i in range(3):
    for j in range(3):
        print(m[i][j],end="  ")
    print()

for i in range(3):
    print(c[i],end=" ")
