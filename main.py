# Turma 725, Equipe 3:
# Marjorie Luize Martins Costa, RA: 24223084-5;
# Matheus Ferreira de Freitas, RA: 24123080-4;
# Henrique Hodel Babler, RA: 24123079-6;

# Paralelo = Teta 0, se é teta x com a vertical, colocar apenas x
# Luz incidente: a intensidade da luz não polarizada é I0

# Bibliotecas
import math
from decimal import Decimal
from colorama import Fore, Style

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
    input(f'Pressione {Fore.GREEN}Enter{Fore.RESET} para continuar...')
    clear_screen()
    menu()

# Funções de cálculo
def I1_I2(): # Função para calcular I1 e I2
    I0 = Decimal(input(f"Digite o valor de {Fore.GREEN}I0{Fore.RESET} em {Fore.BLUE}W/cm²{Fore.RESET}: "))
    t1 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ1{Fore.RESET}: "))
    t2 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ2{Fore.RESET}: "))

    I1 = I0 / 2
    I2 = I1 * Decimal(math.cos(math.radians(t2 - t1))**2)

    print(f"\n{Fore.CYAN}-----------------------------------------------{Fore.RESET}")
    print(f"\nO valor de {Fore.GREEN}I1{Fore.RESET} é: {Fore.MAGENTA}{I1:.3e}{Fore.BLUE} W/cm²{Fore.RESET}\n")
    print(f"O valor de {Fore.GREEN}I2{Fore.RESET} é: {Fore.MAGENTA}{I2:.3e}{Fore.BLUE} W/cm²{Fore.RESET}")
    print(f"\n{Fore.CYAN}-----------------------------------------------{Fore.RESET}")
    
def I0_I2(): # Função para calcular I0 e I2
    I1 = Decimal(input(f"Digite o valor de {Fore.GREEN}I1{Fore.RESET} em {Fore.BLUE}W/cm²{Fore.RESET}: "))
    t1 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ1{Fore.RESET}: "))
    t2 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ2{Fore.RESET}: "))

    I0 = I1 * 2
    I2 = I1 * Decimal(math.cos(math.radians(t2 - t1))**2)

    print(f"\n{Fore.CYAN}-----------------------------------------------{Fore.RESET}")
    print(f"\nO valor de {Fore.GREEN}I0{Fore.RESET} é: {Fore.MAGENTA}{I0:.3e}{Fore.BLUE} W/cm²{Fore.RESET}\n")
    print(f"O valor de {Fore.GREEN}I2{Fore.RESET} é: {Fore.MAGENTA}{I2:.3e}{Fore.BLUE} W/cm²{Fore.RESET}")
    print(f"\n{Fore.CYAN}-----------------------------------------------{Fore.RESET}")

def I0_I1(): # Função para calcular I0 e I1
    I2 = Decimal(input(f"Digite o valor de {Fore.GREEN}I2{Fore.RESET} em {Fore.BLUE}W/cm²{Fore.RESET}: "))
    t1 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ1{Fore.RESET}: "))
    t2 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ2{Fore.RESET}: "))

    I0 = 2 * I2 / Decimal(math.cos(math.radians(t2 - t1))**2)
    I1 = I0 / 2

    print(f"\n{Fore.CYAN}-----------------------------------------------{Fore.RESET}")
    print(f"\nO valor de {Fore.GREEN}I0{Fore.RESET} é: {Fore.MAGENTA}{I0:.3e}{Fore.BLUE} W/cm²{Fore.RESET}\n")
    print(f"O valor de {Fore.GREEN}I1{Fore.RESET} é: {Fore.MAGENTA}{I1:.3e}{Fore.BLUE} W/cm²{Fore.RESET}")
    print(f"\n{Fore.CYAN}-----------------------------------------------{Fore.RESET}")

