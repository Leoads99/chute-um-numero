"""""""""""""""""
2. CHUTE O NÚMERO
Objetivo: Criar um script que gerá um valor aleatoriamente, guarda este valor, e pergunta repetidamente para o usuário chutar o valor gerado até que ele acerte.

Habilidades praticas a aplicar:

Random
Comparadores matemáticos
Controle de Fluxo
Entrada de dados
Saida de dados
Detalhes e boas Práticas: Você deve criar um projeto para rodar na linha de comando que ao iniciar, irá gerar, armazenar, porem não exibir um valor aleatório entre um valor mínimo e máximo que será definido por você ( 10-100, por exemplo). Com esse valor gerado e armazenado de alguma forma que você (o criador ou jogador do script) não possa ver, faça uma pergunta do tipo: “Chute um número” para quem estiver rodando o script e com isso o programa deve gravar a resposta que foi passada.

Depois disso você terá 3 caminhos possíveis: 1. Avisar que a pessoa chutou baixo, 2 dizer que chutou alto ou parabenizar dizer que acertou! Considerando os três possíveis caminhos que podem ser seguidos, você deve cuidar para que em todo o momento a entrada de dados seja tratado para exceções e que caso o usuário digite algo inesperado, que ele receba uma mensagem amigável o informando das possíveis opções que seu programa oferece. Isso deve continuar acontecendo indefinitivamente até que a pessoa acerte o número ou desista por não conseguir acertar hahaha(acontece).
"""""""""""""""""

#Gerar valor aleatório 

from random import randint
import random

#def gerar_valor():
    #valor_aleatorio = random.randint(0,100)
    #return valor_aleatorio

question = input(
                'Para Gerar Valor aleatório digite: s \n' 
                'Para sair digite: n \n'
                 )
cont = 0 
while question != 'n':
    valor_aleatorio = random.randint(0,100)
    #print (valor_aleatorio)
    #para contar a quantidade de valores gerados
    cont = cont+1    
    #print ('Esse é o', cont, '° valor gerado é:\n')    
    perguntar_valor = int(input('Chute o valor que foi gerado:\n'))
    while perguntar_valor != valor_aleatorio:
        if perguntar_valor > valor_aleatorio:
            print ('É maior que o número gerado')
            perguntar_valor = int(input('Chute o valor que foi gerado:\n'))
        elif perguntar_valor < valor_aleatorio:
            print ('É menor que o número gerado')
            perguntar_valor = int(input('Chute o valor que foi gerado:\n'))
    else:
        print ('Parabéns você acertou!\n')
        print ('O total de valores gerados foi', cont, 'valores aleatórios\n')
        question = input(
                'Para Gerar Valor aleatório digite: s \n' 
                'Para sair digite: n \n'
                 ) 
else:
    print ('FIM')

