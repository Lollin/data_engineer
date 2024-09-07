from datetime import datetime
import textwrap


def menu():
    menu = """
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair    
    => """

    return input(textwrap.dedent(menu))


def exibir_extrato(saldo, /, *, extrato, n_transacoes, limite):
    print("\n ==================== EXTRATO ==================== ")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==================================================")
    print(f"Restam apenas {limite - n_transacoes} transações diárias")


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += float(valor)
        extrato += (
            "\n"
            + f"Depósito:\tR$ {saldo:.2f} :: :: {datetime.now().strftime('%d/%m/%Y %H:%M')}"
        )
        print("\n=== Depósito realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limites_saques):

    excedeu_saque = numero_saques >= limites_saques
    excedeu_limite = valor > limite
    excedeu_saldo = valor > saldo
    registro_tempo = datetime.now().strftime("%d/%m/%Y %H:%M")

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saque:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= float(valor)
        extrato += "\n" + f"Saque:\t\tR$ {valor:.2f} :: ::{registro_tempo}"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")
    usuarios.append(
        {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
        }
    )

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    n_saques = 0
    n_transacoes = 0
    usuarios = []
    contas = []
    LIMITES_TRANSACOES = 10

    while True:

        opcao = menu()
        if n_transacoes < LIMITES_TRANSACOES:
            if opcao == "d":
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato)
                n_transacoes += 1

            elif opcao == "s":
                valor = float(input("Informe o valor do saque: "))

                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=n_saques,
                    limites_saques=LIMITE_SAQUES,
                )
                n_transacoes += 1


            elif opcao == "e":
                exibir_extrato(saldo, extrato=extrato, n_transacoes=n_transacoes, limite=LIMITES_TRANSACOES)

            elif opcao == "nu":
                criar_usuario(usuarios)

            elif opcao == "nc":
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                if conta:
                    contas.append(conta)

            elif opcao == "lc":
                listar_contas(contas)

            elif opcao == "q":
                break

            else:
                print(
                    "Operação inválida, por favor selecione novamente a operação desejada."
                )
        else:
            print("Você excedeu o limite de transações diárias permitidas")


main()
