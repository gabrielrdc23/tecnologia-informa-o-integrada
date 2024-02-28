import re

def validar_senha(senha):
    if len(senha) < 6 or len(senha) > 32:
        return False
    if not re.search(r'[A-Z]', senha) or not re.search(r'[a-z]', senha) or not re.search(r'\d', senha):
        return False
    if not senha.isalnum():
        return False
    return True

while True:
    try:
        senha = input().strip()
        if validar_senha(senha):
            print("Senha valida.")
        else:
            print("Senha invalida.")
    except EOFError:
        break