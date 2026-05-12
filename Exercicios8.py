# EXERCÍCIO 8

def menu():
    print("\nCalculadora:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = int(input("Selecione sua opção: "))

    return opcao


def adicao(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por zero."

    else:
        return a / b


opcao = 0

while opcao != 5:

    opcao = menu()

    if opcao >= 1 and opcao <= 4:

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == 1:
            print("Resultado:", adicao(num1, num2))

        elif opcao == 2:
            print("Resultado:", subtracao(num1, num2))

        elif opcao == 3:
            print("Resultado:", multiplicacao(num1, num2))

        elif opcao == 4:
            print("Resultado:", divisao(num1, num2))

    elif opcao == 5:
        print("Programa encerrado.")

    else:
        print("Opção inválida!")



