#Detector de Palíndromo

frase = str(input(('Digite uma frase: '))).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''

for letra in range(len(juntar) -1, -1, -1):
    inverso += juntar[letra]

print(f'O inverso de {juntar} é {inverso}')

if inverso == juntar:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')


    # Outro modelo de detecção de palíndromo
frase2 = str(input('Digite uma frase: ')).strip().upper()
palavras2 = frase.split()
juntar2 = ''.join(palavras)
inverso2 = juntar[::-1]

print(f'O inverso de {juntar2} é {inverso2}')

if inverso == juntar:
    print('Temos um palíndromo')
else:
    print('A frase não é um palíndromo') 
