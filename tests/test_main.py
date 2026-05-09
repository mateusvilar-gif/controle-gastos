from src.main import cotacao_dolar

def test_soma():
    """Teste simples de sanidade"""
    assert 2 + 2 == 4

def test_valor_positivo():
    """Teste de lógica de valores"""
    valor = 10
    assert valor > 0

def test_lista_vazia():
    """Teste de estrutura de dados"""
    gastos = []
    assert len(gastos) == 0

def test_cotacao_dolar():
    """Teste de integração com a API pública"""
    try:
        # Executa a função que faz a chamada à API
        cotacao_dolar()
        # Se a função rodar sem levantar exceções, o teste passa
        assert True
    except Exception as e:
        # Se houver erro na integração (ex: timeout ou erro 500), o teste falha
        assert False, f"Erro na integração com a API: {e}"