quilometro = int(input('Digite quantos quilômetros de distância até o destino: '))

if quilometro <=200:
    PrecoDaPassagem = quilometro * 0.5
else:
    PrecoDaPassagem = quilometro * 0.45

print('O valor da sua passagem ficou em: {:.2f} reais' .format(PrecoDaPassagem))
print('BOA VIAGEM!!!')
