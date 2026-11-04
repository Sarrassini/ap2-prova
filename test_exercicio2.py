from exercicio2 import inverter_palavras

def test_frase_varias_palavras():
    assert inverter_palavras("Python é muito interessante") == "interessante muito é Python"

def test_frase_uma_palavra():
    assert inverter_palavras("Python") == "Python"

def test_frase_vazia():
    assert inverter_palavras("") == ""

def test_frase_espacos_extras():
    assert inverter_palavras("  Python   é  muito  ") == "muito é Python"

def test_frase_numeros_e_letras():
    assert inverter_palavras("Teste 123 456 ok") == "ok 456 123 Teste"