import passagens

def test_sistema_reservas():
    sistema = passagens.SistemaReservas()
    sistema.adicionar_voo("123", 100)
    assert sistema.realizar_reserva("123", 3) == True
    assert sistema.visualizar_reservas("123") == 3
    assert sistema.cancelar_reserva("123", 2) == True
    assert sistema.visualizar_reservas("123") == 1
    assert sistema.cancelar_reserva("123", 2) == False  
    assert sistema.cancelar_reserva("456", 2) == False  

test_sistema_reservas()
