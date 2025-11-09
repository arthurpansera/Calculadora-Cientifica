# language: pt

Funcionalidade: Subtração
  Como usuário da calculadora científica
  Quero subtrair um número de outro
  Para obter a diferença entre eles

  Cenário: Subtrair dois números positivos
    Dado que tenho os números 10 e 3
    Quando eu subtraio o segundo do primeiro
    Então o resultado deve ser 7

  Cenário: Subtrair resultando em número negativo
    Dado que tenho os números 5 e 8
    Quando eu subtraio o segundo do primeiro
    Então o resultado deve ser -3

  Cenário: Subtrair números negativos
    Dado que tenho os números -5 e -3
    Quando eu subtraio o segundo do primeiro
    Então o resultado deve ser -2