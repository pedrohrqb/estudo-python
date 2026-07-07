
soma = 0
while True:
    n = int(input('Digite um número: '))

    if n == 999:
        break
    soma += n

print(f'O valor total dos números digitados foram {soma}')

