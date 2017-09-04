from italian_vip_says import jovanotty, cottanzo, _vip_replace
import unittest

class ItalianVipSaysTestCase(unittest.TestCase):

    def test_capital(self):
        #Jovanotti
        self.assertEqual('Faffi', jovanotty('Sassi'))
        self.assertEqual('Raffffi', jovanotty('Razzi'))
        #Costanzo
        self.assertEqual('Ttate boni', cottanzo('State boni'))
        self.assertEqual('Attelio', cottanzo('Azelio'))

    def test_empty(self):
        self.assertEqual(' ', jovanotty(' '))
        self.assertEqual(' ', cottanzo(' '))

    def test_bestof(self):
        self.assertEqual('Ho le tafche piene di faffi e gli occhi pieni di te', jovanotty('Ho le tasche piene di sassi e gli occhi pieni di te'))
        self.assertEqual('Tono tettanta giorni che ton qui', cottanzo('Sono sessanta giorni che son qui'))

    def test_error(self):
        self.assertNotEqual('Sassi',jovanotty('Sassi'))
        self.assertNotEqual('Sei6',cottanzo('Sei6'))

class EngineTestCase(unittest.TestCase):

    def test_replace(self):
        test_charmap = {'e': '', 's':'t', 'o': 'u'}
        payload = "Frase creata solo per il test"

        defined_result = "Frat crata tulu pr il ttt"
        replaced = _vip_replace(payload,test_charmap)

        self.assertEqual(defined_result,replaced)


if __name__ == '__main__':
    unittest.main()