def I1_I2_I3(): # Função para calcular I1, I2 e I3
    I0 = Decimal(input(f"Digite o valor de {Fore.GREEN}I0 em {Fore.BLUE}W/cm²{Fore.RESET}: "))
    t1 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ1{Fore.RESET}: "))
    t2 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ2{Fore.RESET}: "))
    t3 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ3{Fore.RESET}: "))

    I1 = I0 / 2
    I2 = I1 * Decimal(math.cos(math.radians(t2 - t1))**2)
    I3 = I2 * Decimal(math.cos(math.radians(t3 - t2))**2)

    print(f"\n{Fore.CYAN}-----------------------------------------------{Fore.RESET}")
    print(f"\nO valor de {Fore.GREEN}I1{Fore.RESET} é: {Fore.MAGENTA}{I1:.3e}{Fore.BLUE} W/cm²{Fore.RESET}\n")
    print(f"O valor de {Fore.GREEN}I2{Fore.RESET} é: {Fore.MAGENTA}{I2:.3e}{Fore.BLUE} W/cm²{Fore.RESET}\n")
    print(f"O valor de {Fore.GREEN}I3{Fore.RESET} é: {Fore.MAGENTA}{I3:.3e}{Fore.BLUE} W/cm²{Fore.RESET}")
    print(f"\n{Fore.CYAN}-----------------------------------------------{Fore.RESET}")

def I0_I2_I3(): # Função para calcular I0, I2 e I3
    I1 = Decimal(input(f"Digite o valor de {Fore.GREEN}I1 em {Fore.BLUE}W/cm²{Fore.RESET}: "))
    t1 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ1{Fore.RESET}: "))
    t2 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ2{Fore.RESET}: "))
    t3 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ3{Fore.RESET}: "))

    I0 = 2 * I1
    I2 = I1 * Decimal(math.cos(math.radians(t2 - t1))**2)
    I3 = I2 * Decimal(math.cos(math.radians(t3 - t2))**2)

    print(f"\n{Fore.CYAN}-----------------------------------------------{Fore.RESET}")
    print(f"\nO valor de {Fore.GREEN}I0{Fore.RESET} é: {Fore.MAGENTA}{I0:.3e}{Fore.BLUE} W/cm²{Fore.RESET}\n")
    print(f"O valor de {Fore.GREEN}I2{Fore.RESET} é: {Fore.MAGENTA}{I2:.3e}{Fore.BLUE} W/cm²{Fore.RESET}\n")
    print(f"O valor de {Fore.GREEN}I3{Fore.RESET} é: {Fore.MAGENTA}{I3:.3e}{Fore.BLUE} W/cm²{Fore.RESET}")
    print(f"\n{Fore.CYAN}-----------------------------------------------{Fore.RESET}")

def I0_I1_I3(): # Função para calcular I0, I1 e I3
    I2 = Decimal(input(f"Digite o valor de {Fore.GREEN}I2{Fore.RESET} em {Fore.BLUE}W/cm²{Fore.RESET}: "))
    t1 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ1{Fore.RESET}: "))
    t2 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ2{Fore.RESET}: "))
    t3 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ3{Fore.RESET}: "))

    I0 = 2 * I2 / Decimal(math.cos(math.radians(t2 - t1))**2)
    I1 = I0 / 2
    I3 = I2 * Decimal(math.cos(math.radians(t3 - t2))**2)

    print(f"\n{Fore.CYAN}-----------------------------------------------{Fore.RESET}")
    print(f"\nO valor de {Fore.GREEN}I0{Fore.RESET} é: {Fore.MAGENTA}{I0:.3e}{Fore.BLUE} W/cm²{Fore.RESET}\n")
    print(f"O valor de {Fore.GREEN}I1{Fore.RESET} é: {Fore.MAGENTA}{I1:.3e}{Fore.BLUE} W/cm²{Fore.RESET}\n")
    print(f"O valor de {Fore.GREEN}I3{Fore.RESET} é: {Fore.MAGENTA}{I3:.3e}{Fore.BLUE} W/cm²{Fore.RESET}\n")
    print(f"{Fore.CYAN}-----------------------------------------------{Fore.RESET}")

