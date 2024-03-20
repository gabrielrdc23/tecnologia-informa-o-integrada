import calculadora

def test_calculadora():
    assert calculadora.adicao(1, 2) == 3
    assert calculadora.subtracao(5, 2) == 3
    assert calculadora.multiplicacao(2, 3) == 6
    assert calculadora.divisao(6, 3) == 2
    assert calculadora.divisao(10, 2) == 5

  
