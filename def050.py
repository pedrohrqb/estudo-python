s = 0

for n in range(0, 6):
    a = int(input(('Digite um número: ')))
    if a % 2 == 0:
        s += a
print(f'Os valores somados dos números pares foram {s}')    