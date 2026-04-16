maior = 0
menor = 0

for n in range(0, 2):
    n1 = int(input('Digite seu ano de nascimento: '))
    if 2026 - n1 >= 18:
        maior += 1
    if 2026 - n1 <= 18:
        menor += 1
print(f'O total de pessoas maior de idade são {maior}.')
print(f'O total de pessoas menor de idade são {menor}.')
