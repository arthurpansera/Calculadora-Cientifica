# language: pt

Funcionalidade: Divisão
  Como usuário da calculadora científica
  Quero dividir um número por outro
  Para obter o resultado da divisão

  Cenário: Dividir dois números positivos
    Dado que tenho os números 20 e 4
    Quando eu divido o primeiro pelo segundo
    Então o resultado deve ser 5

  Cenário: Dividir resultando em número decimal
    Dado que tenho os números 10 e 3
    Quando eu divido o primeiro pelo segundo
    Então o resultado deve ser aproximadamente 3.33

  Cenário: Dividir por zero
    Dado que tenho os números 10 e 0
    Quando eu tento dividir o primeiro pelo segundo
    Então deve lançar uma exceção de divisão por zero