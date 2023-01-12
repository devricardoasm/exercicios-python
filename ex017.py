from math import hypot
catetoadj = float(input('Digite o cateto adjacente: '))
catetooposto = float(input('Digite o cateto oposto: '))

hip = hypot(catetoadj, catetooposto)

print('A hipotenusa é: {:.2f}'.format(hip))



#from math import (pow, sqrt)
#catetooposto = float(input('Digite o valor do cateto oposto: '))
#catetoadjacente = float(input('Digite o valor do cateto adjacente: '))

#hipotenusa = sqrt((pow(catetooposto, 2)) + (pow(catetoadjacente, 2)))

#print('O valor da hipotenusa é: {}'.format(hipotenusa))

