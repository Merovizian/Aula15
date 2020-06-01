print(f"\033[;1m{'Desafio 070 - Comprar produtos diversos':*^70}\033[m")
total = maior_mil = produto_menor = 0
produto_nome = ''
while True:
    produto = input("Informe o nome do produto: ")
    preco = (input(f"Informe o valor de {produto}: "))
    preco = float(preco.replace(',','.'))

    if total == 0 or preco < produto_menor:
        produto_menor = preco
        produto_nome = produto

    if preco > 1000:
        maior_mil += 1
    total += preco

    continuar = input("Deseja continuar[S/N]: ").upper()[0]
    while continuar not in 'NS':
        continuar = input("Deseja continuar[S/N]: ").upper()[0]
    if continuar == 'N':
        break


print(f'''O total gasto foi de R$ {total:.2f}.
Foram comprados {maior_mil} produtos acima de R$ 1000.
O produto mais barato é {produto_nome} que custa {produto_menor}.
''')



