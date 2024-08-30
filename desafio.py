def extrato_bancario():
    print(extrato)


def depositar():
    while True:
        valor = input("Qual valor será depositado: ")

        if valor.isdigit() and float(valor) >= 0:
            global extrato
            global saldo
            valor = float(valor)
            extrato += "\n" + f"Depósito realizado de: R$ {valor:.2f}"
            saldo += float(valor)
            extrato += "\n" + f"Novo saldo de: R$ {saldo}"

            break

        else:
            voltar = input(
                """
            O valor deve ser positivo caso tenha escolhido a opção incorreta,
            digite [v] para voltar,
            caso contrário digite outra letra para efetuar um depósito => """
            )
            if voltar == "v":
                break
            else:
                continue


def sacar():
    global n_saques
    if n_saques < LIMITE_SAQUES:
        while True:
            valor = input("Qual valor será sacado (limite máximo por saque R$ 500): ")

            if valor.isdigit() and float(valor) >= 0:
                global extrato
                global saldo
                valor = float(valor)
                if saldo >= valor:
                    if valor <= 500:
                        extrato += "\n" + f"Saque realizado de: R$ {valor:.2f}"
                        saldo -= float(valor)
                        extrato += "\n" + f"Novo saldo de: R$ {saldo:.2f}"

                    break
                else:
                    print("Não é possível efetuar o saque, não há saldo suficiente")
                    break

            else:
                voltar = input(
                    """
                O valor deve ser positivo caso tenha escolhido a opção incorreta,
                digite [v] para voltar,
                caso contrário digite outra letra para efetuar um saque => """
                )
                if voltar == "v":
                    break
                else:
                    continue


if __name__ == "__main__":
    menu = """ 

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    saldo = 0
    limite = 500
    extrato = ""
    n_saques = 0
    LIMITE_SAQUES = 3

    while True:

        opcao = input(menu)

        if opcao == "d":
            depositar()

        elif opcao == "s":
            sacar()

        elif opcao == "e":
            extrato_bancario()

        elif opcao == "q":
            break

        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )
