cidade = str(input('Digite o nome da sua cidade: ')).strip()

ProcurarPalavra = 'SANTO' in cidade[:5].upper()

print('Sua cidade começa com o nome "Santo"?: ', ProcurarPalavra)
