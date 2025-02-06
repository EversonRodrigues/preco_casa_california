import geopandas as gpd
import numpy as np
import pandas as pd
import streamlit as st

from joblib import load
from notebooks.src.config import DADOS_GEO_MEDIAN, DADOS_LIMPOS, MODELO_FINAL

# Função para carregar dados limpos com cache
@st.cache_data
def carregar_dados_limpos():
    return pd.read_parquet(DADOS_LIMPOS)

# Função para carregar dados geoespaciais com cache
@st.cache_data
def carregar_dados_geo():
    return gpd.read_parquet(DADOS_GEO_MEDIAN)

# Função para carregar o modelo treinado com cache
@st.cache_resource
def carregar_modelo():
    return load(MODELO_FINAL)

# Chamar corretamente as funções de carregamento
df = carregar_dados_limpos()
gdf_geo = carregar_dados_geo()
modelo = carregar_modelo()

# Título do aplicativo
st.title("Previsão de preços de imóveis")

# Entradas do usuário
longitude = st.number_input("longitude", value=-122.33)
latitude = st.number_input("latitude", value=37.88)

housing_median_age = st.number_input("Idade do imóvel", value=10)
total_rooms = st.number_input("Quantidade de Cômodos", value=800)
total_bedrooms = st.number_input("Quantidade de Quartos", value=100)
population = st.number_input("População", value=300)
households = st.number_input("Domicílios", value=100)

median_income = st.slider("Renda Média (múltiplos de US$ 10k)", 0.5, 15.0, 4.5, 0.5)

# Garantir que 'ocean_proximity' está presente no DataFrame
if "ocean_proximity" in df.columns:
    # Remover valores nulos e obter valores únicos
    ocean_proximity_values = df["ocean_proximity"].dropna().unique().tolist()
    ocean_proximity = st.selectbox("Proximidade do Oceano", ocean_proximity_values)
else:
    st.error("A coluna 'ocean_proximity' não está disponível no conjunto de dados.")

median_income_cat = st.number_input("Categoria de Renda", value=4)

rooms_per_household = st.number_input("Quartos por domicílio", value=7)
bedrooms_per_room = st.number_input("Quartos por cômodo", value=0.2)
population_per_household = st.number_input("Pessoas por domicílio", value=2)

# Colunas usadas no treinamento
entrada_modelo = {
    'longitude': longitude,
    'latitude': latitude,
    'housing_median_age': housing_median_age,
    'total_rooms': total_rooms,
    'total_bedrooms': total_bedrooms,
    'population': population,
    'households': households,
    'median_income': median_income,
    'ocean_proximity': ocean_proximity,
    'median_income_cat': median_income_cat,
    'rooms_per_household': rooms_per_household,
    'bedrooms_per_room': bedrooms_per_room,
    'population_per_household': population_per_household
}

# O modelo espera um DataFrame com as mesmas colunas que foram usadas no treinamento
df_entrada_modelo = pd.DataFrame(entrada_modelo, index=[0])

botao_previsao = st.button("Prever Preço")

if botao_previsao:
    preco = modelo.predict(df_entrada_modelo)
    st.write(f"Preço Previsto: US$ {preco[0][0]:.2f}")