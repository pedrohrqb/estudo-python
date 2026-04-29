from time import sleep

#Usando laço for para fazer uma contagem regressiva com intervalo de tempo de 1seg.
for cont in range(0, 11, 1):
    sleep(1)
    print(cont)
print('KABUM')