j = (1,2,3)
j = list(j)
j[0] = 0
j = tuple(j)
print(j)

d = dict()
d.update({j: [100,100]})
print(d)

sec = d.get(j)
d.update({})


