info = input('Digite algo: ')
print('O tipo de primitivo dessa variável é: ', type(info))
print('Alfanumérico:', info.isalnum())
print('Alfabético: ', info.isalpha())
print('Dígito:', info.isdigit())
print('Totalmente em minúsculo:', info.islower())
print('Totalmente em maiúsculo:', info.isupper())
print('Número decimal:', info.isdecimal())
print('Numérico:', info.isnumeric())
print('Espaço: ', info.isspace())
print('Capitalizada (começa com letra maiúscula): ', info.istitle())

