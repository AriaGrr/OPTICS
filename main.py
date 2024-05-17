# Turma 725, Equipe 3:
# Marjorie Luize Martins Costa, RA: 24223084-5;
# Matheus Ferreira de Freitas, RA: 24123080-4;
# Henrique Hodel Babler, RA: 24123079-6;

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

# Funções de cálculo
def I1_I2(): # Função para calcular I1 e I2
    t2 = Decimal(input(f"Digite o valor de {Fore.RED}θ2{Fore.RESET}: "))
    t1 = Decimal(input(f"\nDigite o valor de {Fore.RED}θ1{Fore.RESET}: "))
    I0 = Decimal(input(f"\nDigite o valor de {Fore.GREEN}I0{Fore.RESET} em {Fore.BLUE}W/cm²{Fore.RESET}: "))

    I1 = I0 / 2
    I2 = I1 * Decimal(math.cos(math.radians(t2 - t1))**2)

    print(f"\nO valor de {Fore.GREEN}I1{Fore.RESET} é: {Fore.MAGENTA}{I1:.3e}{Fore.BLUE} W/cm²{Fore.RESET}\n")
    print(f"O valor de {Fore.GREEN}I2{Fore.RESET} é: {Fore.MAGENTA}{I2:.3e}{Fore.BLUE} W/cm²{Fore.RESET}\n")

def I0_I2(): # Função para calcular I0 e I2
    t2 = Decimal(input(f"Digite o valor de θ2: "))
    t1 = Decimal(input(f"\nDigite o valor de θ1: "))
    I1 = Decimal(input(f"\nDigite o valor de I1 em W/cm²: "))

    I0 = I1 * 2
    I2 = I1 * Decimal(math.cos(math.radians(t2 - t1))**2)

    print(f"\nO valor de I0 é: {I0:.3e} W/cm²\n")
    print(f"O valor de I2 é: {I2:.3e} W/cm²\n")

def I0_I1(): # Função para calcular I0 e I1
    t2 = Decimal(input(f"Digite o valor de θ2: "))
    t1 = Decimal(input(f"\nDigite o valor de θ1: "))
    I2 = Decimal(input(f"\nDigite o valor de {Fore.GREEN}I2 em W/cm²: "))

    I0 = 2 * I2 / Decimal(math.cos(math.radians(t2 - t1))**2)
    I1 = I0 / 2

    print(f"\nO valor de I1 é: {I1:.3e}W/cm²\n")
    print(f"O valor de I0 é: {I0:.3e}W/cm²\n")

def I1_I2_I3(): # Função para calcular I1, I2 e I3
    t3 = Decimal(input(f"Digite o valor de θ3: "))
    t2 = Decimal(input(f"\nDigite o valor de θ2: "))
    t1 = Decimal(input(f"\nDigite o valor de θ1: "))
    I0 = Decimal(input(f"\nDigite o valor de I0 em W/cm²: "))

    I1 = I0 / 2
    I2 = I1 * Decimal(math.cos(math.radians(t2 - t1))**2)
    I3 = I2 * Decimal(math.cos(math.radians(t3 - t2))**2)

    print(f"\nO valor de I1 é: {I1:.3e}W/cm²\n")
    print(f"O valor de I2 é: {I2:.3e}W/cm²\n")
    print(f"O valor de I3 é: {I3:.3e}W/cm²\n")

def I0_I2_I3(): # Função para calcular I0, I2 e I3
    t3 = Decimal(input(f"Digite o valor de θ3: "))
    t2 = Decimal(input(f"\nDigite o valor de θ2: "))
    t1 = Decimal(input(f"\nDigite o valor de θ1: "))
    I1 = Decimal(input(f"\nDigite o valor de I1 em W/cm²: "))

    I0 = 2 * I1
    I2 = I1 * Decimal(math.cos(math.radians(t2 - t1))**2)
    I3 = I2 * Decimal(math.cos(math.radians(t3 - t2))**2)

    print(f"\nO valor de I0 é: {I0:.3e}W/cm²\n")
    print(f"O valor de I2 é: {I2:.3e}W/cm²\n")
    print(f"O valor de I3 é: {I3:.3e}W/cm²\n")

def I0_I1_I3(): # Função para calcular I0, I1 e I3
    t3 = Decimal(input(f"Digite o valor de θ3: "))
    t2 = Decimal(input(f"\nDigite o valor de θ2: "))
    t1 = Decimal(input(f"\nDigite o valor de θ1: "))
    I2 = Decimal(input(f"\nDigite o valor de I2 em W/cm²: "))

    I0 = 2 * I2 / Decimal(math.cos(math.radians(t3 - t1))**2)
    I1 = I0 / 2
    I3 = I2 * Decimal(math.cos(math.radians(t3 - t2))**2)

    print(f"\nO valor de I0 é: {I0:.3e}W/cm²\n")
    print(f"O valor de I1 é: {I1:.3e}W/cm²\n")
    print(f"O valor de I3 é: {I3:.3e}W/cm²\n")

