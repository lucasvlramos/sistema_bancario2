def saque(saldo, extrato_lista, qtd_saques, saque_excedidos, limite_saques, limite):
    if not saque_excedidos:
        if qtd_saques < limite_saques:
            valor = float(input("Informe o valor de saque: "))
            if valor > limite:
                print("Limite de saque excedido.")
            elif valor <= saldo:
                saldo -= valor
                qtd_saques += 1
                extrato_lista.append(("Saque", valor))
                print("Saque realizado:", valor, 
                      "Saldo atualizado:", saldo,
                      "Quantidade de saques disponíveis:", limite_saques - qtd_saques)
                if qtd_saques == limite_saques:
                    saque_excedidos = True
            else:
                print("Saldo insuficiente.")
        else:
            print("Limite de saques atingido")
    else:
        print("Limite atingido, sem saques por hoje.")
    return saldo, extrato_lista, qtd_saques, saque_excedidos

def deposito(saldo):
    valor = float(input("Informe o valor a ser depositado: "))
    saldo += valor
    print("Depósito realizado:", valor, 
          "Saldo atualizado:", saldo)
    return saldo

def mostrar_extrato(saldo, extrato_lista):
    print("===== Extrato =====")
    for transacao in extrato_lista:
        print(transacao[0] + ":", transacao[1])
    print("Saldo atual:", saldo)

def cadastrar_usuario(lista_usuarios, lista_contas):
    nome = str(input("Digite o nome do usuário: "))
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite o CPF (apenas números): ")
    endereco = input("Digite o endereço (logradouro, bairro, cidade/estado): ")

    for usuario in lista_usuarios:
        if usuario["CPF"] == cpf:
            print("Erro: Já existe um usuário com este CPF na lista.")
        return

    novo_usuario = {
        "Nome": nome,
        "Data de Nascimento": data_nascimento,
        "CPF": cpf,
        "Endereço": endereco,
        "Contas": []  # Inicializa uma lista de contas vazia para o usuário
    }
    lista_usuarios.append(novo_usuario)
    
    # Adiciona automaticamente uma nova conta ao usuário
    numero_conta = len(lista_contas) + 1
    agencia = "0001"  # Agência fixa
    nova_conta = {
        "Agência": agencia,
        "Número da Conta": numero_conta,
        "Usuário": novo_usuario
    }
    lista_contas.append(nova_conta)
    
    print("Usuário cadastrado com sucesso.")
    return lista_usuarios, lista_contas

def buscar_usuario_por_cpf(lista_usuarios, lista_contas):
    cpf = input("Digite o CPF do usuário que deseja buscar: ")

    print("Lista de Usuários:", lista_usuarios)  # Verifica a lista de usuários

    for usuario in lista_usuarios:
        print("CPF do usuário:", usuario["CPF"])  # Verifica o CPF de cada usuário
        if usuario["CPF"] == cpf.strip():  # Remove espaços em branco extras
            print("Nome do usuário:", usuario["Nome"])
            for conta in lista_contas:
                if conta["Usuário"] == usuario:
                    print("Agência:", conta["Agência"])
                    print("Número da Conta:", conta["Número da Conta"])
            return

    print("Usuário com CPF", cpf, "não encontrado.")



lista_usuarios=[]
lista_contas=[]
extrato_lista = []
saldo = 0
criar_conta = []
limite = 500
limite_saques = 3
qtd_saques = 0
saque_excedidos = False

menu = """
= Seja Bem vindo =

[1] Sacar
[2] Depositar
[3] Extrato
[4] Criar conta
[5] Procurar conta
[6] Lista
[0] Sair

======= VB =======
"""

while True:
    opcao = int(input(menu))

    if opcao == 1:
        saldo, extrato_lista, qtd_saques, saque_excedidos = saque(saldo, extrato_lista, qtd_saques, saque_excedidos, limite_saques, limite)
    elif opcao == 2:
        saldo = deposito(saldo)
    elif opcao == 3:
        mostrar_extrato(saldo, extrato_lista)
    if opcao == 4:
        lista_usuarios, lista_contas = cadastrar_usuario(lista_usuarios, lista_contas)
    elif opcao == 5:
        buscar_usuario_por_cpf(lista_usuarios, lista_contas)
    elif opcao == 0:
        print("Obrigado por utilizar nosso sistema...")
        break
    else:
        print("Opção inválida")
        


