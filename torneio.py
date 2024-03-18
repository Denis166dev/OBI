V = 0
for _ in range(6):
    partida = input()
    if partida == 'V':
        V += 1
        
if V == 5 or V == 6:
    print(1)
elif V == 3 or V == 4:
    print(2)
elif V == 1 or V == 2:
    print(3)
else:
    print(-1)