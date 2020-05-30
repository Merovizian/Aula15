import idade
print(f"\033[;1m{'Desafio 069 - Separar pessoas por idade e sexo':*^70}\033[m")
escolha = 'S'
feminino = ('FEMININO', 'F')
masculino = ('MASCULINO', 'M')
quantidade_feminino = quantidade_masculino = quantidade_18 = 0


while escolha == 'S':
    print('-'*50)
    sexo = input("Infome o sexo da pessoa: ").upper()
    nascimento = input("Informe a data de nascimento[dd/mm/aaa]: ")

    if idade.ano(nascimento) != -1:
        if idade.ano(nascimento) > 18 and (sexo in feminino or sexo in masculino):
            quantidade_18 += 1
        if sexo in masculino:
            quantidade_masculino += 1
        if sexo in feminino and idade.ano(nascimento) < 20:
            quantidade_feminino += 1
    print('-'*50)

    escolha = input (("Deseja continuar? [S/N]: ")).upper()

print('-'*50)
print(f'''Existem {quantidade_18} pessoas com mais de 18 anos.
Existem {quantidade_masculino} Homens.
Existem {quantidade_feminino} Mulheres com menos de 20 anos.
''')
print('-'*50)


