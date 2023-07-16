menu = '''\t *** MENU ***
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
    
Selecione a opção desejada: '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input('Informe o valor do depósito: R$ '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Operação inválida! Valor informado não é válido.\n')

    elif opcao == 2:
        valor = float(input('Informe o valor do saque: R$ '))
        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saques_excedido = numero_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print('Operação inválida! Saldo insuficiente.\n')
        elif limite_excedido:
            print('Operação inválida! Valor do saque excede o limite.\n')
        elif saques_excedido:
            print('Operação inválida! Você já realizou o número máximo de saques permitido.\n')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            print(f'Realizado saque no valor de R$ {valor:.2f}')
        else:
            print('Operação inválida! Valor informado não é válido.\n')

    elif opcao == 3:
        print('______ EXTRATO ______')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('_____________________\n')

    elif opcao == 0:
        break

    else:
        print('Opção inválida!\n')


