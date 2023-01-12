frase = str(input('Digite uma frase qualquer: ')).strip()


print('A letra "a" aparece {} vez(es)' .format(frase.upper().count('A')))
print('A letra "a" aparece, primeiramente, na posição: ', frase.upper().find('A')+1)
print('A letra "a" aparece, por último, na posição: ', frase.upper().rfind('A')+1)


