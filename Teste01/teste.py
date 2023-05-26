# Importando unittest
import unittest
# Importando o arquivo com o script que será testado
import script


# Esse teste irá verificar se o retorna da função 'saudacao' é 'hello world'
class TestStringMethods(unittest.TestCase):

    def test_string(self):
        mensagem = script.saudacao()
        self.assertEqual(mensagem.lower().split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            mensagem.split(2)


if __name__ == '__main__':
    unittest.main()
