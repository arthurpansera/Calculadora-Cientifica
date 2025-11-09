import math

class Calculadora:
    def soma(a, b):
        return a + b

    def subtracao(a, b):
        return a - b

    def multiplicacao(a, b):
        return a * b

    def divisao(a, b):
        if b != 0:
            return a / b
        else:
            return "Não é possível dividir por zero!"

    def potenciacao(a, b):
        return a ** b

    def raiz_quadrada(a):
        if a > 0:
            return math.sqrt(a)
        else:
            return "Número negativo não possui raiz real!"

    def seno(angulo_graus):
        return math.sin(math.radians(angulo_graus))

    def cosseno(angulo_graus):
        return math.cos(math.radians(angulo_graus))