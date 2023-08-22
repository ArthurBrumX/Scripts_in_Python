livros = int(input("Quantos livros voce comprou nesse semestre: "))

if livros == 0:
    print("Total De Pontos: 0")
elif livros == 1:
    print("Total De Pontos: 5")
elif livros == 2:
    print("Total De Pontos: 15")
elif livros == 3:
    print("Total De Pontos: 30")
elif livros >= 4:
    print("Total De Pontos: 60")