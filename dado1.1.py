  
from random import randint
import sys



def inicio():
        print("BEM-VINDO(A) AO SIMULADOR DE DADO\n")
        print('''[1] INICIAR ''''[2] SAIR \n''')
        begin = 0
        question = 0
        begin =int(input("Digite sua opção:\n"))
        print(                                 )
        if begin == 1:
            question = str(input("""Você gostaria de jogar o dado?
            \n--- Para jogar digite: sim ---
            \n--- Para sair digite: não ---
            \n"""))
            while question != "não":
                if question == "sim":
                    print("Jogando o dado\n")
                    print("\nO dado caiu no", randint(1,6))
                    print(                                )
                    question = str(input("Você gostaria de jogar o dado?\n"))  
                elif question == "não":
                    print("Fim de jogo\n")
            else:
                print(             )
                print("GAME OVER\n")
        elif begin == 2:
            print(                        )
            print ("SAINDO DO SIMULADOR/n")
            print(" ATÉ LOGO  \O/ ")
            sys.exit()

inicio()

                
