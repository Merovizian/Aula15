import random, time
print(f"\033[;1m{'Desafio 068 - Par ou Ímpar':*^70}\033[m")
vitorias = 0

while True:
    jogador = input("Escolha Par ou impar: ").strip().upper()
    while True:
        if jogador != 'PAR' and jogador != 'IMPAR':
            jogador = input("\033[1;31mEscolha Invalida!\033[m\nEscolha Par ou impar: ").strip().upper()
        else:
            break
    if jogador == 'PAR':
        print("O computador ficou com \033[1;33m IMPAR\033[m")
    else:
        print("O computador ficou com \033[1;33m PAR\033[m")
    jogador_numero = int(input("Escolha um número: "))
    print("\033[1;34mUm do la si e já... \033[m")
    time.sleep(1)
    print('-'*30)
    print(f"O Jogador escolheu: {jogador_numero}")
    computador_numero = random.randrange(0,11)
    print(f"O computador escolheu: {computador_numero}")
    print('-'*30)
    time.sleep(2)
    soma = computador_numero + jogador_numero
    resultado = soma
    if resultado % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print(f"A soma {jogador_numero} e {computador_numero} = {soma} é PAR" if resultado == 'PAR' else f"A soma {jogador_numero} e {computador_numero} = {soma} é IMPAR")
    if resultado == jogador:
        print("\033[1;32mO Jogador Venceu!\033[m")
        vitorias += 1
        print('-' * 30)
        time.sleep(2)
    else:
        print("\033[1;31mO Jogador Perdeu!")
        print('-' * 30)
        time.sleep(2)
        break

print(f"\033[1;33mGAME OVER! o Jogador venceu {vitorias} Vezes")
