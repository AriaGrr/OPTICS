# Turma 725, Equipe 3:
# Marjorie Luize Martins Costa, RA: 24223084-5;
# Matheus Ferreira de Freitas, RA: 24123080-4;
# Henrique Hodel Babler, RA: 24123079-6;

# Paralelo = Teta 0, se é teta x com a vertical, colocar apenas x
# Luz incidente: a intensidade da luz não polarizada é I0
# Vertical = 0 |
# Horizontal = 90 _ 
# Formula: I = I0 * cos²(teta)
# I0 = 2 * I1
# Formula: I = I1 * cos²(teta2 - teta1)
# I1 = I0 / 2
# Lei de Malus: I = I0 * cos²(teta2 - teta1)

# Bibliotecas
import math
from decimal import Decimal

# Variaveis globais

teste = 0 # Variável para testar se é a primeira vez que o programa é executado

# Constantes

# Variaveis

# # I = Intensidade de luz não polarizada
# I0 = 0
# I1 = 0
# I2 = 0
# I3 = 0

# # t = Ângulo de transmissão
# t1 = 0
# t2 = 0
# t3 = 0

# Funcoes

# def limpar_variaveis(): # Função para limpar as variáveis
#     print('Limpando variáveis...')

def clear_screen(): # Função para limpar a tela do terminal
    print('\033[H\033[J')

def clear(): # Função para pause
    input(f'Pressione Enter para continuar...')
    clear_screen()
    menu()

# Funções de cálculo
def I1_I2(): # Função para calcular I1 e I2
    I0 = Decimal(input(f"Digite o valor de I0 em W/cm²: "))
    t1 = Decimal(input(f"\nDigite o valor de θ1: "))
    t2 = Decimal(input(f"\nDigite o valor de θ2: "))

    I1 = I0 / 2
    I2 = I1 * Decimal(math.cos(math.radians(t2 - t1))**2)

    print(f"\n-----------------------------------------------")
    print(f"\nO valor de I1 é: {I1:.3e} W/cm²\n")
    print(f"O valor de I2 é: {I2:.3e} W/cm²")
    print(f"\n-----------------------------------------------")
    
def I0_I2(): # Função para calcular I0 e I2
    I1 = Decimal(input(f"Digite o valor de I1 em W/cm²: "))
    t1 = Decimal(input(f"\nDigite o valor de θ1: "))
    t2 = Decimal(input(f"\nDigite o valor de θ2: "))

    I0 = I1 * 2
    I2 = I1 * Decimal(math.cos(math.radians(t2 - t1))**2)

    print(f"\n-----------------------------------------------")
    print(f"\nO valor de I0 é: {I0:.3e} W/cm²\n")
    print(f"O valor de I2 é: {I2:.3e} W/cm²")
    print(f"\n-----------------------------------------------")

def I0_I1(): # Função para calcular I0 e I1
    I2 = Decimal(input(f"Digite o valor de I2 em W/cm²: "))
    t1 = Decimal(input(f"\nDigite o valor de θ1: "))
    t2 = Decimal(input(f"\nDigite o valor de θ2: "))

    I0 = 2 * I2 / Decimal(math.cos(math.radians(t2 - t1))**2)
    I1 = I0 / 2

    print(f"\n-----------------------------------------------")
    print(f"\nO valor de I0 é: {I0:.3e} W/cm²\n")
    print(f"O valor de I1 é: {I1:.3e} W/cm²")
    print(f"\n-----------------------------------------------")

def I1_I2_I3(): # Função para calcular I1, I2 e I3
    I0 = Decimal(input(f"Digite o valor de I0 em W/cm²: "))
    t1 = Decimal(input(f"\nDigite o valor de θ1: "))
    t2 = Decimal(input(f"\nDigite o valor de θ2: "))
    t3 = Decimal(input(f"\nDigite o valor de θ3: "))

    I1 = I0 / 2
    I2 = I1 * Decimal(math.cos(math.radians(t2 - t1))**2)
    I3 = I2 * Decimal(math.cos(math.radians(t3 - t2))**2)

    print(f"\n-----------------------------------------------")
    print(f"\nO valor de I1 é: {I1:.3e} W/cm²\n")
    print(f"O valor de I2 é: {I2:.3e} W/cm²\n")
    print(f"O valor de I3 é: {I3:.3e} W/cm²")
    print(f"\n-----------------------------------------------")