def I0_I1_I2(): # Função para calcular I0, I1 e I2
    I3 = Decimal(input(f"Digite o valor de {Fore.GREEN}I3{Fore.RESET} em {Fore.BLUE}W/cm²{Fore.RESET}: "))
    t1 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ1{Fore.RESET}: "))
    t2 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ2{Fore.RESET}: "))
    t3 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ3{Fore.RESET}: "))

    I0 = 2 * I3 / Decimal(math.cos(math.radians(t2 - t1)) **2) / Decimal(math.cos(math.radians(t3 - t2))**2)
    I1 = I0 / 2
    I2 = I1 * Decimal(math.cos(math.radians(t2 - t1))**2)

    print(f"\n{Fore.CYAN}-----------------------------------------------{Fore.RESET}")
    print(f"\nO valor de {Fore.GREEN}I0{Fore.RESET} é: {Fore.MAGENTA}{I0:.3e}{Fore.BLUE} W/cm²{Fore.RESET}\n")
    print(f"O valor de {Fore.GREEN}I1{Fore.RESET} é: {Fore.MAGENTA}{I1:.3e}{Fore.BLUE} W/cm²{Fore.RESET}\n")
    print(f"O valor de {Fore.GREEN}I2{Fore.RESET} é: {Fore.MAGENTA}{I2:.3e}{Fore.BLUE} W/cm²{Fore.RESET}")
    print(f"\n{Fore.CYAN}-----------------------------------------------{Fore.RESET}")

# Funções menu

def menu_2polarizadores(): # Função para o menu de polarizadores
    print(f'{Fore.BLUE}Opções:{Fore.RESET}\n')
    print(f"{Fore.BLUE}1 - {Fore.GREEN}Entrada:{Fore.RESET} θ1, θ2 e {Fore.MAGENTA}I0")
    print(f"{Fore.RED}Saida:{Fore.RESET} I1 e I2\n")
    print(f"{Fore.BLUE}2 - {Fore.GREEN}Entrada:{Fore.RESET} θ1, θ2 e {Fore.MAGENTA}I1")
    print(f"{Fore.RED}Saida:{Fore.RESET} I0 e I2\n")
    print(f"{Fore.BLUE}3 - {Fore.GREEN}Entrada:{Fore.RESET} θ1, θ2 e {Fore.MAGENTA}I2")
    print(f"{Fore.RED}Saida:{Fore.RESET} I0 e I1\n")
    print(f"{Fore.BLUE}0 -{Fore.RESET} Voltar\n")
    option = input(f'{Fore.BLUE}Escolha uma opção:{Fore.RESET} ')

    if option == '1':
        clear_screen()
        print(f'Cálculo de {Fore.GREEN}I1{Fore.RESET} e {Fore.GREEN}I2{Fore.RESET}...\n')
        I1_I2()
        clear()

    elif option == '2':
        clear_screen()
        print(f'Cálculo de {Fore.GREEN}I0{Fore.RESET} e {Fore.GREEN}I2{Fore.RESET}...\n')
        I0_I2()
        clear()

    elif option == '3':
        clear_screen()
        print(f'Cálculo de {Fore.GREEN}I0{Fore.RESET} e {Fore.GREEN}I1{Fore.RESET}...\n')
        I0_I1()
        clear()

    elif option == '0':
        print(f'Voltando...')
        clear_screen()
        menu()
    else:
        print(f'Opção inválida. Escolha uma opção válida.')


def menu_3polarizadores(): # Função para o menu de polarizadores
    print(f'{Fore.BLUE}Opções:{Fore.RESET}\n')
    print(f"{Fore.BLUE}1 -{Fore.GREEN} Entrada:{Fore.RESET} θ1, θ2, θ3 e {Fore.MAGENTA}I0")
    print(f"{Fore.RED}Saida:{Fore.RESET} I1, I2 e I3\n")
    print(f"{Fore.BLUE}2 -{Fore.GREEN} Entrada:{Fore.RESET} θ1, θ2, θ3 e {Fore.MAGENTA}I1")
    print(f"{Fore.RED}Saida:{Fore.RESET} I0, I2 e I3\n")
    print(f"{Fore.BLUE}3 -{Fore.GREEN} Entrada:{Fore.RESET} θ1, θ2, θ3 e {Fore.MAGENTA}I2")
    print(f"{Fore.RED}Saida:{Fore.RESET} I0, I1 e I3\n")
    print(f"{Fore.BLUE}4 -{Fore.GREEN} Entrada:{Fore.RESET} θ1, θ2, θ3 e {Fore.MAGENTA}I3")
    print(f"{Fore.RED}Saida:{Fore.RESET} I0, I1 e I2\n")
    print(f"{Fore.BLUE}0 -{Fore.RESET} Voltar\n")
    option = input(f'{Fore.GREEN}Escolha uma opção:{Fore.RESET} ')

    if option == '1':
        clear_screen()
        print(f'Cálculo de {Fore.GREEN}I1{Fore.RESET}, {Fore.GREEN}I2{Fore.RESET} e {Fore.GREEN}I3{Fore.RESET}...\n')
        I1_I2_I3()
        clear()
    elif option == '2':
        clear_screen()
        print(f'Cálculo de {Fore.GREEN}I0{Fore.RESET}, {Fore.GREEN}I2{Fore.RESET} e {Fore.GREEN}I3{Fore.RESET}...\n')
        I0_I2_I3()
        clear()
    elif option == '3':
        clear_screen()
        print(f'Cálculo de {Fore.GREEN}I0{Fore.RESET}, {Fore.GREEN}I1{Fore.RESET} e {Fore.GREEN}I3{Fore.RESET}...\n')
        I0_I1_I3()
        clear()
    elif option == '4':
        clear_screen()
        print(f'Cálculo de {Fore.GREEN}I0{Fore.RESET}, {Fore.GREEN}I1{Fore.RESET} e {Fore.GREEN}I2{Fore.RESET}...\n')
        I0_I1_I2()
        clear()
    elif option == '0':
        print(f'Voltando...\n')
        clear_screen()
        menu()
    else:
        print(f'Opção inválida. Escolha uma opção válida.')

