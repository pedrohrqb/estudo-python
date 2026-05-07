from random import randint
from time import sleep

cont = 0

while True:
    print('Seja bem vindo ao jogo de adivinhação')
    print('Máquina pensando em um número')
    for number in range(1, 4):
        print('Estou pensando em um número...')
        sleep(1)
    print('Ótimo..., pensei, tente adivinhar o número que eu pensei. ')

    num_maquina = randint(1, 3)
    num_jogador = int(input('Digite um número entre 1 a 10: '))

    if num_jogador == num_maquina:
        print('Parabéns, você conseguiu adivinhar o número escolhido')
        break
    if num_jogador != num_maquina:
        cont += 1
        print('Poxa, infelizmento não foi dessa vez, deseja tentar novamente?')
        print(f'O número escolhido foi {num_maquina}')
        print('Digite [S] para SIM ou Digite [N] para terminar a partida. ')
        regame = str(input('Deseja continuar a partida? [S/N] ')).strip().upper()
        
        if regame == 'N':
            print('Obrigado por jogar conosco, até logo.')
            break
print(f'O número de tentativas de acertos foi {cont}.')