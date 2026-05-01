
while True:
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()

    if sexo != 'M' or sexo != 'F':
        print('Você digitou um sexo inválido, digite novamente.')
    
    if sexo == 'M' or sexo == 'F':
        print(f'O sexo escolhido foi {sexo}')
        break