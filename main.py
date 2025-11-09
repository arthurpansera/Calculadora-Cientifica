from calculadora import Calculadora

def main():
    calc = Calculadora()

    while True:
        print("\n=== CALCULADORA CIENTÍFICA ===")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potenciação")
        print("6. Raiz Quadrada")
        print("7. Seno")
        print("8. Cosseno")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao in ('1','2','3','4','5'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == '1':
                print("Resultado: ", calc.soma(num1, num2))

            elif opcao == '2':
                print("Resultado: ", calc.subtracao(num1, num2))

            elif opcao == '3':
                print("Resultado:", calc.multiplicacao(num1, num2))

            elif opcao == '4':
                while num2 == 0:
                    print("Opção inválida! Impossível dividir por 0!")
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                print("Resultado:", calc.divisao(num1, num2))

            elif opcao == '5':
                print("Resultado:", calc.potenciacao(num1, num2))

        elif opcao == '6':
            num = float(input("Digite o número: "))
            print("Resultado:", calc.raiz_quadrada(num))

        elif opcao == '7':
            ang = float(input("Digite o ângulo (em graus): "))
            print("Resultado:", calc.seno(ang))

        elif opcao == '8':
            ang = float(input("Digite o ângulo (em graus): "))
            print("Resultado:", calc.cosseno(ang))

        elif opcao == '0':
            print("Saindo...")
            break

        else:
            print("Escolha inválida! Escolha uma das opções.")

main()