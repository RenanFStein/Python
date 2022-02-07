def soma (x,y):
    return (x + y)


def subtracao (x,y):
    return(x - y)

        
def divisao (x,y):
    return(x / y)

        
def multiplicacao (x,y):
    return(x * y)
    
def sobra (x,y):
    return (x % y)

escolha = ()

while escolha  != '0' or escolha != '1' or escolha != '2' or escolha != '3' or escolha != '4' or escolha != '4' or escolha != '5':
    print(' \n')   
    print(' ________Calculadora__________')
    print('|    Escolha Entre 0 a 5      |')
    print('|    1 - Somar                |')
    print('|    2 - Subtrair             |')
    print('|    3 - Dividir              |')
    print('|    4 - Multiplicar          |')
    print('|    5 - Sobra da Divisão     |')
    print('|    0 - Sair                 |')
    print('|_____________________________|')
    escolha = (input('Escolha o Calculo:'))

    if escolha == '1':
        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("\nDigite o segundo número: "))
        print ('\n A soma de ', num1, '+', num2, 'é =', soma(num1, num2))

    elif escolha == '2':
        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("\nDigite o segundo número: "))
        print ('\n A subtração de ', num1, '-', num2, 'é =', subtracao(num1, num2))
            
    elif escolha == '3':
        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("\nDigite o segundo número: "))
        print ('\n A multiplicação de ', num1, '*', num2, 'é =', divisao(num1, num2))
        
    elif escolha == '4':
        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("\nDigite o segundo número: "))
        print ('\n A divisão de ', num1, '/', num2, 'é =', int(multiplicacao(num1, num2)))

    elif escolha == '5':
        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("\nDigite o segundo número: "))
        print ('\n A sobra da divisão', num1, '/', num2, 'é =', int(sobra(num1, num2)))

    elif escolha == '0':       
        print ('Obrigado e Volte Sempre' )
        break
      


            



   



    


