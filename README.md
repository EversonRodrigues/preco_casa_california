# 📊 Projeto de Regressão Linear - Ciência de Dados Impressionador

Este repositório contém um projeto desenvolvido durante o curso **Ciência de Dados Impressionador** da **Hashtag Treinamentos**. O objetivo do projeto é aplicar técnicas de **Regressão Linear** para prever preços de casas na Califórnia com base em um conjunto de dados do **California Housing Dataset**. O objetivo foi explorar e modelar a relação entre diferentes variáveis, como renda média da população, idade média das casas e localização geográfica, a fim de estimar o valor das propriedades.

## 📝 Etapas do Projeto

1. **Entendimento da Base de Dados**
   - Exploração inicial do dataset.
   - Identificação das principais variáveis.

2. **Importação de Bibliotecas**
   - Utilização de bibliotecas como `pandas`, `numpy`, `seaborn`, `matplotlib`, `sklearn`, `geopandas`, `folium`, entre outras.

3. **Análise Inicial dos Dados**
   - Verificação de informações básicas do dataset.
   - Identificação e tratamento de valores nulos e duplicados.

4. **Feature Engineering**
   - Criação de novas variáveis a partir dos dados existentes.
   - Aplicação de critérios para eliminação de outliers.
   - Otimização do dataframe para melhor desempenho.

5. **Separação de Variáveis**
   - Identificação e tratamento de colunas categóricas e numéricas.
   - Geração de uma nova base de dados no formato **Parquet**.

6. **Visualização de Dados**
   - Geração de gráficos exploratórios com **Seaborn** e **Matplotlib**.
   - Uso do **GeoPandas** e **Folium** para visualização espacial dos dados.

7. **Preparação para Machine Learning**
   - Aplicação de estratégias de pré-processamento.
   - Escolha do modelo de Regressão Linear.
   - Utilização de **GridSearch** para otimização dos hiperparâmetros.

8. **Treinamento e Persistência do Modelo**
   - Treinamento do modelo utilizando **Scikit-Learn**.
   - Salvamento do modelo com **Joblib** para futura utilização.

9. **Deploy do Modelo**
   - Implementação do modelo em uma aplicação **Streamlit** para interação com os usuários.

---

## 🔧 Instalação e Configuração

Para rodar o projeto localmente, siga os passos abaixo:

### 1️⃣ Clone este repositório
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio


## Organização do projeto

```
├── .env               <- Arquivo de variáveis de ambiente (não versionar)
├── .gitignore         <- Arquivos e diretórios a serem ignorados pelo Git
├── environment.yml       <- O arquivo de requisitos para reproduzir o ambiente de machine learning
├── LICENSE            <- Licença de código aberto se uma for escolhida
├── README.md          <- README principal para desenvolvedores que usam este projeto.
|
├── dados              <- Arquivos de dados para o projeto.
|
├── modelos            <- Modelos treinados e serializados, previsões de modelos ou resumos de modelos
|
├── notebooks          <- Cadernos Jupyter. A convenção de nomenclatura é um número (para ordenação),
│                         as iniciais do criador e uma descrição curta separada por `-`, por exemplo
│                         `01-fb-exploracao-inicial-de-dados`.
│
|   └──src             <- Código-fonte para uso neste projeto.
|      │
|      ├── __init__.py  <- Torna um módulo Python
|      ├── 01_dicionario_de_dados.md <- Dicionário que auxilia na tradução dos dados do projeto
|      ├── config.py    <- Configurações básicas do projeto
|      ├── auxiliares <- funções auxiliares
|      ├── models0 <- funções utilizadas para auxiliar na seleção do modelo
|      └── graficos.py  <- Scripts para criar visualizações exploratórias e orientadas a resultados
|
├── referencias        <- Dicionários de dados, manuais e todos os outros materiais explicativos.
|
├── relatorios         <- Análises geradas em HTML, PDF, LaTeX, etc.
│   └── imagens        <- Gráficos e figuras gerados para serem usados em relatórios
```

## Configuração do ambiente

1. Faça o clone do repositório que será criado a partir deste modelo.

    ```bash
    git clone ENDERECO_DO_REPOSITORIO
    ```

2. Crie um ambiente virtual para o projeto utilizando o gerenciador de ambientes de sua preferência.

    a. Caso esteja utilizando o `conda`, exporte as dependências do ambiente para o arquivo `environmente.yml`:

      ```bash
      conda env export > environmente.yml
      ```

    b. Caso esteja utilizando outro gerenciador de ambientes, exporte as dependências
    para o arquivo `requirements.txt` ou outro formato de sua preferência. Adicione o
    arquivo ao controle de versão, removendo o arquivo `ambiente.yml`.