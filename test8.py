a = [1,3,5,9,8,5,6,7,4]

if 5 in a:
    print("yes")
else:
    print("no")
a = [2,2,3,5,5,5,7,7,8,14]
b=[]
for j in a:
    if j not in b:
        b.append(j)
print(b)