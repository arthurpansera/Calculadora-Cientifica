# language: pt

Funcionalidade: Cosseno
  Como usuário da calculadora científica
  Quero calcular o cosseno de um ângulo
  Para obter seu valor trigonométrico

  Cenário: Calcular cosseno de 0 graus
    Dado que tenho o ângulo 0 graus
    Quando eu calculo o cosseno
    Então o resultado deve ser 1

  Cenário: Calcular cosseno de 90 graus
    Dado que tenho o ângulo 90 graus
    Quando eu calculo o cosseno
    Então o resultado deve ser 0

  Cenário: Calcular cosseno de 60 graus
    Dado que tenho o ângulo 60 graus
    Quando eu calculo o cosseno
    Então o resultado deve ser aproximadamente 0.5