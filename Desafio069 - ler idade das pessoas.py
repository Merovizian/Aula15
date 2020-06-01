import idade
print(f"\033[;1m{'Desafio 069 - Separar pessoas por idade e sexo':*^70}\033[m")
quantidade_feminino = quantidade_masculino = quantidade_18 = 0


while True:
    print('-'*50)

    sexo = input("Infome o sexo da pessoa: ").upper()[0]
    while sexo not in 'FM':
        print("\033[1;31mInforme um sexo correto!\033[m")
        sexo = input("Infome o sexo da pessoa: ").upper()[0]

    nascimento = input("Informe a data de nascimento[dd/mm/aaa]: ")
    while idade.ano(nascimento) == -1:
        nascimento = input("Informe a data de nascimento[dd/mm/aaa]: ")

    if idade.ano(nascimento) != -1:
        if idade.ano(nascimento) > 18 and (sexo in 'FM'):
            quantidade_18 += 1
        if sexo == 'M':
            quantidade_masculino += 1
        if sexo == 'F' and idade.ano(nascimento) < 20:
            quantidade_feminino += 1
    print('-'*50)

    escolha = input(("Deseja continuar? [S/N]: ")).upper()[0]
    while escolha not in 'NS':
        print("\033[1;31mInforme um sexo correto!\033[m")
        escolha = input(("Deseja continuar? [S/N]: ")).upper()[0]
    if escolha == 'N':
        break

print('-'*50)
print(f'''Existem {quantidade_18} pessoas com mais de 18 anos.
Existem {quantidade_masculino} Homens.
Existem {quantidade_feminino} Mulheres com menos de 20 anos.
''')
print('-'*50)
