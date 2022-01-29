from ast import While
from itertools import repeat

print('\nMinha primeira calculadora com Python\n')

# Soma

def soma(x, y):
    return x + y

# Subtração

def subtracao(x, y):
    return x - y

# Divisão

def divisao(x, y):
    return x / y

# Multiplicação

def multiplicacao(x, y):
    return x * y

# Janela de Opções 

print("\nSelecione a operação desejada: \n")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = int(input("\nDigite sua opção (1/2/3/4): "))

while escolha >= 5:

    print('\nEscolha errada!')
    print('\nEscolha um numero entre 1 e 4\n')
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    escolha = int(input("\nDigite sua opção (1/2/3/4): "))

    if escolha == 1:
        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("\nDigite o segundo número: "))
        print ('\n A soma de ', num1, '+', num2, 'é =', soma(num1, num2))

    elif escolha == 2:
        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("\nDigite o segundo número: "))
        print ('\n A subtração de ', num1, '-', num2, 'é =', subtracao(num1, num2))
            
    elif escolha == 3:
        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("\nDigite o segundo número: "))
        print ('\n A multiplicação de ', num1, '*', num2, 'é =', multiplicacao(num1, num2))
        
    elif escolha == 4:
        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("\nDigite o segundo número: "))
        print ('\n A divisão de ', num1, '/', num2, 'é =', int(divisao(num1, num2)))
  
  
      


            



   



    


