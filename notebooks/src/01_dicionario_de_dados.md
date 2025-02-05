# Dicionário de dados

Origem: https://www.kaggle.com/datasets/camnugent/california-housing-prices/data

Este conjunto de dados foi derivado do censo dos EUA de 1990, usando uma linha por grupo
de blocos censitários. Um grupo de blocos é a menor unidade geográfica para a qual o
Escritório do Censo dos EUA publica dados amostrais (um grupo de blocos geralmente tem
uma população de 600 a 3.000 pessoas).

Um domicílio (*household*) é um grupo de pessoas que reside em uma casa. Como o número
médio de cômodos e quartos neste conjunto de dados é fornecido por domicílio, essas
colunas podem apresentar valores surpreendentemente altos para grupos de blocos com
poucos domicílios e muitas casas vazias, como em resorts de férias.

A variável alvo é o valor mediano das casas para os distritos da Califórnia, expressa em
dólares.

- `median_income`: renda mediana no grupo de blocos (em dezenas de milhares de dólares)
- `housing_median_age`: idade mediana das casas no grupo de blocos
- `total_rooms`: número cômodos no grupo de blocos
- `total_bedrooms`: número de quartos no grupo de blocos
- `population`: população do grupo de blocos
- `households`: domicílios no grupo de blocos
- `latitude`: latitude do grupo de blocos
- `longitude`: longitude do grupo de blocos
- `ocean_proximity`: proximidade do oceano
  - `NEAR BAY`: perto da baía
  - `<1H OCEAN`: a menos de uma hora do oceano
  - `INLAND`: no interior
  - `NEAR OCEAN`: perto do oceano
  - `ISLAND`: ilha
- `median_house_value`: valor mediano das casas no grupo de blocos (em dólares)
