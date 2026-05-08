
while True:
    result = 1
    num = int(input('Digite um número para saber seu fatorial: '))

    n = num
    while n >= 1:
        if n > 1:
            print(f'{n}x', end='')
        else:
            print(f'{n}', end='')

        result *= n
        n -= 1

    print(f'= {result}')

   
    reload = str(input('Deseja continuar? [S/N]')).upper().strip()
    
    if reload == 'S':
        continue
    if reload == 'N':
        print('Obrigado por participar, até breve')
        break
    
    