import textwrap

# Menu principal
def menu():
    menu_text = """\n
    [d]    Depositar
    [s]    Sacar
    [e]    Extrato
    [u]    Criar Usuário
    [c]    Criar Conta
    [q]    Sair
=> """
    return input(textwrap.dedent(menu_text))

# Variáveis globais
usuarios = []
contas = []
numero_conta = 1
agencia = "0001"

# Funções
def sacar(saldo: float, valor: float, extrato: str, limite: float, numero_saques: int, limite_saques: int):
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato

    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    return saldo, extrato

def depositar(saldo: float, valor: float, extrato: str):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def visualizar_extrato(saldo: float, extrato: str):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(nome: str, data_nascimento: str, cpf: str, endereco: str):
    cpf = ''.join(filter(str.isdigit, cpf))  # Armazena apenas números
    if any(u['cpf'] == cpf for u in usuarios):
        print("Usuário já cadastrado com esse CPF.")
    else:
        usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
        print("Usuário criado com sucesso!")

def criar_conta(usuario):
    global numero_conta
    conta = {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'usuario': usuario
    }
    contas.append(conta)
    numero_conta += 1
    print(f"Conta criada com sucesso! Número da conta: {conta['numero_conta']}")

# Loop principal
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

    elif opcao == "e":
        visualizar_extrato(saldo, extrato)

    elif opcao == "u":
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        cpf = input("CPF: ")
        endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        criar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == "c":
        cpf = input("Informe o CPF do usuário: ")
        usuario = next((u for u in usuarios if u['cpf'] == ''.join(filter(str.isdigit, cpf))), None)
        if usuario:
            criar_conta(usuario)
        else:
            print("Usuário não encontrado.")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")