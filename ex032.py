ano = int(input('Digite o ano que deseja: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano escolhido é bisexto!')

else:
    print('O ano não é bisexto!')
print('Para mais informações, consulte o calendário.')
