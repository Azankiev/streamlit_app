import streamlit as st
import pandas as pd

st.header("Meu dashboard")

# Especifique o caminho do arquivo CSV
caminho_arquivo = "C:/Users/vinic/Desktop/app stream/sales_data_sample.csv"

# Abra o arquivo CSV e crie o DataFrame
data_frame = pd.read_csv(caminho_arquivo, encoding='latin1')

st.table(data_frame)


colunas_grafico = ["QUANTITYORDERED", "SALES"]

# Crie o gráfico utilizando as colunas selecionadas
st.line_chart(data_frame[colunas_grafico])
st.bar_chart(data_frame[colunas_grafico])

