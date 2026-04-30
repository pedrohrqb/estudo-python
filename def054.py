from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0

for p in range(1,3):
    nasc = int(input(f'Em que ano a {p}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print(f'Ao todo tivemos {totmaior} pessoa(s) maiores de idade.')
print(f'Ao todo tivemos {totmenor} pessoa(s) menores de idade.')