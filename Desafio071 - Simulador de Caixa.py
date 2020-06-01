import time
print(f"\033[;1m{'Desafio 071 - Simular as celulas que irão sair':*^70}\033[m")
print('='*50)
print(f"{'Banco Eric':^50}")
print('='*50)
valor = int(input("Quanto deseja sacar? "))
ced = 100
total_ced = 0
print(f"Processando....")
time.sleep(2)

while True:
    if valor >= ced:
        valor -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f"O total de {total_ced} cédulas de {ced}")

        if ced == 100:
            ced = 50
            total_ced = 0
        elif ced == 50:
            ced = 20
            total_ced = 0
        elif ced == 20:
            ced = 10
            total_ced = 0
        elif ced == 10:
            ced = 5
            total_ced = 0
        elif ced == 5:
            ced = 2
            total_ced = 0
        elif ced == 2:
            print(f"Valor Retido: R${valor}")
            break
print('-'*50)