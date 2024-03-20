import re

def verificar_senha_segura(senha):
    """
    Verifica se a senha atende aos critérios de segurança:
    - Pelo menos 8 caracteres de comprimento
    - Pelo menos uma letra maiúscula
    - Pelo menos uma letra minúscula
    - Pelo menos um caractere especial
    """
    if len(senha) < 8:
        return False
    
    if not re.search("[a-z]", senha):
        return False
    
    if not re.search("[A-Z]", senha):
        return False
    
    if not re.search("[!@#$%^&*()_+{}:<>?]", senha):
        return False
    
    return True
