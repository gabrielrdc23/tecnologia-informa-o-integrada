import contador

def test_contador_palavras():
    assert contador.contar_palavras("Isso é uma frase de exemplo") == 6
    assert contador.contar_palavras("Apenas uma palavra") == 3

test_contador_palavras()  
