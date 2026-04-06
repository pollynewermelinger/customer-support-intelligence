# Customer Support Intelligence Platform

Projeto de portfólio com foco em Analytics + IA + automação, simulando um cenário real de operação de atendimento para uma empresa global de hospitalidade.

## Objetivo
Construir uma solução end-to-end que:
- consolida dados de tickets
- gera KPIs operacionais
- identifica gargalos por categoria, canal e região
- cria uma camada de insights automatizados
- entrega visualização executiva para tomada de decisão

## Stack
- Python
- Pandas / NumPy
- Plotly
- Streamlit
- SQL (conceitualmente no pipeline)
- LLM-ready workflow (simulação de camada de IA para classificação e resumo)

## Estrutura
- data/support_tickets.csv: base sintética com 1.200 tickets
- scripts/etl.py: pipeline simples para geração de métricas
- app/dashboard.py: dashboard interativo em Streamlit
- dashboard.html: versão estática do dashboard

## Como rodar
pip install -r requirements.txt
streamlit run app/dashboard.py
