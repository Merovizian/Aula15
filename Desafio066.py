print(f"\033[;1m{'Desafio 066 - Soma de vários números':*^70}\033[m")
soma = contador = 0
while True:
    numero = int(input("Digite um número: "))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f"Foram digitados {contador} números e a soma deles é {soma}")