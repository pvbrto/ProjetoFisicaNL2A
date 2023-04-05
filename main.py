import time
import os
import math
os.system('cls')
print("=============NL2A - Átomo de Bohr=============")
os.system('cls')
print()
print("==================Sumário e Objetivos==================")
print()
print()
time.sleep(12)
os.system('cls')
print("==================Integrantes do Grupo=================")
print()
print("- Livia Miyabara\n- Luiggi Paschoalini\n- Marcio Forner\n- Paulo Brito")
print()
time.sleep(3)
os.system('cls')

# Constantes físicas
h = 6.62607015e-34  # Constante de Planck
heV = 4.136e-15  # Constante de Planck em eV
c = 3e8      # Velocidade da luz
me = 9.10938356e-31 # Massa do elétron
e = 1.602176634e-19 # Carga elementar

# Funções para cálculo de raio, velocidade, comprimento de onda, energia cinética, energia potencial e energia total
def radius(n):
    return (n**2)*(5.29e-11)

def velocity(n):
    return (2.187e6)/n

def wavelength(n):
    return h/(me*velocity(n))

def kinetic_energy(n):
    return 13.6/(n**2)

def potential_energy(n):
    
    return -27.2/(n**2)

def total_energy(n):
    return -13.6/(n**2)

# Funções para cálculo de energia, comprimento de onda e frequência do fóton absorvido/emitiido
def energy_photon(ni, nf):
    Eabsorvida = abs((-13.6/(nf**2)) - (-13.6/(ni**2))) # em eV
    lambda_foton = abs((heV*c) / (Eabsorvida))   # em metros
    frequencia_foton = abs(c / lambda_foton)   
    print(f"A energia do fóton absorvido é: {Eabsorvida:.3f} eV")
    print(f"O comprimento de onda do fóton absorvido é: {lambda_foton:.2e} m")
    print(f"A frequência do fóton absorvido é: {frequencia_foton:.2e} Hz")     # em Hz

def wavelength_photon(ni, nf):
    return (h*c)/energy_photon(ni, nf)

def frequency_photon(ni, nf):
    return energy_photon(ni, nf)/h

# Funções para cálculo do nível inicial ou final na absorção/emissão de fóton pelo átomo de hidrogênio
def absorvido():
        #permita o usuário escolher entre ni ou nf
        while True:
            print("Deseja calcular o nível inicial ou final? (1 - inicial/ 2 - final): ")
            opcao = int(input())
            if opcao == 1:
                n = int(input("Digite o nível inicial: "))
                while True: 
                    print("Você deseja calcular o nível inicial a partir de uma frequência ou de um comprimento de onda? (1 - frequência/ 2 -comprimento de onda): ")
                    opcao = int(input())
                    if opcao == 1:
                        frequencia_foton = float(input("Digite a frequência do fóton em Hz: "))
                        Efinal = -13.6/n ** 2 + heV * frequencia_foton
                        print(f"Efinal: {Efinal:.3f} eV")
                        nf = round((-13.6/Efinal) ** 0.5)
                        print(f"O nível final é: {nf}")
                        break
                    elif opcao == 2:
                        lambda_foton = float(input("Digite o comprimento de onda do fóton em m: "))
                        Efinal = (-13.6/n ** 2) + ((heV*c) / lambda_foton)
                        print(f"Efinal: {Efinal:.3f} eV")
                        nf = round((-13.6/Efinal) ** 0.5)
                        print(f"O nível final é: {nf}")
                        break
                    else:
                        print("Opção inválida!")
                break
            elif opcao == 2:
                n = int(input("Digite o nível final: "))
                while True: 
                    print("Você deseja calcular o nível final a partir de uma frequência ou de um comprimento de onda? (1 - frequência/ 2 -comprimento de onda): ")
                    opcao = int(input())
                    if opcao == 1:
                        frequencia_foton = float(input("Digite a frequência do fóton em Hz: "))
                        Einicial = -13.6/n ** 2 - heV * frequencia_foton
                        print(f"Efinal: {Einicial:.3f} eV")
                        nf = round((-13.6/Einicial) ** 0.5)
                        print(f"O nível final é: {nf}")
                        break
                    elif opcao == 2:
                        lambda_foton = float(input("Digite o comprimento de onda do fóton em m: "))
                        Einicial = (-13.6/n ** 2) - ((heV*c) / lambda_foton)
                        print(f"Efinal: {Einicial:.3f} eV")
                        nf = round((-13.6/Einicial) ** 0.5)
                        print(f"O nível final é: {nf}")
                        break
                    else:
                        print("Opção inválida!")
                break

