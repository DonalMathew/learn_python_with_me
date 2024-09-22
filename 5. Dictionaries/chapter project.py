list=["Chris","Annie","Beej","Aaron","Charlie"]

d={}

while list:
    x=list[0][0]
    d[x]=[list[0]]
    list.pop(0)

    for j in range(len(list)):
        y=list[j][0]
        if y==x:
            d[x].append(list[j])
            list.pop(j)

print(d)
