Comp1 = int(input('Digite o primeiro comprimento: '))
Comp2 = int(input('Digite o segundo comprimento: '))
Comp3 = int(input('Digite o terceiro comprimento: '))

if Comp1 + Comp2 > Comp3 and Comp1 + Comp3 > Comp2 and Comp2 + Comp3 > Comp1:
    print('Essas retas formam um triângulo!')
else:
    print('Essas retas NÃO formam um triângulo!')