def emitido():
    #permita o usuário escolher entre ni ou nf
        while True:
            print("Deseja calcular o nível inicial ou final? (1 - inicial/ 2 - final): ")
            opcao = int(input())
            if opcao == 1:
                n = int(input("Digite o nível inicial: "))
                while True: 
                    print("Você deseja calcular o nível inicial a partir de uma frequência ou de um comprimento de onda? (1 - frequência/ 2 -comprimento de onda): ")
                    opcao = int(input())
                    if opcao == 1:
                        frequencia_foton = float(input("Digite a frequência do fóton em Hz: "))
                        Efinal = -13.6/n ** 2 - heV * frequencia_foton
                        print(f"Efinal: {Efinal:.3f} eV")
                        nf = round((-13.6/Efinal) ** 0.5)
                        print(f"O nível final é: {nf}")
                        break
                    elif opcao == 2:
                        lambda_foton = float(input("Digite o comprimento de onda do fóton em m: "))
                        Efinal = (-13.6/n ** 2) - ((heV*c) / lambda_foton)
                        print(f"Efinal: {Efinal:.3f} eV")
                        nf = round((-13.6/Efinal) ** 0.5)
                        print(f"O nível final é: {nf}")
                        break
                    else:
                        print("Opção inválida!")
                break
            elif opcao == 2:
                n = int(input("Digite o nível final: "))
                while True: 
                    print("Você deseja calcular o nível final a partir de uma frequência ou de um comprimento de onda? (1 - frequência/ 2 -comprimento de onda): ")
                    opcao = int(input())
                    if opcao == 1:
                        frequencia_foton = float(input("Digite a frequência do fóton em Hz: "))
                        Einicial = -13.6/n ** 2 + heV * frequencia_foton
                        print(f"Efinal: {Einicial:.3f} eV")
                        nf = round((-13.6/Einicial) ** 0.5)
                        print(f"O nível inicial é: {nf}")
                        break
                    elif opcao == 2:
                        lambda_foton = float(input("Digite o comprimento de onda do fóton em m: "))
                        Einicial = (-13.6/n ** 2) + ((heV*c) / lambda_foton)
                        print(f"Efinal: {Einicial:.3f} eV")
                        nf = round((-13.6/Einicial) ** 0.5)
                        print(f"O nível inicial é: {nf}")
                        break
                    else:
                        print("Opção inválida!")
                break

while True:
    print(" 1 - cálculo de raio, velocidade, comprimento de onda, energia cinética, energia potencial e energia total ")
    print(" 2 - cálculo de energia, comprimento de onda e frequência do fóton absorvido/emitiido ")
    print(" 3 - cálculo do nível na absorção de fóton pelo átomo de hidrogênio ")
    print(" 4 - cálculo do nível na emissão de fóton pelo átomo de hidrogênio ")
    print(" 5 - sair do programa ")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        n = int(input("Digite o nível: "))
        print(f"Raio da órbita do elétron: {radius(n):.2e} m")
        print(f"Velocidade do elétron na órbita: {velocity(n):.2e} m/s")
        print(f"Comprimento de onda de De Broglie do elétron no nível n: {wavelength(n):.2e} m")
        print(f"Energia cinética no nível n: {kinetic_energy(n):.2e} eV")
        print(f"Energia potencial no nível n: {potential_energy(n):.2e} eV")
        print(f"Energia total no nível n: {total_energy(n):.2e} eV")
    elif opcao == 2:
        ni = int(input("Digite o nível inicial: "))
        nf = int(input("Digite o nível final: "))
        energy_photon(ni, nf)
    elif opcao == 3:
        absorvido()
    elif opcao == 4:
        emitido()

    elif opcao == 5:
        break
