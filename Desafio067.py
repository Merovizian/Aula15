print(f"\033[;1m{'Desafio 067 - Tabuada para o número desejado':*^70}\033[m")
while True:
    numero = int(input("Quer ver a tabuada de que numero: "))
    if numero < 0:
        break
    print('-'*20)
    for c in range (1,11):
        print(f"{numero:0>2} x {c:0>2} = {numero*c:0>2}")
    print('-'*20)

