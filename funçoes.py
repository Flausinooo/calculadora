#Funcoes
#para organizar o codigo
#para reaproveitamento
#primo pobre do microservico

#sintaxe
#def nome_funcao(parametros separados por virgula):
#   instruçoes
#   return expressao

#1o passo é a definicao da funcaoo
#2o passo é o uso dela
# print('Funções')
# print('\nFuncões simples')
# #1o passo
# def OlaMundo ():
#     print('Ola Mundo')
#
# #2o passo
# OlaMundo()
#
# #funcao com parametros
# #A gente define o parametro apenas dizendo o seu nome
# #Nao precissamos definir o tipo do parametro
# print('\nFunção com parametro e uso posicional')
# def Soma (p1, p2):
#     total = p1 + p2
#     print (total)
#
# Soma(5,6)
#
# print('\nFunção com parametro e uso nomeado')
# def Subtracao(p1, p2):
#     total = p1 - p2
#     print(total)
#     print('Posicional')
#     print('O total é:', end=' ')
# Subtracao(5, 6)
#
# print('Nomeado')
# print('O total é:', end=' ')
# Subtracao(p2=8, p1=5)
#
#
# def MostraClima():
#     print(f'O clima de hoje é de {clima}')
# clima = 'inverno'
# MostraClima()
#
# def MostraClima2():
#
#     print(f'O clima de hoje é de {clima2}')
# clima2 = 'verao'
# MostraClima2()

def MostraTemperatura():
    temperatura = 13
    print(f'A temperetura hoje é de {temperatura} graus C')

MostraTemperatura()

print('\nRetorno da Funcao')

def Soma2 (p1, p2):
    total = p1 + p2
    return total

n1 = 8
n2 = 9
print(f'A soma de {n1} e {n2} é {Soma2(n1, n2)}')

def Saudacao (nome):
    return 'Bom dia ' + nome + '!'

print(Saudacao('Gabriel'))