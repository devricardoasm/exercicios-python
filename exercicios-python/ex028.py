from random import choice
from time import sleep
print('---BEM-VINDO AO JOGO DA ADIVINHAÇÃO NUMÉRICA!---')
NumeroDigitado = int(input('Digite um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(1)
ListaNumeros = [0,1,2,3,4,5]
NumeroEscolhido = choice(ListaNumeros)


if NumeroDigitado == NumeroEscolhido:
    print('PARABÉNS! Você acertou o número escolhido pelo sistema.')
else:
    print('Que pena, tente novamente!')
print('O numero sorteado foi: {}'.format(NumeroEscolhido))

