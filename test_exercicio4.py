from unittest.mock import patch
from exercicio4 import criar_identificacao

@patch("exercicio4.gerar_codigo", return_value="USR-1234")
def test_mensagem_gerada_corretamente(mock_gerar_codigo):
    resultado = criar_identificacao("Carlos")
    assert resultado == "Usuário Carlos cadastrado com código USR-1234."

@patch("exercicio4.gerar_codigo", return_value="USR-1234")
def test_gerar_codigo_foi_chamada(mock_gerar_codigo):
    criar_identificacao("Carlos")
    mock_gerar_codigo.assert_called()

@patch("exercicio4.gerar_codigo", return_value="USR-1234")
def test_gerar_codigo_chamada_apenas_uma_vez(mock_gerar_codigo):
    criar_identificacao("Carlos")
    mock_gerar_codigo.assert_called_once()

@patch("exercicio4.gerar_codigo", return_value="USR-9999")
def test_mock_simular_diferentes_codigos(mock_gerar_codigo):
    resultado = criar_identificacao("Ana")
    assert resultado == "Usuário Ana cadastrado com código USR-9999."

@patch("exercicio4.gerar_codigo", return_value="USR-5555")
def test_comportamento_nomes_diferentes(mock_gerar_codigo):
    assert criar_identificacao("Beatriz") == "Usuário Beatriz cadastrado com código USR-5555."
    assert criar_identificacao("João") == "Usuário João cadastrado com código USR-5555."