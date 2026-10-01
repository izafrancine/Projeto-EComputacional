# Inadimplência de clientes de cartão de crédito

Projeto da disciplina de **Estatística Computacional** (UFCA) sobre o dataset *Default of Credit Card Clients* (UCI/Kaggle): 30.000 clientes de um banco de Taiwan, 23 variáveis explicativas e a variável resposta `default` (inadimplência no mês seguinte).

## Como executar

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab notebooks/
```

Os notebooks localizam a raiz do repositório sozinhos, então podem ser abertos de qualquer diretório.

## Estrutura

```
credit-default-analysis/
├── data/
│   ├── raw/          # dado original (versionado, imutável)
│   ├── interim/      # etapas intermediárias (gerado)
│   └── processed/    # bases prontas para modelagem (gerado)
├── notebooks/        # um notebook por etapa, numerados na ordem do curso
├── src/              # código reutilizável importado pelos notebooks
│   ├── data.py         # caminhos, renomeação de colunas, rótulos, carregamento
│   ├── dicionario.py   # dicionário de variáveis (natureza e escala)
│   └── estatistica.py  # tabelas de frequência, Sturges, medidas-resumo
├── reports/figures/  # figuras geradas pelos notebooks
└── docs/             # anotações, enunciados, referências
```

## Notebooks

| Nº | Notebook | Conteúdo | Situação |
|---|---|---|---|
| 01 | `01_descricao_e_analise_univariada.ipynb` | 1.0 Problema, dados e variáveis · 1.1 Análise univariada · 1.2 Gráficos univariados | Concluído |

## Como expandir

- **Novo tópico do curso:** crie `notebooks/NN_nome_do_topico.ipynb` (numeração sequencial) e acrescente uma linha na tabela acima.


## Fonte

Yeh, I. C.; Lien, C. H. (2009). The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients. *Expert Systems with Applications*, 36(2), 2473–2480.
