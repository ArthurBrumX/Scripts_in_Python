# Script Que Lê o Nome Completo De Uma Pesssoa e Mostre:

    # O Nome Com Todas As Letras Maiusculas.

    # O Nome Com Todas As Letras Minusculas.

    # Quanstas Letras Ao Todo Sem Considerar Espaços.

    # Quantas Letras Tem o Primeiro Nome.

nome = input("Qual é o Seu Nome Completo: ")

print ("Seu Nome Em Maiusculo é {}".format(nome.upper()))

    # (nome Da Variavel).upper Deixa todo o conteudo da variavel em maiusculo

print ("Seu Nome Em Minusculo é {}".format(nome.lower()))

    # (Nome Da Variavel).lower Deixa todo o conteudo da variavel em minusculo.

nome_1 = nome.split()

juncao = ''.join(nome)

print ("Seu Nome tem {} letras".format(len(juncao))) 

    # Sem Contar Espaços.

print ("Seu primeiro nome tem {} letras".format(len(nome_1)))

