# language: pt

Funcionalidade: Soma
  Como usuário da calculadora científica
  Quero somar dois números
  Para obter o resultado da adição

  Cenário: Somar dois números positivos
    Dado que tenho os números 5 e 3
    Quando eu somo os dois números
    Então o resultado deve ser 8

  Cenário: Somar números negativos
    Dado que tenho os números -5 e -3
    Quando eu somo os dois números
    Então o resultado deve ser -8

  Cenário: Somar número positivo com negativo
    Dado que tenho os números 10 e -4
    Quando eu somo os dois números
    Então o resultado deve ser 6