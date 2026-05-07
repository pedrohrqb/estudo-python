#fatorial de um número com FOR e com While (não sei, maas vou tentar)


num = int(input('Digite um número para saber seu fatorial: '))
print(f'O fatorial de {num}! é: ')

resultado = 1
for n in range(num, 0, -1):
        if n > 1:
            print(f'{n}x', end='')
        else:
            print(f'{n}', end='')
        
        resultado *= n 

print(f'= {resultado}')