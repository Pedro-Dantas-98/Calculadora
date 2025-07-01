import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Usar nan como valor inicial é uma boa prática. 
    Se o operador fornecido não corresponder a nenhuma das opções válidas (+, -, etc.), a função retornará nan, 
    sinalizando que o cálculo não pôde ser realizado.
    """
    result = float("nan")
    
    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2    
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        result = num1 / num2
    elif operador == '^':
        result = num1 ** num2  
                
    return result


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')
            while True:
                selecao = input("Operações disponíveis: \n Adição (+) \n Subtração (-) \n Multiplicação (*) \n Divisão (/) \n Exponenciação (^) \n Introduza o operador da conta que pretende fazer: ") 

                if selecao == "+":
                    print('----------------------------------\n')
                    num1 = int(input("Introduza o primeiro número: "))
                    num2 = int(input("Introduza o segundo número: "))
                    operador = "+"
                    calculadora(num1, num2, operador)
                    


        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')