def I0_I2_I3(): # Função para calcular I0, I2 e I3
    I1 = Decimal(input(f"Digite o valor de I1 em W/cm²: "))
    t1 = Decimal(input(f"\nDigite o valor de θ1: "))
    t2 = Decimal(input(f"\nDigite o valor de θ2: "))
    t3 = Decimal(input(f"\nDigite o valor de θ3: "))

    I0 = 2 * I1
    I2 = I1 * Decimal(math.cos(math.radians(t2 - t1))**2)
    I3 = I2 * Decimal(math.cos(math.radians(t3 - t2))**2)

    print(f"\n-----------------------------------------------")
    print(f"\nO valor de I0 é: {I0:.3e} W/cm²\n")
    print(f"O valor de I2 é: {I2:.3e} W/cm²\n")
    print(f"O valor de I3 é: {I3:.3e} W/cm²")
    print(f"\n-----------------------------------------------")

def I0_I1_I3(): # Função para calcular I0, I1 e I3
    I2 = Decimal(input(f"Digite o valor de I2 em W/cm²: "))
    t1 = Decimal(input(f"\nDigite o valor de θ1: "))
    t2 = Decimal(input(f"\nDigite o valor de θ2: "))
    t3 = Decimal(input(f"\nDigite o valor de θ3: "))

    I0 = 2 * I2 / Decimal(math.cos(math.radians(t2 - t1))**2)
    I1 = I0 / 2
    I3 = I2 * Decimal(math.cos(math.radians(t3 - t2))**2)

    print(f"\n-----------------------------------------------")
    print(f"\nO valor de I0 é: {I0:.3e} W/cm²\n")
    print(f"O valor de I1 é: {I1:.3e} W/cm²\n")
    print(f"O valor de I3 é: {I3:.3e} W/cm²\n")
    print(f"-----------------------------------------------")

def I0_I1_I2(): # Função para calcular I0, I1 e I2
    I3 = Decimal(input(f"Digite o valor de I3 em W/cm²: "))
    t1 = Decimal(input(f"\nDigite o valor de θ1: "))
    t2 = Decimal(input(f"\nDigite o valor de θ2: "))
    t3 = Decimal(input(f"\nDigite o valor de θ3: "))

    I0 = 2 * I3 / Decimal(math.cos(math.radians(t2 - t1)) **2) / Decimal(math.cos(math.radians(t3 - t2))**2)
    I1 = I0 / 2
    I2 = I1 * Decimal(math.cos(math.radians(t2 - t1))**2)

    print(f"\n-----------------------------------------------")
    print(f"\nO valor de I0 é: {I0:.3e} W/cm²\n")
    print(f"O valor de I1 é: {I1:.3e} W/cm²\n")
    print(f"O valor de I2 é: {I2:.3e} W/cm²")
    print(f"\n-----------------------------------------------")

# Funções menu

def menu_2polarizadores(): # Função para o menu de polarizadores
    print(f'Opções:\n')
    print(f"1 - Entrada: θ1, θ2 e I0")
    print(f"Saida: I1 e I2\n")
    print(f"2 - Entrada: θ1, θ2 e I1")
    print(f"Saida: I0 e I2\n")
    print(f"3 - Entrada: θ1, θ2 e I2")
    print(f"Saida: I0 e I1\n")
    print(f"0 - Voltar\n")
    option = input(f'Escolha uma opção: ')

    if option == '1':
        clear_screen()
        print(f'Cálculo de I1 e I2...\n')
        I1_I2()
        clear()

    elif option == '2':
        clear_screen()
        print(f'Cálculo de I0 e I2...\n')
        I0_I2()
        clear()

    elif option == '3':
        clear_screen()
        print(f'Cálculo de I0 e I1...\n')
        I0_I1()
        clear()

    elif option == '0':
        print(f'Voltando...')
        clear_screen()
        menu()
    else:
        print(f'Opção inválida. Escolha uma opção válida.')


