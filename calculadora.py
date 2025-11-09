import math

class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Não é possível dividir por zero!"

    def potenciacao(self, a, b):
        return a ** b

    def raiz_quadrada(self, a):
        if a >= 0:
            return math.sqrt(a)
        else:
            return "Número negativo não possui raiz real!"

    def seno(self, angulo_graus):
        return math.sin(math.radians(angulo_graus))

    def cosseno(self, angulo_graus):
        return math.cos(math.radians(angulo_graus))