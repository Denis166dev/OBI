CI = int(input())
CA = int(input())
CE = int(input())

maior = max(CI,CA,CE)
menor = min(CI,CA,CE)

meio = (CI+CA+CE) - maior - menor

print(meio)