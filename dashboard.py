import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Customer Support Intelligence Platform', layout='wide')

@st.cache_data
def load_data():
    return pd.read_csv('data/support_tickets.csv', parse_dates=['created_at'])

df = load_data()

st.title('Customer Support Intelligence Platform')
st.caption('Analytics + IA + automação para operação de atendimento')

st.sidebar.header('Filtros')
regions = st.sidebar.multiselect('Região', sorted(df['region'].unique()), default=sorted(df['region'].unique()))
channels = st.sidebar.multiselect('Canal', sorted(df['channel'].unique()), default=sorted(df['channel'].unique()))
categories = st.sidebar.multiselect('Categoria', sorted(df['category'].unique()), default=sorted(df['category'].unique()))

filtered = df[df['region'].isin(regions) & df['channel'].isin(channels) & df['category'].isin(categories)].copy()

k1, k2, k3, k4, k5 = st.columns(5)
k1.metric('Tickets', f"{len(filtered):,}")
k2.metric('FRT médio (min)', round(filtered['first_response_time_min'].mean(), 1))
k3.metric('Tempo resolução (h)', round(filtered['resolution_time_hours'].mean(), 1))
k4.metric('CSAT médio', round(filtered['csat_score'].mean(), 2))
k5.metric('SLA breach %', f"{round(filtered['sla_breached'].mean()*100, 1)}%")

daily = filtered.groupby(filtered['created_at'].dt.date).size().reset_index(name='tickets')
fig_daily = px.line(daily, x='created_at', y='tickets', title='Volume de tickets por dia')
cat = filtered.groupby('category', as_index=False).agg(
    tickets=('ticket_id', 'count'),
    frt=('first_response_time_min', 'mean'),
    resolution=('resolution_time_hours', 'mean'),
    csat=('csat_score', 'mean')
).sort_values('tickets', ascending=False)
fig_cat = px.bar(cat, x='category', y='tickets', title='Tickets por categoria')
fig_channel = px.bar(filtered.groupby('channel', as_index=False).size(), x='channel', y='size', title='Volume por canal')
fig_region = px.bar(filtered.groupby('region', as_index=False).size(), x='region', y='size', title='Volume por região')

c1, c2 = st.columns(2)
c1.plotly_chart(fig_daily, use_container_width=True)
c2.plotly_chart(fig_cat, use_container_width=True)
c3, c4 = st.columns(2)
c3.plotly_chart(fig_channel, use_container_width=True)
c4.plotly_chart(fig_region, use_container_width=True)

st.subheader('Tabela de categorias')
st.dataframe(cat, use_container_width=True)

worst = cat.sort_values(['resolution', 'tickets'], ascending=[False, False]).head(1)
if not worst.empty:
    row = worst.iloc[0]
    st.info(
        f"A categoria com maior tempo médio de resolução é **{row['category']}** ({row['resolution']:.1f}h). "
        f"Recomenda-se revisar fluxo operacional, priorização e volume por canal para reduzir impacto no SLA."
    )
