def calcular():
    while True:
        # Recebendo entrada do usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Exibindo opções de operação
        print("\nEscolha a operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        # Recebendo a escolha do usuário
        opcao = input("Digite o número da operação desejada: ")

        # Realizando as operações
        if opcao == '1':
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif opcao == '2':
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif opcao == '3':
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif opcao == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        elif opcao == '5':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

        print("\n" + "-"*30 + "\n")  # Separação visual

# Chamando a função
calcular()
