from calculadora import Calculadora

calc = Calculadora()

def test_soma():
    assert calc.soma(10, 5) == 15

def test_subtracao():
    assert calc.subtracao(20, 8) == 12

def test_multiplicacao():
    assert calc.multiplicacao(4, 6) == 24

def test_divisao():
    assert calc.divisao(20, 5) == 4

def test_potenciacao():
    assert calc.potenciacao(2, 3) == 8

def test_raiz_quadrada():
    assert calc.raiz_quadrada(25) == 5

def test_seno():
    assert round(calc.seno(90), 2) == 1.0

def test_cosseno():
    assert round(calc.cosseno(0), 2) == 1.0