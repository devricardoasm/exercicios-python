from random import shuffle

aluno1 = input('Digite o primeiro aluno: ')
aluno2 = input('Digite o segundo aluno: ')
aluno3 = input('Digite o terceiro aluno: ')
aluno4 = input('Digite o quarto aluno: ')

ordem = [aluno1, aluno2, aluno3, aluno4]
shuffle(ordem)
print('A ordem definida para apresentação de trabalhos é: {}'.format(ordem))
