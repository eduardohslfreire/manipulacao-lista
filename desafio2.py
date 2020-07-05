#!/usr/bin/python
#
# LuizaLabs - Desafio 2
# Autor: Eduardo Freire



# Importação
# de 
# bibliotecas
from os import system 



# Definição 
# de variavéis
# Globais
lista = []



# Definição
# de
# Funções

#Função para limpar console
clear = lambda: system('clear')


#Função para exibir menu principal
def exibe_menu():
    print("""****************************** Bem-vindo ao sistema de manipulação de lista. ******************************
    Escolha uma opção abaixo:

    1 - Listar
    2 - Inserir
    3 - Remover
    4 - Sair  
    """)


#Função para listar Lista
def listar():
    print("Lista = "+str(lista))
    

#Função para inserir elemento na Lista
def inserir():
    global lista

    print("\n\nDeseja inserir qual numero a Lista? ") 
    numero = input("Numero: ") 
    entrada_valida, mensagem = validaNumero(numero)
    
    while not entrada_valida:
        print("Numero invalido! "+mensagem)    

        numero = input("\n\nInforme um numero valido: ")
        entrada_valida, mensagem = validaNumero(numero) 

    lista.append(int(numero))
    print("Numero inserido com sucesso!")


#Função para remover elemento da Lista
def remover():
    global lista

    if len(lista) == 0:
        print("\n\nImpossivel remover numero! Lista esta vazia!")
    else:
        print("\n\nDeseja remover qual numero da Lista? ")
        numero = input("Numero: ")

        if ehInteiro(numero):
            num = int(numero)
            if num in lista:
                lista.remove(num)
                print("Numero removido com sucesso!")        
            else:
                print("Falha ao remover! Numero nao encontrado na Lista!")
        else:
            print("Falha ao remover! Numero nao eh valido!")

#Função para sair do menu
def sair():
    global lista
    del lista
    print("Saindo...")
    exit()


#Função para verificar se numero eh inteiro
def ehInteiro(numero):
    try:
        int(numero)
    except ValueError:
        return False
    else:
        return True


#Função para verificar se numero esta no range de 1 a 15000
def pertenceRange(numero):
    if numero >= 1 and numero <= 15000:
        return True
    else:
        return False


#Função para verificar se numero eh repetido
def ehRepetido(numero):
    if numero in lista:
        return True
    else:
        return False


#Função para verificar se numero eh primo
def ehPrimo(numero):
    for num in range(2, numero):
        if numero % num == 0:
            return False
    return True
     


#Função para validar as restrições de entrada
#numero eh inteiro
#numero esta fora do range de 1 a 15000
#numero eh repetido
#numero eh primo
def validaNumero(numero):
    if ehInteiro(numero):
        num = int(numero)
        if pertenceRange(num):
            if not ehRepetido(num):
                if not ehPrimo(num):
                    return (True, "")
                else:
                    return (False, "Numero eh Primo")
            else:
                return (False, "Numero eh repetido!")
        else:
            return (False, "Numero nao esta no range de 1 a 15.000!")
    else:
        return (False, "Numero nao eh inteiro!")


#Função principal
def menu_principal():
    while True:
        exibe_menu()
        opcao = input("Opção: ")
        if opcao == '1':
            listar()
        elif opcao == '2':
            inserir()
        elif opcao == '3':
            remover()
        elif opcao == '4':
            sair()
        else:
            print("Opção invalida! Favor inserir uma opcao correta!")
        
        input()
        clear()


#Função Inicial
menu_principal()