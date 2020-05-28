soma = contador = 0

while True:
    numero = int(input("Digite um valor: "))
    if numero == 999:
        break
    soma += numero
    contador += 1

print(f"Os {contador} números digitados deram soma de {soma} ")