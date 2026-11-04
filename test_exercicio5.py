from unittest.mock import patch
from exercicio5 import acessar_sistema

@patch("exercicio5.verificar_permissao", return_value=True)
def test_usuario_com_permissao(mock_permissao):
    assert acessar_sistema("admin") == "Acesso autorizado"

@patch("exercicio5.verificar_permissao", return_value=False)
def test_usuario_sem_permissao(mock_permissao):
    assert acessar_sistema("visitante") == "Acesso negado"

@patch("exercicio5.verificar_permissao", return_value=True)
def test_verificar_permissao_foi_chamada(mock_permissao):
    acessar_sistema("admin")
    mock_permissao.assert_called()

@patch("exercicio5.verificar_permissao", return_value=True)
def test_verificar_permissao_chamada_com_usuario_correto(mock_permissao):
    acessar_sistema("maria")
    mock_permissao.assert_called_once_with("maria")

@patch("exercicio5.verificar_permissao")
def test_mock_simular_dois_cenarios(mock_permissao):
    mock_permissao.return_value = True
    assert acessar_sistema("lucas") == "Acesso autorizado"
    
    mock_permissao.return_value = False
    assert acessar_sistema("pedro") == "Acesso negado"
    #ola