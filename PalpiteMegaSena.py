from random import randint
from time import sleep

jogo = list()
lista = list()
print('-=' * 30)
print('     JOGA NA MEGA SENA    ')
print('-=' * 30)
quant = int(input('Quantos jogos voçê quer sortear? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()  # Estou Ordenando os numeros da Lista
    jogo.append(lista[:])  # Estou Adicionando todos os numeros da lista ao jogo
    lista.clear()  # Estou limpando a lista gerada , para poder gerar outros numeros
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogo):  # Gerei um for para enumerar os jogos realizado e imprimir na tela.
    print(f'Jogo {i + 1}: {l}')
    sleep(1)  # Dei um Sleep para demorar 1 segundo para cada jogo
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
