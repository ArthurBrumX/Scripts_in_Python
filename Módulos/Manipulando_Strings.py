# Tratamento De Cadeia De Caractere

    # Fatiamento De Caracteres

    # Fatiamento Se Resume em pegar pedaços de uma determinada Frase.

    # Toda Contagem De Strings Sempre Começa com 0

    # -----------------------------------------------------------------------------------

    # Frase = Esta Chovendo Muito = 18 caracter

        # Exemplos De Fatiamento De Strings

            # Fatiamento : Frase [9] = (Vai mostras apenas o caracter 9)

                # Resposta: e
            
                # O primero Numero mostra Qual o valor alfabetico daquele espaço

            # Fatiamento: Frase[5:19] - Vai Mostras Apenas do espaço 9 até o 18

                # Resposta: Chovendo Muito

                # O primeiro Sempre Vai Ser Exato, Porém o Ultimo Será Um Pra Trás

                # O Ultimo é sempre Um a menos

            # Fatiamento: Frase[5:19:2] - Vai mostra apartir do espaço 5 e vai até o espaço 18 Pulando De 2 Em 2

                # Resposta: coed ut

                # O Primeiro Mostra Qual A partir de Qual Espaço ele ira mostrar

                # O segundo Vai Dizer ate onde ele vai contar (Sendo sempre um a menos)

                # O Terceirp Vai Dizer o quanto ele quer q pule

        # Analise De Frase

            # Comandos

                # len(frase)
             
                    # Vai mostra o Numero De Caracteres Que a Variavel Possui

                    # Resposta = 18 Caracters

                # frase.count('o')

                    # Solicita pro programa contar Quantas Vezes Apareceu a letra (o)

                    # Resposta = 2

                # frase.find('ndo')

                    # find = encontrar

                    # Solicita ao programa para dizer em que momento começou o 'ndo' que ele e encontrou no programa

                    # Resposta: 10, 11, 12

                # frase.find('android')

                    # Resposta: Retorna o valor -1 pois esse valor n existe dentro da variavel

                # 'chovendo' in frase - (nome da variavel)

                    # Resposta: True

                    # Dentro Da Variavel (frase) existe o conteudo (Chovendo)

        # Transformacao De Strings

            # frase.replace ('muito' , 'Pouco')

                # replace = trocar / reposicionar

                # Solicita Que troque a sting 'muito' por 'pouco'

            # frase.upper()

                # Transforma a string toda em maiuscula

                # Resposta: ESTA CHOVENDO MUITO

            # frase.lower()

                # Transforma a string toda para minuscula

            

