# language: pt

Funcionalidade: Seno
  Como usuário da calculadora científica
  Quero calcular o seno de um ângulo
  Para obter seu valor trigonométrico

  Cenário: Calcular seno de 0 graus
    Dado que tenho o ângulo 0 graus
    Quando eu calculo o seno
    Então o resultado deve ser 0

  Cenário: Calcular seno de 90 graus
    Dado que tenho o ângulo 90 graus
    Quando eu calculo o seno
    Então o resultado deve ser 1

  Cenário: Calcular seno de 30 graus
    Dado que tenho o ângulo 30 graus
    Quando eu calculo o seno
    Então o resultado deve ser aproximadamente 0.5