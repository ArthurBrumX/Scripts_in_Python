# Scripts Que lê Um Ângulo Qualquer e Mostre Na Tela o Valor Do Seno, Cosseno e Tangente Desse Angulo.

import math

angulo = float(input("Digite o Ângulo Que Você Deseja: "))

seno = math.sin(math.radians(angulo))

print ("O Ângulo de {} Tem o SENO de {}".format(angulo, seno))

cosseno = math.cos(math.radians(angulo))

print ("O ângulo De {} tem o COSSENO de {}")
