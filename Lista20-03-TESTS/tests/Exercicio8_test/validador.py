import re

def validar_telefone(numero):
    if re.match(r'^\(\d{2}\) \d{4,5}-\d{4}$', numero):
        return True
    else:
        return False