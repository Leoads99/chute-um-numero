import sys
import time
import itertools
from itertools import zip_longest
from colorama import init
init()
from colorama import Fore, init
init()
from colorama import Back, init
init()
import unidecode


print(f'{Back.BLACK} {Fore.WHITE} Copyright (C) Leonardo Andrade de Souza. Todos os direitos reservados.\n')
time.sleep(5)


linha = '-' * 146
print(linha)
titulo = f'{Fore.BLUE} GERENCIADOR COVID-19'
print(titulo.center(146))
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


#Define uma função que tira acentuação
def tira_acento_dois(ls):
    for i in range(len(ls)):
        ls[i] = unidecode.unidecode(ls[i])

        
 #Define uma função que retira os pacientes       
def removertudo(lista_nomes,lista_exames):
    name_select = str(input(f'{Fore.RED}Qual paciente você gostaria de remover?\n')).upper()
    while name_select not in lista_nomes:
        print('Desculpe não entendi, esse paciente não foi encontrado')
        name_select = str(input(f'{Fore.RED}Qual paciente você gostaria de remover?\n')).upper()
    else:
        lista_nomes.remove(name_select)
    exame_select = str(input(f'{Fore.RED}Qual exame desse paciente você irá remover?\n')).upper()
    while exame_select not in lista_exames:
        print('Desculpe não entendi, esse exame não foi encontrado')
        exame_select = str(input(f'{Fore.RED}Qual exame desse paciente você irá remover?\n')).upper()
    else:
        lista_exames.remove(exame_select)
    
        
#Define uma função que printa as listas 
def mostrar(lista1,lista2):
    print(lista1, lista2)

    
#Define uma função que printa o histórico de pacientes e exames adicionados
def history_covid(dictionary):
    print('='*146)
    hist = 'HISTÓRICO DE PACIENTES E EXAMES ADICIONADOS:'
    print(hist.center(146))
    print('='*146)
    print(dictionary)
     
    
#Define uma função que busca o paciente e retorna seus exames
def find_pacient():
    print
    ('**Digite o nome conforme o inserido anteriormente,'
    f'{Fore.BLUE} se tiver digitado nome inteiro então, digite o nome inteiro.'
    f'{Fore.BLUE} se tiver inserido apenas o primeiro nome, então, digite o primeiro nome**') 
    name_pacient = str(input('Para buscar, digite o nome do paciente:\n')).upper()
    while name_pacient not in covid_pacients_dictionary:
        print('Desculpe não entendi, esse paciente não foi encontrado')
        print
        ('**Digite o nome conforme o inserido anteriormente,'
        f'{Fore.BLUE} se tiver digitado nome inteiro então, digite o nome inteiro.'
        f'{Fore.BLUE} se tiver inserido apenas o primeiro nome, então, digite o primeiro nome**') 
        name_pacient = str(input('Para buscar, digite o nome do paciente:\n')).upper()    
    else:
        localizator = covid_pacients_dictionary.get(name_pacient)
        print('                                                                                ')
        print (f'O paciente {name_pacient} tem os seguintes exames pendentes:\n' 
            f'{localizator}')

        
acao = 0
while acao != 6:
    print(linha)
    try:
        acao = int(input(Fore.BLUE+'DIGITE\n'
                    f'{Fore.WHITE}[1] para adicionar um paciente e exame realizado\n' 
                    f'{Fore.WHITE}[2] para remover\n' 
                    f'{Fore.WHITE}[3] para exibir os pacientes e exames\n'
                    f'{Fore.WHITE}[4] para exibir o histórico de pacientes e exames\n'
                    f'{Fore.WHITE}[5] para buscar os exames do paciente pelo nome\n' 
                    f'{Fore.WHITE}[6] para sair\n'))
    except ValueError as err:
        print('OPÇÃO INVÁLIDA!')
    time.sleep(1)
    if acao == 1:
        print('='*146)
        nome = str(input(f'{Fore.BLUE} Digite o nome do Paciente:\n')).upper()
        print('='*146)
        lnome.append(nome)
        tira_acento_um(lnome)
        #nome = dict(itertools.zip_longest(*[iter(lnome)] * 2, fillvalue=""))
        print(nome)
        time.sleep(1)
        exames = str(input(f'{Fore.BLUE} Digite os exames do Paciente:\n')).upper()
        print('='*146)
        lexames.append(exames)
        tira_acento_dois(lexames)
        covid_pacients_dictionary = dict(zip(lnome, lexames))
        #exames = dict(itertools.zip_longest(*[iter(lexames)] * 2, fillvalue=""))
        print(exames)
        time.sleep(1)
        print(lnome)
        print('='*146)
        print(lexames)
        print('='*146)
        time.sleep(1)
    if acao == 2:
        input(f'{Fore.BLUE} \nPara remover um paciente, Pressione ENTER para continuar')
        print('='*146)
        removertudo(lnome,lexames)
        time.sleep(1)
        print(linha)
        titulo2 = f'{Fore.BLUE} | PACIENTES |      | EXAMES ADICIONADOS | :\n'
        #print(titulo2.center(146))
        print(linha)
        print(lnome)
        print(lexames)
        time.sleep(1)
    if acao == 3:
        print(linha)
        titulo3 = f'{Fore.BLUE} | PACIENTES | | EXAMES ADICIONADOS| :\n'
        print(titulo3.center(146))
        print(linha)
        mostrar(lnome,lexames)
        time.sleep(1)
    if acao == 4:
        history_covid(covid_pacients_dictionary)
    if acao == 5:
        print('='*146)
        find_pacient()
        time.sleep(2)
else:
    print('='*146)
    adeus = f'{Fore.RED} SAINDO DO GERENCIADOR\n'
    print(adeus.center(146))
    print('='*146)
    time.sleep(2)
    print('='*146)
    ate_mais = f'{Fore.BLUE} ATÉ LOGO!\n'
    print(ate_mais.center(146))
    print('='*146)
    time.sleep(2)
    print('='*146)
    rights = f'{Fore.WHITE} Copyright (C) Todos os direitos reservados, Leonardo Andrade de Souza'
    print(rights.center(146))
    print('='*146)
    time.sleep(5)
    sys.exit()
