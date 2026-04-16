
s = 0
for n in range(1, 500):
    if n % 3 == 0:
        if n % 2 == 1:
            s += n
            print(f'{n} ' , end='')
print(f'\nO total é {s}')
