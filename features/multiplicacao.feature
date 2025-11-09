# language: pt

Funcionalidade: Multiplicação
  Como usuário da calculadora científica
  Quero multiplicar dois números
  Para obter o produto deles

  Cenário: Multiplicar dois números positivos
    Dado que tenho os números 4 e 5
    Quando eu multiplico os dois números
    Então o resultado deve ser 20

  Cenário: Multiplicar por zero
    Dado que tenho os números 7 e 0
    Quando eu multiplico os dois números
    Então o resultado deve ser 0

  Cenário: Multiplicar números negativos
    Dado que tenho os números -3 e -4
    Quando eu multiplico os dois números
    Então o resultado deve ser 12