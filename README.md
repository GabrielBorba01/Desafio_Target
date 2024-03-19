# Desafio_Target

    Este repositório foi criado com a finalidade de mostrar minhas soluções 
    para os exercícios propostos pelo desafio target.

    Exercício 1:
    O valor da variável soma recebe 91.
    
    Exercício 2:
    
    print(f"Sequência Fibonacci:")
    resposta = int(input("Quantos digítos você deseja mostrar: "))
    d1 = 1
    d2 = 1
    d3 = 0
    temp = 0
    for i in range(2, resposta):
        if i == 2:
            print(f'{d1} {d2}', end='')
        else:
            d3 = d2 + d1
            print(f' {d3}', end='')
            temp = d2
            d2 = d3
            d1 = temp    

    Exercício 3:
    a) 9
    b) 128
    c) 49
    d) 100
    e) 13
    f) 200

    Exercício 4:

        Acenderia o 1° interruptor por alguns minutos e o 2° por um tempo maior. 
        Iria a primeira sala e tocaria na lampada para sentir a temperatura, 
        entraria na segunda sala e faria a mesma coisa.
        Com essas informações eu teria que a lampada com maior temperatura seria do interruptor 2, 
        a lampada menos quente seria do interruptor 1 e a lampada de menor temperatura seria do interruptor numero 3.
    
    Exercício 5: 

    palavra = str(input("Informe uma Palavra/Frase: "))
    comprimento = len(palavra)
    reverso = ''
    for i in range(comprimento - 1, -1, -1):
        print(f'{palavra[i]}',end='')

