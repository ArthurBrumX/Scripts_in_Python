caneta = "tampada"

class caneta:
    def __init__(self, cor, tamanho):
        self.cor = cor
        self.tamanho = tamanho

    def tapada(self):
        if caneta == "tampada":
            print("A caneta esta Tampada")

    def destamparCaneta(self):
        if caneta == "destampada":
            print("A caneta esta Destampada")

caneta1 = caneta("preta","5cm")
print(caneta1)