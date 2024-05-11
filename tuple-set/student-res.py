stu=dict()
n=int(input("Student Number = "))
for i in range(n):
    name=(input("Enter Students Name = "))
    marks=[]
    for i in range(5):
        mark = int(input("Enter Marks = "))
        marks.append(mark)
    stu[name] = marks
print("Dictionary Of Students Is = ",stu)

s_mark=sum(marks)
total=print("Total = ",s_mark)
min=print("Min = ",min(marks))
max=print("Max = ",max(marks))
per=s_mark/5
print("Per",per)

name = input("Enter Name Of Students ")
if name in stu.keys():
    print(stu[name])
else:
    print("No Student")