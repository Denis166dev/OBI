N = int(input())
lista = []

for _ in range(N):
    E,A,G = input().split(' ')

    if float(A) <= float(G)*0.7:
        lista += [E]

if len(lista) == 0:
    print('*')
else:
    for i in range(len(lista)):
        print(lista[i])