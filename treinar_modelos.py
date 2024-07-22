#apenas teste
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score
modelos = {
    #"Linear Regression": LinearRegression(),
    #"Ridge Regression": Ridge(),
    #"Lasso Regression": Lasso(),
    #"Decision  cTree": DecisionTreeRegressor(),
    #"Random Forest": RandomForestRegressor(),
    #"Gradient Boosting": GradientBoostingRegressor(),
    "SVR": SVR()
}

# Avaliação de cada modelo
resultados = {}

for nome, modelo in modelos.items():
    modelo.fit(variaveis_treino, result_treino)
    y_pred = modelo.predict(variaveis_teste)
    mse = mean_squared_error(result_teste, y_pred)
    r2 = r2_score(result_teste, y_pred)
    resultados[nome] = {"MSE": mse, "R2": r2}

# Exibição dos resultados
for nome, metrica in resultados.items():
    print(f"{nome}:")
    print(f"  Mean Squared Error (MSE): {metrica['MSE']:.2f}")
    print(f"  R-squared (R2): {metrica['R2']:.2f}")

import streamlit as st

st.title('Hello, Streamlit!')
st.write('Este é o meu primeiro aplicativo web usando Streamlit.')

variaveis_treino.columns