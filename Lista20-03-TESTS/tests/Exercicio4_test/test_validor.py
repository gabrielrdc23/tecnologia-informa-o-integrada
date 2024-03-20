import validor

def test_validador_email():
    assert validor.validar_email("usuario@example.com") == True
    assert validor.validar_email("usuario.example.com") == False
    assert validor.validar_email("usuario@example") == False
    assert validor.validar_email("usuario@example.") == False

test_validador_email()