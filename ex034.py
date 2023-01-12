salario = float(input('Digite o seu salário: '))

if salario > 1250:
    NovoSalario = salario * 1.1
    print('Seu novo salário é de {:.2f} reais' .format(NovoSalario))
else:
    NovoSalario = salario * 1.15
    print('Seu novo salário é de {:.2f} reais' .format(NovoSalario))
print('PARABÉNS!!!')
