nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em letras maiúsculas: ', nome.upper())
print('Seu nome em letras minúsculas', nome.lower())

NomeQtdeLetras = nome.replace(' ', '')
print('Quantidade de letras (sem espaço): ', len(NomeQtdeLetras))

PrimeiroNomeFatiado = nome.split()
print('O número de letras do seu primeiro nome é: ', len(PrimeiroNomeFatiado[0]))
