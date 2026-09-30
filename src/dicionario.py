"""Dicionário de variáveis: descrição, natureza e escala de medida de cada coluna."""
from __future__ import annotations

import pandas as pd

MESES = ["setembro", "agosto", "julho", "junho", "maio", "abril"]  # índice 1..6 -> mês (2005)


def _linhas() -> list[dict]:
    L = [
        ("ID", "Identificador do cliente", "Identificador (não analítica)", "—", "1 a 30000"),
        ("LIMIT_BAL", "Limite de crédito concedido (inclui crédito familiar/suplementar)",
         "Quantitativa contínua", "Razão", "Dólares taiwaneses (NT$)"),
        ("SEX", "Sexo", "Qualitativa nominal", "Nominal", "1 = masculino; 2 = feminino"),
        ("EDUCATION", "Escolaridade", "Qualitativa ordinal", "Ordinal",
         "1 = pós-graduação; 2 = universidade; 3 = ensino médio; 4 = outros; 5, 6 = desconhecido"),
        ("MARRIAGE", "Estado civil", "Qualitativa nominal", "Nominal",
         "1 = casado(a); 2 = solteiro(a); 3 = outros"),
        ("AGE", "Idade", "Quantitativa discreta", "Razão", "Anos completos"),
    ]
    for i, mes in enumerate(MESES, start=1):
        L.append((
            f"PAY_{i}", f"Status de pagamento em {mes}/2005", "Qualitativa ordinal", "Ordinal",
            "-1 = pago em dia; 1..9 = meses de atraso (–2 e 0 aparecem nos dados sem documentação)"))
    for i, mes in enumerate(MESES, start=1):
        L.append((f"BILL_AMT{i}", f"Valor da fatura em {mes}/2005", "Quantitativa contínua",
                  "Razão*", "NT$ (pode ser negativo)"))
    for i, mes in enumerate(MESES, start=1):
        L.append((f"PAY_AMT{i}", f"Valor pago em {mes}/2005", "Quantitativa contínua", "Razão", "NT$"))
    L.append(("default", "Inadimplência no mês seguinte (outubro/2005) — variável resposta",
              "Qualitativa nominal (binária)", "Nominal", "0 = não; 1 = sim"))
    return [dict(zip(["variavel", "descricao", "natureza", "escala", "dominio_unidade"], t)) for t in L]


def dicionario() -> pd.DataFrame:
    """Retorna o dicionário de variáveis como DataFrame indexado pelo nome da coluna."""
    return pd.DataFrame(_linhas()).set_index("variavel")
