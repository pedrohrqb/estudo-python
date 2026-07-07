

lista = []
cont = 0
soma = 0
while True:
    num = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar [S/N] ?')).upper().strip()
    cont += 1
    soma += num

    if continuar == 'N':
        break
media = (soma / cont)

print(f'A soma de todos os valores é {soma}')
print(f'A média de todos os valores é {media}')

    