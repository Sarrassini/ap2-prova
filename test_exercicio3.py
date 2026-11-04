from exercicio3 import validar_documento

def test_documento_11_digitos():
    assert validar_documento("12345678900") is True

def test_documento_formatado():
    assert validar_documento("123.456.789-00") is True

def test_documento_menos_11_digitos():
    assert validar_documento("123456789") is False

def test_documento_mais_11_digitos():
    assert validar_documento("123456789001") is False

def test_documento_com_letras():
    assert validar_documento("1234567890a") is False

def test_documento_vazio():
    assert validar_documento("") is False