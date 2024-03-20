import ordenacao

def test_ordenar_lista():
    assert ordenacao.ordenar_lista([3, 1, 2]) == [1, 2, 3]
    assert ordenacao.ordenar_lista([3, 1, 2], ascendente=False) == [3, 2, 1]

test_ordenar_lista()