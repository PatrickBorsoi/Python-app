import streamlit as st
import pandas as pd
import pandas_datareader.data as web
import numpy as numpy
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import yfinance as yf
yf.pdr_override()

st.sidebar.title('Menu')

#Lista das empresas - ticket b3
Empresas = ['PETR4.SA', 'AMER3.SA']
Selecao = st.sidebar.selectbox('Selecione a empresa:', Empresas);
#Range de seleção
#                                             mes inicio, mes final, pulando de 1 em 1
Range = st.sidebar.slider('Periodo de meses', 0,12,1, key='Barra_selecao')
# coloco mo para o yfinance entender q queremos por mes
Selecao_Range = str(Range) + 'mo'

#Colunas
col1, col2 = st.columns([0.9, 0.1])

#Imagens
Imagens = [
    'https://files.tecnoblog.net/wp-content/uploads/2022/02/logo-americanas.png',
    'https://seeklogo.com/images/P/Petrobras-logo-03DABEE0AC-seeklogo.com.png'
]

#Titulo
Titulo = f'Análise econômica {str(Selecao)}'
col1.title(Titulo)

if Selecao == 'AMER3.SA':
    col2.image(Imagens[0], width=70) 
else:
    col2.image(Imagens[1], width=70) 

# Coletar dados da API do yahoo
Dados = web.get_data_yahoo(Selecao , period=Selecao_Range)

Grafico_Candlestick = go.Figure(
    data=[
        go.Candlestick(
            x=Dados.index,
            open=Dados['Open'],
            high=Dados['High'],
            low=Dados['Low'],
            close=Dados['Close'],
        )
    ]

)
Grafico_Candlestick.update_layout(
    xaxis_rangeslider_visible=False,
    title='Análise das ações',
    xaxis_title='Período',
    yaxis_title='Preço'
)

#Mostrar o gráfico do plotly no streamlit
st.plotly_chart(Grafico_Candlestick)

#Condição
if st.checkbox('Mostrar dados em tabela'): 
    st.subheader('Tabela de registros')
    st.write(Dados)


