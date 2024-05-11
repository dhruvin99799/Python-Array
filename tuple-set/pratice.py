n = dict(name="Dhruvin", email="Dhruvin@gmail.com",country="India")
print(n)

z = {
    "name":"Raj",
    "email":"Raj@gmail.com",
    "country":"India"
}
print(z)
print(z["Email"])

sub = {}
for i in range(5):
    sub[str(i)] = input("enter the sub"+str(i)+":")

print(sub)