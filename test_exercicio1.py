import pytest
from exercicio1 import classificar_produto

def test_produto_sem_estoque():
    assert classificar_produto(0) == "Sem estoque"

def test_produto_estoque_baixo():
    assert classificar_produto(3) == "Estoque baixo"

def test_produto_estoque_normal():
    assert classificar_produto(12) == "Estoque normal"

def test_produto_estoque_alto():
    assert classificar_produto(25) == "Estoque alto"

def test_quantidade_negativa():
    assert classificar_produto(-5) == "Quantidade inválida"

