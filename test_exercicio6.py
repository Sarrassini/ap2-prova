from unittest.mock import patch
from exercicio6 import atender_proximo_cliente

@patch("exercicio6.registrar_atendimento", return_value=True)
@patch("exercicio6.obter_proximo_cliente", return_value="Carlos")
def test_atendimento_realizado_sucesso(mock_obter, mock_registrar):
    assert atender_proximo_cliente() == "Atendimento realizado"

@patch("exercicio6.registrar_atendimento")
@patch("exercicio6.obter_proximo_cliente", return_value=None)
def test_fila_vazia(mock_obter, mock_registrar):
    assert atender_proximo_cliente() == "Fila vazia"

@patch("exercicio6.registrar_atendimento", return_value=False)
@patch("exercicio6.obter_proximo_cliente", return_value="Carlos")
def test_falha_ao_registrar_atendimento(mock_obter, mock_registrar):
    assert atender_proximo_cliente() == "Falha no atendimento"

@patch("exercicio6.registrar_atendimento")
@patch("exercicio6.obter_proximo_cliente", return_value="Carlos")
def test_obter_proximo_cliente_foi_chamada(mock_obter, mock_registrar):
    atender_proximo_cliente()
    mock_obter.assert_called_once()

@patch("exercicio6.registrar_atendimento", return_value=True)
@patch("exercicio6.obter_proximo_cliente", return_value="Mariana")
def test_registrar_atendimento_chamado_com_cliente_correto(mock_obter, mock_registrar):
    atender_proximo_cliente()
    mock_registrar.assert_called_once_with("Mariana")

@patch("exercicio6.registrar_atendimento")
@patch("exercicio6.obter_proximo_cliente", return_value=None)
def test_registrar_atendimento_nao_chamado_quando_fila_vazia(mock_obter, mock_registrar):
    atender_proximo_cliente()
    mock_registrar.assert_not_called()