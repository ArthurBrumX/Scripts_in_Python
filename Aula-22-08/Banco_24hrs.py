print("=" * 60)
print("(1) - Entrar Na Minha Conta Bancaria")
print("(2) - Criar Uma Conta pessoa Fisica")
print("(3) - Criar Uma Conta Pessoa Juridica")
print("=" * 60)

user = ['123','456','789']
senha = ['123','456','789']

user_Joao = 123
user_Maria = 456
user_Rodrigo = 789

questionamento = int(input("Oque Voce Deseja Fazer: "))

if questionamento == 1:
    verificacao_user = int(input("Digite o Numero da conta: "))
    verificacao_senha = int(input("Digite A senha Da conta: "))

    if verificacao_user == 123 and verificacao_senha == 123:
        print("=" * 60)
        print("Bem-Vindo João!!!")
        print("Conta Acessada Com Sucesso!!") 
        print("(1) - Depositar")
        print("(2) - Sacar")
        print("(3) - Retirar Extrato")
        verificacao_procedi = int(input("Digite o Numero da Operação Desejada: "))        
        print("=" * 60)

        if verificacao_procedi == 1:
            print("Voce Escolheu Depositar!")
            veirificacao_deposito = int(input("Digite O VaLor Que Deseja Depositar: R$"))

    else:
        print("Dados Invalidos (Falha Ao Acessar conta)")

