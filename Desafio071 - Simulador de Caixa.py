import time
print(f"\033[;1m{'Desafio 071 - Simular as celulas que irão sair':*^70}\033[m")
print('='*50)
print(f"{'Banco Eric':^50}")
print('='*50)
valor = int(input("Quanto deseja sacar? "))
celula_50 = valor // 50
celula_20 = (valor % 50) // 20
celula_10 = ((valor % 50) % 20) // 10
celula_1 = (((valor % 50) % 20 ) % 10) // 1
print(f"Processando....")
time.sleep(2)

if celula_50 > 0:
    print(f"Total de {celula_50} células de R$50")
if celula_20 > 0:
    print(f"Total de {celula_20} células de R$20")
if celula_10 > 0:
    print(f"Total de {celula_10} células de R$10")
if celula_1 > 0:
    print(f"Total de {celula_1} células de R$1")
print('-'*50)
