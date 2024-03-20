import verificador
import unittest

class TestVerificarSenhaSegura(unittest.TestCase):
    def test_comprimento_senha(self):
        self.assertFalse(verificador.verificar_senha_segura("abc12!"))
        self.assertTrue(verificador.verificar_senha_segura("Abc123!@#"))
    
    def test_letra_maiuscula(self):
        self.assertFalse(verificador.verificar_senha_segura("abcdefg123!@#"))
        self.assertTrue(verificador.verificar_senha_segura("Abcdefg123!@#"))
    
    def test_letra_minuscula(self):
        self.assertFalse(verificador.verificar_senha_segura("ABCDEFG123!@#"))
        self.assertTrue(verificador.verificar_senha_segura("Abcdefg123!@#"))
    
    def test_caractere_especial(self):
        self.assertFalse(verificador.verificar_senha_segura("Abcdefg1234"))
        self.assertTrue(verificador.verificar_senha_segura("Abcdefg123!@#"))
    
    def test_senha_vazia(self):
        self.assertFalse(verificador.verificar_senha_segura(""))
    
    def test_senha_curta(self):
        self.assertFalse(verificador.verificar_senha_segura("Abc12!"))

if __name__ == '__main__':
    unittest.main()