def menu(): # Função para o menu de cálculos
    print(f'{Fore.GREEN}Opções:{Fore.RESET}\n')
    print(f'{Fore.GREEN}1 -{Fore.RESET} Voltar\n')
    print(f'{Fore.GREEN}2 -{Fore.RESET} Dois polarizadores\n')
    print(f'{Fore.GREEN}3 -{Fore.RESET} Três polarizadores\n')
    option = input(f'{Fore.BLUE}Escolha uma opção:{Fore.RESET} ')

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
        print(f"Tópicos de {Fore.YELLOW}Óptica{Fore.RESET} e {Fore.RED}Física Moderna")
        print(f"{Fore.CYAN}-----------------------------------------------{Fore.RESET}")
        print(f"{Fore.MAGENTA}-> {Fore.RESET}Equipe {Fore.MAGENTA}3")
        print(f"{Fore.BLUE}✔{Fore.RESET} Marjorie Luize Martins Costa, {Fore.MAGENTA}RA:{Fore.RESET} 24223084-5")
        print(f"{Fore.BLUE}✔{Fore.RESET} Matheus Ferreira de Freitas, {Fore.MAGENTA}RA:{Fore.RESET} 24123080-4")
        print(f"{Fore.BLUE}✔{Fore.RESET} Henrique Hodel Babler, {Fore.MAGENTA}RA:{Fore.RESET} 24123079-6")
        print(f"{Fore.MAGENTA}!{Fore.RESET} Turma {Fore.MAGENTA}725")
        print(f"{Fore.CYAN}-----------------------------------------------{Fore.RESET}")
        print(f"{Fore.YELLOW}ℹ️{Fore.RESET} O programa desenvolvido permite calcular a intensidade da luz após passar por polarizadores em um sistema óptico. Utilizando os ângulos de transmissão fornecidos pelo usuário, ele determina como a intensidade da luz não polarizada inicial é modificada ao atravessar até três polarizadores. Através de fórmulas baseadas nas leis de Malus e na física da polarização da luz, o programa calcula e exibe as intensidades resultantes, ajudando a entender o comportamento da luz em sistemas de polarização.")
        print(f"{Fore.CYAN}-----------------------------------------------{Fore.RESET}")
        print(f'Pressione {Fore.GREEN}Enter{Fore.RESET} para continuar...')
        input() 
        teste = Decimal(1)

    clear_screen()
    print(f'{Fore.MAGENTA}Opções:{Fore.RESET}\n')
    print(f'{Fore.MAGENTA}1 -{Fore.RESET} Cálculos\n')
    # print('2 - Conversores')
    # print('2 - Limpar variáveis')
    print(f'{Fore.MAGENTA}0 -{Fore.RESET} Sair\n')
    option = input(f'{Fore.GREEN}Escolha uma opção: {Fore.RESET}\n')

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

    input(f'Pressione {Fore.GREEN}Enter{Fore.RESET} para continuar...')

print('Finalizando...')
