# language: pt

Funcionalidade: Raiz Quadrada
  Como usuário da calculadora científica
  Quero calcular a raiz quadrada de um número
  Para obter seu valor aproximado

  Cenário: Calcular raiz quadrada de número positivo
    Dado que tenho o número 16
    Quando eu calculo a raiz quadrada
    Então o resultado deve ser 4

  Cenário: Calcular raiz quadrada de zero
    Dado que tenho o número 0
    Quando eu calculo a raiz quadrada
    Então o resultado deve ser 0

  Cenário: Calcular raiz quadrada de número negativo
    Dado que tenho o número -4
    Quando eu tento calcular a raiz quadrada
    Então deve lançar uma exceção de valor inválido