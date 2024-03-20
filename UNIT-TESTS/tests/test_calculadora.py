import calculadora

def test_soma_inteiros():
    resultado = calculadora.soma(1, 2) 
    assert resultado == 3

def test_soma_invalido():
    assert calculadora.soma('2', 1 ) == 'Erro'        
        
        
        
