quota = int(input())
N = int(input())
valor_atual = 0


for _ in range(N):
    valor_usado = int(input())
    valor_atual += quota - valor_usado
    
print(quota+valor_atual)