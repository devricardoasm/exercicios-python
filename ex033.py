PrimeiroNumero = int(input('Digite o primeiro número: '))
SegundoNumero = int(input('Digite o segundo número: '))
TerceiroNumero = int(input('Digite o terceiro número: '))

if PrimeiroNumero > SegundoNumero and PrimeiroNumero > TerceiroNumero:
    print('{} é o maior número!' .format(PrimeiroNumero))
elif SegundoNumero > TerceiroNumero:
    print('{} é o maior número!' .format(SegundoNumero))
else:
    print('{} é o maior número!' .format(TerceiroNumero))


if PrimeiroNumero < SegundoNumero and PrimeiroNumero < TerceiroNumero:
    print('{} é o menor número!' .format(PrimeiroNumero))

elif SegundoNumero < TerceiroNumero:
    print('{} é o menor número!' .format(SegundoNumero))
else:
    print('{} é o menor número!' .format(TerceiroNumero))
