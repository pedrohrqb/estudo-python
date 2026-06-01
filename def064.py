
cont = 0
soma = 0


while True:
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if num == 999:
        print('O programa encerrou, pois foi digitado o número "999".')
        soma -= 999
        cont -= 1
        break

print(f'O total de número digitas foram: {cont}')
print(f'A soma de todos os números digitados foram {soma}')