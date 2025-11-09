# language: pt

Funcionalidade: Potenciação
  Como usuário da calculadora científica
  Quero elevar um número a uma potência
  Para calcular seu resultado exponencial

  Cenário: Elevar número a potência positiva
    Dado que tenho a base 2 e o expoente 3
    Quando eu calculo a potência
    Então o resultado deve ser 8

  Cenário: Elevar número a potência zero
    Dado que tenho a base 5 e o expoente 0
    Quando eu calculo a potência
    Então o resultado deve ser 1

  Cenário: Elevar número a potência negativa
    Dado que tenho a base 2 e o expoente -2
    Quando eu calculo a potência
    Então o resultado deve ser 0.25