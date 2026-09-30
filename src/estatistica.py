"""Funções de estatística descritiva reutilizáveis (tabelas de frequência e medidas-resumo)."""
from __future__ import annotations

import math

import numpy as np
import pandas as pd


def tabela_frequencia_qualitativa(serie: pd.Series, ordem=None, rotulos: dict | None = None) -> pd.DataFrame:
    """Distribuição de frequências de uma variável qualitativa.

    Colunas: frequência absoluta (fi), relativa (fr), relativa em % e acumuladas (Fi, Fr %).
    `ordem` define a sequência das categorias (relevante para variáveis ordinais);
    a acumulada só tem interpretação estrita quando a sequência é uma ordem natural.
    """
    fi = serie.value_counts()
    if ordem is not None:
        fi = fi.reindex(ordem, fill_value=0)
    else:
        fi = fi.sort_index()
    tab = pd.DataFrame({"fi": fi})
    tab["fr"] = tab["fi"] / tab["fi"].sum()
    tab["fr_%"] = (tab["fr"] * 100).round(2)
    tab["Fi"] = tab["fi"].cumsum()
    tab["Fr_%"] = (tab["fr"].cumsum() * 100).round(2)
    if rotulos:
        tab.index = [rotulos.get(i, i) for i in tab.index]
    tab.index.name = serie.name
    return tab


def regra_de_sturges(n: int) -> int:
    """Número de classes pela regra de Sturges, k = 1 + 3,322·log10(n), arredondado."""
    return round(1 + 3.322 * math.log10(n))


def limites_de_classe(serie: pd.Series, k: int | None = None, arredondar_para: float = 1.0) -> np.ndarray:
    """Limites de classes de mesma amplitude.

    A amplitude é h = ceil(R / k), arredondada para cima ao múltiplo de `arredondar_para`
    (para obter limites 'redondos'). Classes fechadas à esquerda: [li, ls).
    """
    k = k or regra_de_sturges(len(serie))
    amplitude_total = serie.max() - serie.min()
    h = math.ceil(amplitude_total / k / arredondar_para) * arredondar_para
    n_classes = math.ceil(amplitude_total / h) + (1 if amplitude_total % h == 0 else 0)
    return serie.min() + h * np.arange(n_classes + 1)


def tabela_frequencia_quantitativa(serie: pd.Series, limites: np.ndarray) -> pd.DataFrame:
    """Distribuição de frequências por classes: fi, fr, Fi, Fr e ponto médio de cada classe."""
    classes = pd.cut(serie, bins=limites, right=False)
    fi = classes.value_counts().sort_index()
    tab = pd.DataFrame({"fi": fi.values}, index=fi.index.astype(str))
    tab["ponto_medio"] = (limites[:-1] + limites[1:]) / 2
    tab["fr"] = tab["fi"] / tab["fi"].sum()
    tab["fr_%"] = (tab["fr"] * 100).round(2)
    tab["Fi"] = tab["fi"].cumsum()
    tab["Fr_%"] = (tab["fr"].cumsum() * 100).round(2)
    tab.index.name = f"classe de {serie.name}"
    return tab


def medidas_resumo(serie: pd.Series) -> pd.Series:
    """Medidas de posição, dispersão e forma de uma variável quantitativa."""
    q1, q2, q3 = serie.quantile([0.25, 0.5, 0.75])
    iqr = q3 - q1
    lim_inf, lim_sup = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    return pd.Series({
        "n": serie.count(),
        "mínimo": serie.min(),
        "Q1": q1,
        "mediana": q2,
        "média": serie.mean(),
        "moda": serie.mode().iloc[0],
        "Q3": q3,
        "máximo": serie.max(),
        "amplitude": serie.max() - serie.min(),
        "amplitude interquartil (IQR)": iqr,
        "desvio-padrão": serie.std(),
        "coeficiente de variação": serie.std() / serie.mean(),
        "assimetria": serie.skew(),
        "curtose (excesso)": serie.kurt(),
        "cerca superior (Q3+1,5·IQR)": lim_sup,
        "n de outliers (Tukey)": int(((serie < lim_inf) | (serie > lim_sup)).sum()),
    })
