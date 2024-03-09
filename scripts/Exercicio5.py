palavra = str(input("Informe uma Palavra/Frase: "))

comprimento = len(palavra)
reverso = ''
for i in range(comprimento - 1, -1, -1):
    print(f'{palavra[i]}',end='')