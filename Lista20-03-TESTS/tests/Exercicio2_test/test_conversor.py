import conversor

def test_conversor_moedas():
    assert round(conversor.usd_para_euro(100), 2) == 84.00
    assert round(conversor.real_para_usd(100), 2) == 18.00

