# Importando unittest
import unittest
# Importando o arquivo com o script que será testado
import script


# Esse teste irá verificar se o retorna da função 'saudacao' é 'hello world'
class testSaudacao(unittest.TestCase):

    def test_return(self):
        mensagem = script.saudacao()
        self.assertEqual(mensagem.lower().split(), ['hello', 'world'])


if __name__ == '__main__':
    unittest.main()
