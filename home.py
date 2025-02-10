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

condados = list(gdf_geo["name"].sort_values())

selecionar_condado = st.selectbox("Região", condados)

longitude = gdf_geo.query("name == @selecionar_condado")["longitude"].values
latitude = gdf_geo.query("name == @selecionar_condado")["latitude"].values

housing_median_age = st.number_input("Idade do imóvel", value=10, min_value=1, max_value=50)

total_rooms = gdf_geo.query("name == @selecionar_condado")["total_rooms"].values
total_bedrooms = gdf_geo.query("name == @selecionar_condado")["total_bedrooms"].values
population = gdf_geo.query("name == @selecionar_condado")["population"].values
households = gdf_geo.query("name == @selecionar_condado")["households"].values

median_income = st.slider("Renda Média (Milhares de US$)", 5.0, 100.0, 45.0, 5.0)

ocean_proximity = gdf_geo.query("name == @selecionar_condado")["ocean_proximity"].values

bins_income = [0, 1.5, 3, 4.5, 6, np.inf]
median_income_cat = np.digitize(median_income / 10, bins=bins_income)

rooms_per_household = gdf_geo.query("name == @selecionar_condado")["rooms_per_household"].values
bedrooms_per_room = gdf_geo.query("name == @selecionar_condado")["bedrooms_per_room"].values
population_per_household = gdf_geo.query("name == @selecionar_condado")["population_per_household"].values

# Colunas usadas no treinamento
entrada_modelo = {
    'longitude': longitude,
    'latitude': latitude,
    'housing_median_age': housing_median_age,
    'total_rooms': total_rooms,
    'total_bedrooms': total_bedrooms,
    'population': population,
    'households': households,
    'median_income': median_income / 10,
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