def menu_3polarizadores(): # Função para o menu de polarizadores
    print(f'Opções:\n')
    print(f"1 - Entrada: θ1, θ2, θ3 e I0")
    print(f"Saida: I1, I2 e I3\n")
    print(f"2 - Entrada: θ1, θ2, θ3 e I1")
    print(f"Saida: I0, I2 e I3\n")
    print(f"3 - Entrada: θ1, θ2, θ3 e I2")
    print(f"Saida: I0, I1 e I3\n")
    print(f"4 - Entrada: θ1, θ2, θ3 e I3")
    print(f"Saida: I0, I1 e I2\n")
    print(f"0 - Voltar\n")
    option = input(f'Escolha uma opção: ')

    if option == '1':
        clear_screen()
        print(f'Cálculo de I1, I2 e I3...\n')
        I1_I2_I3()
        clear()
    elif option == '2':
        clear_screen()
        print(f'Cálculo de I0, I2 e I3...\n')
        I0_I2_I3()
        clear()
    elif option == '3':
        clear_screen()
        print(f'Cálculo de I0, I1 e I3...\n')
        I0_I1_I3()
        clear()
    elif option == '4':
        clear_screen()
        print(f'Cálculo de I0, I1 e I2...\n')
        I0_I1_I2()
        clear()
    elif option == '0':
        print(f'Voltando...\n')
        clear_screen()
        menu()
    else:
        print(f'Opção inválida. Escolha uma opção válida.')

def menu(): # Função para o menu de cálculos
    print(f'Opções:\n')
    print(f'1 - Voltar\n')
    print(f'2 - Dois polarizadores\n')
    print(f'3 - Três polarizadores\n')
    option = input(f'Escolha uma opção: ')

    if option == '2':
        print('Redirecionando para o menu de dois polarizadores...')
        clear_screen()
        menu_2polarizadores()
    elif option == '3':
        print('Redirecionando para o menu de três polarizadores...')
        clear_screen()
        menu_3polarizadores()
    elif option == '1':
        print('Voltando...')
        clear_screen()
    

# def menu_conversores(): # Função para o menu de conversores
#     print('Opções:')


# Menu principal
while True:
    clear_screen()

    if teste == 0:
        print(f"Tópicos de Óptica e Física Moderna")
        print(f"-----------------------------------------------")
        print(f"-> Equipe 3")
        print(f"✔ Marjorie Luize Martins Costa, RA: 24223084-5")
        print(f"✔ Matheus Ferreira de Freitas, RA: 24123080-4")
        print(f"✔ Henrique Hodel Babler, RA: 24123079-6")
        print(f"! Turma 725")
        print(f"-----------------------------------------------")
        print(f"ℹ️ O programa desenvolvido permite calcular a intensidade da luz após passar por polarizadores em um sistema óptico. Utilizando os ângulos de transmissão fornecidos pelo usuário, ele determina como a intensidade da luz não polarizada inicial é modificada ao atravessar até três polarizadores. Através de fórmulas baseadas nas leis de Malus e na física da polarização da luz, o programa calcula e exibe as intensidades resultantes, ajudando a entender o comportamento da luz em sistemas de polarização.")
        print(f"-----------------------------------------------")
        print(f'Pressione Enter para continuar...')
        input() 
        teste = Decimal(1)

    clear_screen()
    print(f'Opções:\n')
    print(f'1 - Cálculos\n')
    # print('2 - Conversores')
    # print('2 - Limpar variáveis')
    print(f'0 - Sair\n')
    option = input(f'Escolha uma opção: \n')

    if option == '1':
        print('Redirecionando para o menu de cálculos...\n')
        clear_screen()
        menu()

    # elif option == '2':
    #     print('Redirecionando para o menu de conversores...')
    #     menu_conversores()

    # elif option == '2':
    #     print('Limpando variáveis...')
    #     limpar_variaveis()

    elif option == '0':
        break
    else:
        print('Opção inválida. Escolha uma opção válida.')

    input(f'Pressione Enter para continuar...')

print('Finalizando...')