def I0_I1_I2(): # Função para calcular I0, I1 e I2
    t3 = Decimal(input(f"Digite o valor de θ3: "))
    t2 = Decimal(input(f"\nDigite o valor de θ2: "))
    t1 = Decimal(input(f"\nDigite o valor de θ1: "))
    I3 = Decimal(input(f"\nDigite o valor de I3 em W/cm²: "))

    I0 = 2 * I3 / Decimal(math.cos(math.radians(t3 - t1))**2)
    I1 = I0 / 2
    I2 = I1 * Decimal(math.cos(math.radians(t2 - t1))**2)

    print(f"\nO valor de I0 é: {I0:.3e}W/cm²\n")
    print(f"O valor de I1 é: {I1:.3e}W/cm²\n")
    print(f"O valor de I2 é: {I2:.3e}W/cm²\n")

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
        print(f'Redirecionando para o cálculo de I1 e I2...\n')
        I1_I2()
    elif option == '2':
        clear_screen()
        print(f'Redirecionando para o cálculo de I0 e I2...\n')
        I0_I2()
    elif option == '3':
        clear_screen()
        print(f'Redirecionando para o cálculo de I0 e I1...\n')
        I0_I1()
    elif option == '0':
        print(f'Voltando...')
        clear_screen()
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
        print(f'Redirecionando para o cálculo de I1, I2 e I3...\n')
        I1_I2_I3()
    elif option == '2':
        clear_screen()
        print(f'Redirecionando para o cálculo de I0, I2 e I3...\n')
        I0_I2_I3()
    elif option == '3':
        clear_screen()
        print(f'Redirecionando para o cálculo de I0, I1 e I3...\n')
        I0_I1_I3()
    elif option == '4':
        clear_screen()
        print(f'Redirecionando para o cálculo de I0, I1 e I2...\n')
        I0_I1_I2()
    elif option == '0':
        print(f'Voltando...\n')
        clear_screen()
    else:
        print(f'Opção inválida. Escolha uma opção válida.')

def menu(): # Função para o menu de cálculos
    print(f'{Fore.GREEN}Opções:{Fore.RESET}\n')
    print(f'{Fore.GREEN}1 -{Fore.RESET} Dois polarizadores\n')
    print(f'{Fore.GREEN}2 -{Fore.RESET} Três polarizadores\n')
    print(f'{Fore.GREEN}0 -{Fore.RESET} Voltar\n')
    option = input(f'{Fore.BLUE}Escolha uma opção:{Fore.RESET} ')

    if option == '1':
        print('Redirecionando para o menu de dois polarizadores...')
        clear_screen()
        menu_2polarizadores()
    elif option == '2':
        print('Redirecionando para o menu de três polarizadores...')
        clear_screen()
        menu_3polarizadores()
    elif option == '0':
        print('Voltando...')
        clear_screen()
    

# def menu_conversores(): # Função para o menu de conversores
#     print('Opções:')


# Menu principal
while True:
    clear_screen()

    if teste == 0:
        print(f"{Fore.RED}Tópicos de Óptica e Física Moderna{Fore.RESET}")
        print(f"{Fore.BLUE}-----------------------------------------------{Fore.RESET}")
        print(f"{Fore.MAGENTA}-> Equipe 3{Fore.RESET}")
        print(f"{Fore.MAGENTA}✔{Fore.RESET} Marjorie Luize Martins Costa, {Fore.MAGENTA}RA:{Fore.RESET} 24223084-5")
        print(f"{Fore.MAGENTA}✔{Fore.RESET} Matheus Ferreira de Freitas, {Fore.MAGENTA}RA:{Fore.RESET} 24123080-4")
        print(f"{Fore.MAGENTA}✔{Fore.RESET} Henrique Hodel Babler, {Fore.MAGENTA}RA:{Fore.RESET} 24123079-6")
        print(f"{Fore.MAGENTA}!{Fore.RESET} Turma 725")
        print(f"{Fore.BLUE}-----------------------------------------------{Fore.RESET}")
        print(f"{Fore.RED}ℹ️{Fore.RESET} Texto explicativo...")
        print(f"{Fore.BLUE}-----------------------------------------------{Fore.RESET}")
        print(f'{Fore.GREEN}Pressione Enter para continuar...{Fore.RESET}')
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

    input('Pressione Enter para continuar...')

print('Finalizando...')