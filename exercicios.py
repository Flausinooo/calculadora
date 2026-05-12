#Exercicio1
n1 = float(input("Digite a primeira Nota: "))
n2 = float(input("Digite a segunda Nota: "))
def verificarAprovacao(nota1, nota2):
    media =(nota1 + nota2) /2

    if media >= 6:
        return "Você foi aprovado!"
    else:
        return "Você foi reprovado!"


    print(verificarAprovacao(n1, n2))