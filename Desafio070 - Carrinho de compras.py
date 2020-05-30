print(f"\033[;1m{'Desafio 070 - Comprar produtos diversos':*^70}\033[m")
total = maior_mil = 0
continuar = 'S'


while continuar == 'S':
    produto = input("Informe o nome do produto: ")
    preco = float(input(f"Informe o valor de {produto}: "))

    if total == 0:
        produto_menor = preco
        produto_nome = produto
    if preco < produto_menor:
        produto_menor = preco
        produto_nome = produto
    if preco > 1000:
        maior_mil += 1
    total += preco

    continuar = input("Deseja continuar[S/N]: ").upper()

print(f'''O total gasto foi de R$ {total}.
Foram comprados {maior_mil} produtos acima de R$ 1000.
O produto mais barato é {produto_nome}.
''')



