# IMPORTANDO DADOS 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('df_s_out.csv')

# Mapa de correlção
correlation_matrix = df.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")

# Dividir os dados em train e test
variaveis  = df.drop(columns=["dias_de_emprestimo", "codigo_barras", "id_emprestimo"])
resultado = df["dias_de_emprestimo"]

variaveis_treino, variaveis_teste, result_treino, result_teste = train_test_split(
    variaveis, resultado, shuffle=True)

# Treinar modelos
modelos = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(),
    "Lasso Regression": Lasso(),
    "Decision  cTree": DecisionTreeRegressor(),
    "Random Forest": RandomForestRegressor()
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

# Foi escolhido: RandomForestRegressor
modelo = RandomForestRegressor()
modelo.fit(variaveis_treino, result_treino)

# Função para coletar novos dados e fazer previsão
def coletar_dados_e_prever():
    # Coletar dados do usuário
    print("Digite: 0: Aluno de Graduação, 1: Aluno de Pós-graduação, 2: Docente, 3: Docente Externo, 4: Servidor Técnico-administrativo, 5: Outros")
    novo_vinculo = int(input())
    print("Digite: 0: Acervo, 1: Obras Raras e de Referencia, 2: Coleções, 3: Multimeios, 4: Teses e Trabalhos Acadêmicos, 5: Dissertações e Monografia, 6: Publicações da UFRN, 7: Outros")
    novo_colecao = int(input())
    print("Digite: 0: Biblioteca Central Zila Mamede, 1: Biblioteca Setorial Prof. Rodolfo Helinski - Escola Agrícola de Jundiaí - EAJ  - Macaiba, 2: Biblioteca Setorial Bertha Cruz Enders - \xadEscola de Saúde da UFRN - ESUFRN, 3: Biblioteca Setorial do Centro Ciências da Saúde - CCS, 4: Biblioteca Setorial Prof. Alberto Moreira Campos - \xadDepartamento de Odontologia, 5: Biblioteca Setorial Prof. Ronaldo Xavier de Arruda - CCET, 6: Biblioteca Setorial do Centro de Ciências Humanas, Letras e Artes - CCHLA, 7: Biblioteca Setorial Prof. Horácio Nicolas Solimo - \xad Engenharia Química - EQ - CT, 8: Biblioteca Setorial Prof. Francisco Gurgel De Azevedo - Instituto Química - IQ, 9: Biblioteca Setorial do Centro Ciências Sociais Aplicadas - CCSA, 10: Biblioteca Setorial do Departamento de Artes - DEART, 11: Biblioteca Setorial Prof. Dr. Marcelo Bezerra de Melo Tinôco - DARQ - \xadCT, 12: Biblioteca Setorial Árvore do Conhecimento - Instituto do Cérebro - ICe, 13: Biblioteca Setorial Moacyr de Góes - CE, 14: Biblioteca Setorial Prof. Leopoldo Nelson - \xadCentro de Biociências - CB, 15: Biblioteca Setorial Dr. Paulo Bezerra - EMCM/RN - Caicó, 16: Biblioteca Setorial Pe. Jaime Diniz - Escola de Música - EMUFRN, 17: Biblioteca Setorial Profª. Maria Lúcia da Costa Bezerra - \xadCERES\xad - Caicó, 18: Biblioteca Setorial Profª. Maria José Mamede Galvão - FELCS - Currais Novos, 19: Biblioteca Setorial do Núcleo de Educação da Infância - NEI, 20: Biblioteca Setorial da Faculdade de Ciências da Saúde do Trairi - FACISA - Santa Cruz, 21: Biblioteca Setorial do Núcleo de Ensino Superior do Agreste - NESA - Nova Cruz")
    novo_biblioteca = int(input())
    print("Digite: 0: Regular, 1: Especial, 2: Não-circulante")
    novo_status = int(input())
    print("Digite: 0: Ciências aplicadas, 1: Linguagem, 2: Ciências sociais, 3: Geografia, Biografia ou História, 4: Matemática e Ciências Naturais, 5: Religião, 6: Generalidades, 7: Filosofia e Psicologia, 8: Belas artes")
    novo_CDU = int(input())
    print("Foi renovado? Digite: 0: Não, 1: Sim")
    novo_renovado = int(input())

    # Criar um DataFrame com o novo dado
    novo_dado = pd.DataFrame([[novo_vinculo, novo_colecao, novo_biblioteca, novo_status, novo_CDU, novo_renovado]], 
                             columns=['tipo_vinculo_usuario', 'colecao', 'biblioteca', 'status_material', 'CDU_geral', 'foi_renovado'])

    # Fazer previsão
    predicao = modelo.predict(novo_dado)
    
    # Arredondar a previsão para o inteiro mais próximo
    predicao_inteira = int(round(predicao[0]))

    # Exibir o resultado da previsão
    print(f'A previsão para os dados inseridos é: {predicao_inteira}')

# Chamar a função para coletar dados e fazer previsão
coletar_dados_e_prever()
