from italian_vip_says import jovanotty, cottanzo, _vip_replace

class TestItalianVipSays():

    def test_capital(self):
        #Jovanotti
        assert 'Faffi' == jovanotty('Sassi')
        assert 'Raffffi' == jovanotty('Razzi')
        #Costanzo
        assert 'Ttate boni' == cottanzo('State boni')
        assert 'Attelio' == cottanzo('Azelio')

    def test_empty(self):
        assert ' ' == jovanotty(' ')
        assert ' ' == cottanzo(' ')

    def test_bestof(self):
        assert 'Ho le tafche piene di faffi e gli occhi pieni di te' == jovanotty('Ho le tasche piene di sassi e gli occhi pieni di te')
        assert 'Tono tettanta giorni che ton qui' == cottanzo('Sono sessanta giorni che son qui')

    def test_error(self):
        assert not 'Sassi' == jovanotty('Sassi')
        assert not 'Sei6' == cottanzo('Sei6')


class TestEngine():

    def test_replace(self):
        test_charmap = {'e': '', 's':'t', 'o': 'u'}
        payload = "Frase creata solo per il test"

        defined_result = "Frat crata tulu pr il ttt"
        replaced = _vip_replace(payload,test_charmap)

        assert defined_result == replaced
