

while True:
    tab = int(input('Deseja ver a tabuada de qual valor? '))

    if tab <= -1:
        print('PROGRAMA TABUADA ENCERRADO.')
        break

    for n in range(1, 11):
        print(f'{tab} x {n} = {tab*n}')
    