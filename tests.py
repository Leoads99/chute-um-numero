"""""""""""""""""""""""""""""""""""""""""""""""
import unicodedata

from unidecode import unidecode

def to_ascii(ls):
    for i in range(len(ls)):
        ls[i] = unidecode.unidecode(ls[i])
    to_ascii(ls)
    print(ls)
    return ls

lsa = ['Ação','porém']

to_ascii(lsa)
"""""""""""""""""""""""""""""""""""""""""""""""

#import unidecode

#palavras = [
#    u"acentuacao",
#    u"divagacão",
#    u"programaçao",
#    u"taxação",
#]

#def to_ascii(ls):
#    for i in range(len(ls)):
#        ls[i] = unidecode.unidecode(ls[i])
#
#to_ascii(palavras)
#print(palavras)

import sys
import time
from colorama import init
init()
from colorama import Fore, init
init()
from colorama import Back, init
init()
import unidecode

print(Back.BLACK+Fore.WHITE+'Copyright (C) Leonardo Andrade de Souza. Todos os direitos reservados.\n')
time.sleep(5)


linha = '-' * 100
print(linha)
titulo = Fore.RED +'GERENCIADOR COVID-19'
print(titulo.center(100))
print(linha)
time.sleep(5)

#Define uma lista vazia que irá receber os nomes dos pacientes do setor COVID-19
lnome = []
#Define uma lista vazia que irá receber os exames dos pacientes do setor COVID-19
lexames = []

#Define uma função que tira acentuação
def tira_acento_um(ls):
    for i in range(len(ls)):
        ls[i] = unidecode.unidecode(ls[i])

#tira_acento_um(lnome)
#print(lnome)

#Define uma função que tira acentuação
def tira_acento_dois(ls):
    for i in range(len(ls)):
        ls[i] = unidecode.unidecode(ls[i])

#tira_acento_dois(lexames)
#print(lexames)

#Define uma função que torna todas letras em maíusculas
#def palavra_maiscula(ls):
#    return ls.upper()


#Define uma função que remove elementos de uma lista
#def remover(lis1):
#    remove.lis1
    
    
#def remover(lista_nomes):
    #name_select = str(input(Fore.RED+'Qual nome você gostaria de remover?'))
    #lista_nomes.remove(name_select)
    
    
def removertudo(lista_nomes,lista_exames):
    name_select = str(input(Fore.RED+ 'Qual paciente você gostaria de remover?\n'))
    lista_nomes.remove(name_select)
    exame_select = str(input(Fore.RED+ 'Qual exame desse paciente você irá remover?\n'))
    lista_exames.remove(exame_select)
    
    
#Define uma função que printa as listas 
def mostrar(lista1,lista2):
    print(f'{lista1}\n',f'{lista2}\n')
        
        
acao = 0
while acao != 4:
    print(linha)
    try:
        acao = int(input(Fore.BLUE+'DIGITE\n'
                    '[1] para adicionar um paciente e exame realizado' 
                    '\n[2] para remover' 
                    '\n[3] para exibir os pacientes e exames' 
                    '\n[4] para sair\n'))
    except ValueError as err:
        print('OPÇÃO INVÁLIDA!')
    time.sleep(2)
    if acao == 1:
        print('=='*25)
        nome = str(input(Fore.BLUE+'Digite o nome do Paciente:\n'))
        print('=='*25)
        lnome.append(nome)
        palavra_maiscula(lnome)
        tira_acento_um(lnome)
        time.sleep(2)
        exames = str(input(Fore.BLUE+'Digite os exames do Paciente:\n'))
        print('=='*25)
        lexames.append(exames)
        palavra_maiscula(lexames)
        tira_acento_dois(lexames)
        time.sleep(2)
        print(lnome)
        print('=='*25)
        print(lexames)
        print('=='*25)
        time.sleep(2)
    if acao == 2:
        input(Fore.BLUE+'\nPara remover um paciente, Pressione ENTER para continuar')
        print('=='*25)
        #remover(lnome)
        removertudo(lnome,lexames)
        time.sleep(2)
        print(linha)
        print(Fore.BLUE+'PACIENTES / EXAMES ADICIONADOS:\n')
        print(linha)
        print(lnome)
        print(lexames)
        time.sleep(2)
        #input(Fore.BLUE+'\nPara remover um exame do paciente, Pressione ENTER para continuar')
        #print('=='*25)
        #remover(lexames)
        #removertudo(lnome,lexames)
        #print(linha)
        #time.sleep(2)
        #print(Fore.BLUE+'PACIENTES / EXAMES ADICIONADOS:\n')
        #print(linha)
        #print(lnomes)
        #print(lexames)
        #1time.sleep(2)
    if acao == 3:
        print(linha)
        print(Fore.BLUE+'PACIENTES / EXAMES ADICIONADOS:\n')
        print(linha)
        mostrar(lnome,lexames)
        time.sleep(2)
else:
    print (Fore.RED+'SAINDO DO GERENCIADOR\n')
    time.sleep(2)
    print(Fore.BLUE +' ATÉ LOGO  \O/ ')
    time.sleep(2)
    print(Fore.BLACK+'\nCopyright (C) Todos os direitos reservados, Leonardo Andrade de Souza')
    time.sleep(5)
    sys.exit()