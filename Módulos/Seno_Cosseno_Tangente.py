# Scripts Que lê Um Ângulo Qualquer e Mostre Na Tela o Valor Do Seno, Cosseno e Tangente Desse Angulo.

import math
# Importando a biblioteca math (matematica)

angulo = float(input("Digite o Ângulo Que Você Deseja: "))
    # Vartiavel = angulo
        # Mensagem = Digite o Angulo Que Voce Deseja:

seno = math.sin(math.radians(angulo))

print ("O dÂngulo de {} Tem o SENO de {}".format(angulo, seno))

cosseno = math.cos(math.radians(angulo))

print ("O ângulo De {} tem o COSSENO de {}".format(angulo, cosseno))

tangente = math.tan(math.radians(angulo))

print ("O angulo de {} tem a Tangente de {}".format(angulo, tangente))
