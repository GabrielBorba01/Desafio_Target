print(f"Sequência Fibonacci:")
resposta = int(input("Quantos digítos você deseja mostrar: "))
d1 = 1
d2 = 1
d3 = 0
temp = 0
for i in range(1, resposta):
    if i == 1:
        print(f'{d1} {d2}', end='')
    else:
        d3 = d2 + d1
        print(f' {d3}', end='')
        temp = d2
        d2 = d3
        d1 = temp
