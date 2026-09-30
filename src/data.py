"""Carregamento e padronização do dataset *Default of Credit Card Clients*.

Fonte: UCI Machine Learning Repository / Kaggle (uciml/default-of-credit-card-clients-dataset).
Referência: Yeh, I. C.; Lien, C. H. (2009). The comparisons of data mining techniques for the
predictive accuracy of probability of default of credit card clients.
Expert Systems with Applications, 36(2), 2473-2480.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

RAIZ_PROJETO = Path(__file__).resolve().parents[1]
DIR_BRUTO = RAIZ_PROJETO / "data" / "raw"
DIR_INTERIM = RAIZ_PROJETO / "data" / "interim"
DIR_PROCESSADO = RAIZ_PROJETO / "data" / "processed"
DIR_FIGURAS = RAIZ_PROJETO / "reports" / "figures"

ARQUIVO_BRUTO = DIR_BRUTO / "UCI_Credit_Card.csv"

# O arquivo original chama o status de setembro de PAY_0 (e não PAY_1) e usa um nome de alvo com
# pontos; padronizamos ambos para manter a numeração 1..6 consistente entre PAY_*, BILL_AMT* e PAY_AMT*.
RENOMEAR = {"PAY_0": "PAY_1", "default.payment.next.month": "default"}

ALVO = "default"
COL_ID = "ID"
COLS_STATUS = [f"PAY_{i}" for i in range(1, 7)]
COLS_FATURA = [f"BILL_AMT{i}" for i in range(1, 7)]
COLS_PAGAMENTO = [f"PAY_AMT{i}" for i in range(1, 7)]

ROTULOS = {
    "SEX": {1: "Masculino", 2: "Feminino"},
    "EDUCATION": {
        1: "Pós-graduação",
        2: "Universidade",
        3: "Ensino médio",
        4: "Outros",
        5: "Desconhecido (5)",
        6: "Desconhecido (6)",
        0: "Não documentado (0)",
    },
    "MARRIAGE": {1: "Casado(a)", 2: "Solteiro(a)", 3: "Outros", 0: "Não documentado (0)"},
    ALVO: {0: "Adimplente", 1: "Inadimplente"},
}


def carregar_dados_brutos(caminho: Path = ARQUIVO_BRUTO) -> pd.DataFrame:
    """Lê o CSV original, sem nenhuma transformação além da padronização de nomes."""
    return pd.read_csv(caminho).rename(columns=RENOMEAR)
