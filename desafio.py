menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"+ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente para realizar a operação!")

        elif excedeu_limite:
            print("Limite insuficiente para realizar a operação!")

        elif excedeu_saques:
            print("Excedeu o limite de saque para realizar a operação!")

        elif valor > 0:
            saldo -= valor
            extrato += f"saques: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido!")

    elif opcao == "e":
        print("=============== EXTRATO ===============")
        print("Não foram realizadas movimentações!" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================")

    elif opcao == "q":
        break

    else:
        print("\nA opção selecionada não existe!\n")