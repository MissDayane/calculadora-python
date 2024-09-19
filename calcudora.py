
from operacoes import soma, subtracao, multiplicacao, divisao

def menu():
    print("Escolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

while True:
    menu()
    opcao = input("Digite o número da operação: ")

    if opcao in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == '1':
            print(f"Resultado: {soma(num1, num2)}")
        elif opcao == '2':
            print(f"Resultado: {subtracao(num1, num2)}")
        elif opcao == '3':
            print(f"Resultado: {multiplicacao(num1, num2)}")
        elif opcao == '4':
            print(f"Resultado: {divisao(num1, num2)}")
    else:
        print("Opção inválida. Tente novamente.")

    continuar = input("Deseja fazer outra operação? (s/n): ")
    if continuar.lower() != 's':
        break
