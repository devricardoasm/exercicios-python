quilometragem = float(input('Qual a velocidade atual do carro? '))

if quilometragem <=80:
    print('Você é um bom condutor.')
else:
    multa = float(quilometragem - 80)*7
    print('O valor da sua multa é de: {:.2f} reais' .format(multa))
print('Dirija com responsabilidade!')
