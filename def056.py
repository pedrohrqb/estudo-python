
mulheres = 0
media = 0
cont = 0
maior_idade = 0
homem_velho = ''
for n in range(0, 4):
    nome = str(input(f'Digite o nome da {n+1}ª pessoa: '))
    idade = int(input(f'Digite a idade da {n+1}ª pessoa: '))
    sexo = str(input(f'Digite o sexo da {n+1}ª pessoa [M/F]: ')).upper()
    if sexo == 'F' and idade < 20:
        mulheres += 1
    
    if n == 1 and sexo == 'M':
        maior_idade = idade
        homem_velho = nome
    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        nomevelçho = nome
    

    cont += 1
    print('===============//================')


    media += idade

print(f'A média das idades é {media / cont:.1f}')
print(f'Ao todo são {mulheres} com menos de 20 anos')
print(f'{maior_idade}')