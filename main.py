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
        print(f"\n{num1} + {num2} = {result}")
        print('----------------------------------')
    elif operador == '-':
        result = num1 - num2
        print(f"\n{num1} - {num2} = {result}")
        print('----------------------------------')    
    elif operador == '*':
        result = num1 * num2
        print(f"\n{num1} x {num2} = {result}")
        print('----------------------------------')
    elif operador == '/':
        result = num1 / num2
        print(f"\n{num1} ÷ {num2} = {result}")
        print('----------------------------------')
    elif operador == '^':
        result = num1 ** num2
        print(f"\n{num1}^{num2} = {result}")
        print('----------------------------------')          
                
    return result


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------')
            while True:
                selecao = input("Operações disponíveis: \n\n Soma (+) \n Subtração (-) \n Multiplicação (*) \n Divisão (/) \n Exponenciação (^) \n\n Introduza o operador da conta que pretende fazer: ") 

                if selecao == "+":
                    print('----------------------------------')
                    num1 = float(input("Introduza o primeiro número: "))
                    num2 = float(input("Introduza o segundo número: "))
                    operador = selecao
                    calculadora(num1, num2, operador)
                elif selecao == "-":
                    print('----------------------------------')
                    num1 = float(input("Introduza o primeiro número: "))
                    num2 = float(input("Introduza o segundo número: "))
                    operador = selecao
                    calculadora(num1, num2, operador)
                elif selecao == "*":
                    print('----------------------------------')
                    num1 = float(input("Introduza o primeiro número: "))
                    num2 = float(input("Introduza o segundo número: "))
                    operador = selecao
                    calculadora(num1, num2, operador)                                        
                elif selecao == "/":
                    print('----------------------------------')
                    num1 = float(input("Introduza o primeiro número: "))
                    num2 = float(input("Introduza o segundo número: "))
                    operador = selecao
                    calculadora(num1, num2, operador)
                elif selecao == "^":
                    print('----------------------------------')
                    num1 = float(input("Introduza o primeiro número: "))
                    num2 = float(input("Introduza o segundo número: "))
                    operador = selecao
                    calculadora(num1, num2, operador)
                else:
                    print('----------------------------------')
                    print("Operação inválida.")
                    print('----------------------------------')                                                                    
        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)
            
        encerro = input("Pretende efetuar outras operações? (S/N): ").lower()
            
        if encerro == "s":
            print("A resumir o programa.")
        else:
            break
            
    print('\nVolte sempre!\n')
