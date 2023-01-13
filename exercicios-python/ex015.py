dias = int(input('Insira por quantos dias o carro foi alugado: '))
quilometragem = float(input('Insira a quantidade de quilômetros percorridos com o carro: '))

custototal = (quilometragem*0.15) + (dias*60.00)

print('O custo total foi de: {:.2f} reais'.format(custototal))
