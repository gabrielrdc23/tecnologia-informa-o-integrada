import diferencadata

def test_diferenca_entre_datas():
    assert diferencadata.diferenca_entre_datas("2024-03-15", "2024-03-20", "dias") == 5
    assert diferencadata.diferenca_entre_datas("2024-03-15", "2025-03-15", "meses") == 12
    assert diferencadata.diferenca_entre_datas("2024-03-15", "2025-03-15", "anos") == 1
    assert abs(diferencadata.diferenca_entre_datas("2024-03-15 12:00", "2024-03-15 14:30", "horas") - 2.5) < 0.01
    assert diferencadata.diferenca_entre_datas("2024-03-15 12:00", "2024-03-15 12:45", "minutos") == 45
