# language: pt

from behave import given, when, then
from calculadora import Calculadora

calc = Calculadora()

# GIVEN (dados iniciais)

@given('que tenho os números {a:d} e {b:d}')
def step_dados(context, a, b):
    context.a = a
    context.b = b

@given('que tenho a base {a:d} e o expoente {b:d}')
def step_base_expoente(context, a, b):
    context.a = a
    context.b = b

@given('que tenho o número {a:d}')
def step_numero(context, a):
    context.a = a

@given('que tenho o ângulo {a:d} graus')
def step_angulo(context, a):
    context.a = a

# WHEN (ações do usuário)

@when('eu somo os dois números')
def step_soma(context):
    context.resultado = calc.soma(context.a, context.b)

@when('eu subtraio o segundo do primeiro')
def step_subtrai(context):
    context.resultado = calc.subtracao(context.a, context.b)

@when('eu multiplico os dois números')
def step_multiplica(context):
    context.resultado = calc.multiplicacao(context.a, context.b)

@when('eu divido o primeiro pelo segundo')
def step_divide(context):
    context.resultado = calc.divisao(context.a, context.b)

@when('eu calculo a potência')
def step_potencia(context):
    context.resultado = calc.potenciacao(context.a, context.b)

@when('eu calculo a raiz quadrada')
def step_raiz(context):
    context.resultado = calc.raiz_quadrada(context.a)

@when('eu calculo o seno')
def step_seno(context):
    context.resultado = round(calc.seno(context.a), 2)

@when('eu calculo o cosseno')
def step_cosseno(context):
    context.resultado = round(calc.cosseno(context.a), 2)

# THEN (resultado esperado)

@then('o resultado deve ser {esperado:g}')
def step_resultado(context, esperado):
    assert round(context.resultado, 2) == round(esperado, 2)