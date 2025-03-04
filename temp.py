res = {'Xwin': 0, 'Owin': 1}
print(res)

d = {(1,2): res}

print(d)

# {(move1, move2) -> {'Xwin'->n, 'Owin'->m}}
def updateWin(map: dict, letter: str, moveCombination: tuple):
    result_dict = map.get(moveCombination)
    result_dict.update({letter: result_dict.get(f'{letter}win') + 1})

updateWin(d, 'X', (1,2))
print(d)

y = 0
my = f'{y}hello'
print(my)

print(len(d))

d2 = dict()
print(len(d2))

print(d.get((1,2)).get('Owin'))

for i in range(1, 10):
    print(i)

