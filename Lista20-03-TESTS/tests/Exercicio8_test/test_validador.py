import validador

def test_validador_telefone():
    assert validador.validar_telefone("(12) 1234-5678") == True
    assert validador.validar_telefone("(12) 12345-6789") == True
    assert validador.validar_telefone("12 1234-5678") == False
    assert validador.validar_telefone("(123) 1234-5678") == False
    assert validador.validar_telefone("(12) 12345-678") == False