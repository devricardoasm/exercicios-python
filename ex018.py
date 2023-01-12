from math import radians, sin, cos, tan
angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O seno de {} vale: {:.2f}'.format(angulo, seno))
print('O cosseno de {} vale: {:.2f}'.format(angulo, cosseno))
print('A tangente de {} vale: {:.2f}'.format(angulo, tangente))
