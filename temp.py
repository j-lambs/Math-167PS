import random as r

clist = [1,2,3,4,5]

print(r.sample(population=clist, k=2))

print(clist)

s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)

print(r.sample(population=list(s), k = 2)[0])
print(s)

print(r.randint(0,1))
