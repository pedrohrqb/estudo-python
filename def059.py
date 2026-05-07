n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

while True:
    print('''
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA

''')
    resposta = int(input('Qual opção acima deseja: '))
    
    if resposta == 1:
        soma = n1 + n2
        print(f'A soma dos valores de {n1} e {n2} é {soma}')
        
    if resposta == 2:
        mult = n1 * n2
        print(f'A multiplicação dos números {n1} e {n2} é {mult}')

    if resposta == 3:
        if n1 > n2:
            maior = n1
            print(f'O maior número entre {n1} e {n2} é {n1}')
        if n2 > n1:
            maior = n2
            print(f'O maior número entre {n1} e {n2} é {n2}')
    
    if resposta == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um número: '))
    
    if resposta == 5:
        print('Obrigado por participar do programa, até breve.')
        break
