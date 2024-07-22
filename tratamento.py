import pandas as pd
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt

def verificar_outliers_iqr(data, coluna, fator):
    # Verifica a quantidade de outliers em um DataFrame com base no dataframe, coluna desejada e fator

    Q1 = data[coluna].quantile(0.25)
    Q3 = data[coluna].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - fator * IQR
    limite_superior = Q3 + fator * IQR

    outliers_iqr = data[(data[coluna] < limite_inferior) | (data[coluna] > limite_superior)]
    quantidade_outliers = outliers_iqr.shape[0]
    
    return quantidade_outliers
def remover_outliers_iqr(data, coluna, fator):
    # Remove os outliers de um DataFrame com base na coluna especificada
    
    Q1 = data[coluna].quantile(0.25)
    Q3 = data[coluna].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - fator * IQR
    limite_superior = Q3 + fator * IQR

    data_sem_outliers = data[(data[coluna] >= limite_inferior) & (data[coluna] <= limite_superior)]
    
    return data_sem_outliers
def plotar_grafico_dispersao(data, variavel_x, variavel_y, posicao_grade, paleta="Dark2"):
    plt.subplot(2, 3, posicao_grade)
    sns.scatterplot(data=data, x=variavel_x, y=variavel_y, palette=paleta)
    sns.despine(top=True, right=True, bottom=True, left=True)
def processar_status_material(data, coluna, status, fator):
    # Processa e remove outliers para um dado status_material no DataFrame.
    df_status = data.loc[data[coluna] == status]
    data = data.loc[data[coluna] != status]
    
    quantidade_outliers = verificar_outliers_iqr(df_status, 'dias_de_emprestimo', fator)
    print(f"A quantidade de outliers na coluna 'dias_de_emprestimo' para {coluna} {status} é: {quantidade_outliers}")
    
    df_status_sem_outliers = remover_outliers_iqr(df_status, 'dias_de_emprestimo', fator)
    data = pd.concat([data, df_status_sem_outliers], ignore_index=True)
    
    return data

# Importando dataframe limpo para começarmos a tratar os dados 
    # Foi testado diversos modelos com o df apenas limpo, mas estavam tendo um péssimo desempenho
    # solução: tratamento dos outliers em cada coluna - foi definido no processo fator do IQR = 1.05 para um melhor resultado
data = pd.read_csv('df_arrumado.csv')
data.info()


# COLUNA: 'colecao'
plotar_grafico_dispersao(data, "colecao", "dias_de_emprestimo", 1)
data['colecao'].value_counts()

# Processar diferentes valores de 'colecao'
for status in range(16):
    data = processar_status_material(data, 'colecao', status, 1.05)
plotar_grafico_dispersao(data, "colecao", "dias_de_emprestimo", 1)

# Agrupando em categorias
'''
0: acervo (0)
1: obras raras de referencia (10, 11)
2: coleções (8, 13) 
3: multimeios (7)
4: teses + trabalhos (2, 9)
5: dissertações + monografia (3,4)
6: publicações RN + publicações UFRN (5,6)
7: outros = cordel + eventos + necessidades + folhetos (14, 15, 12, 1)
'''
substituicoes = {
    1: 7,
    2: 4,
    3: 5,
    4: 5,
    5: 6,
    7: 3,
    8: 2,
    9: 4,
    10: 1,
    11: 1,
    12: 7,
    13: 2,
    14: 7,
    15: 7
}
# Substituir os valores na coluna 'colecao'
data['colecao'] = data['colecao'].replace(substituicoes)
data['colecao'].value_counts()
plotar_grafico_dispersao(data, "colecao", "dias_de_emprestimo", 1)

# Verficação de outliers nas colunas que foram unidas
status_values = [1, 2, 4, 5, 6, 7]
for status in status_values:
    data = processar_status_material(data, 'status_material', status, 1.05)
plotar_grafico_dispersao(data, "colecao", "dias_de_emprestimo", 1)


# COLUNA: 'tipo_vinculo_usuario'
plotar_grafico_dispersao(data, "tipo_vinculo_usuario", "dias_de_emprestimo", 2)
data['tipo_vinculo_usuario'].value_counts()

# Processar diferentes valores de 'tipo_vinculo_usuario'
for status in range(8):
    data = processar_status_material(data, 'tipo_vinculo_usuario', status, 1.05)
plotar_grafico_dispersao(data, "tipo_vinculo_usuario", "dias_de_emprestimo", 2)

# Agrupando em categorias
'''
0: 'ALUNO DE GRADUAÇÃO'
1: 'ALUNO DE PÓS-GRADUAÇÃO'
2: 'DOCENTE'
3: 'DOCENTE EXTERNO'
4: 'SERVIDOR TÉCNICO-ADMINISTRATIVO',
5: 'ALUNO MÉDIO/TÉCNICO', 'USUÁRIO EXTERNO' e 'OUTROS' (5, 6, 7)
'''
substituicoes = {
    3: 4, 
    4: 3,
    6: 5,
    7: 5,
}
# Substituir os valores na coluna 'tipo_vinculo_usuario'
data['tipo_vinculo_usuario'] = data['tipo_vinculo_usuario'].replace(substituicoes)
data['tipo_vinculo_usuario'].value_counts()
plotar_grafico_dispersao(data, "tipo_vinculo_usuario", "dias_de_emprestimo", 2)

# Verficação de outliers nas colunas que foram unidas
data = processar_status_material(data, 'tipo_vinculo_usuario', 5, 1.05)
plotar_grafico_dispersao(data, "tipo_vinculo_usuario", "dias_de_emprestimo", 2)


# COLUNA: 'biblioteca'
plotar_grafico_dispersao(data, "biblioteca", "dias_de_emprestimo", 3)
data['biblioteca'].value_counts()
# Processar diferentes valores de 'tipo_vinculo_usuario'
for status in range(22):
    data = processar_status_material(data, 'tipo_vinculo_usuario', status, 1.05)
plotar_grafico_dispersao(data, "biblioteca", "dias_de_emprestimo", 3)


# COLUNA: 'CDU_geral'
plotar_grafico_dispersao(data, "CDU_geral", "dias_de_emprestimo", 4)
data['CDU_geral'].value_counts()
# Processar diferentes valores de 'tipo_vinculo_usuario'
for status in range(9):
    data = processar_status_material(data, 'CDU_geral', status, 1.05)
plotar_grafico_dispersao(data, "CDU_geral", "dias_de_emprestimo", 4)


# COLUNA: 'status_material'
plotar_grafico_dispersao(data, "status_material", "dias_de_emprestimo", 5)
data['status_material'].value_counts()
# Processar diferentes valores de 'status_material'
for status in range(3):
    data = processar_status_material(data, 'status_material', status, 1.05)
plotar_grafico_dispersao(data, "status_material", "dias_de_emprestimo", 5)


# COLUNA: 'status_material'
plotar_grafico_dispersao(data, "foi_renovado", "dias_de_emprestimo", 6)
data['foi_renovado'].value_counts()
# Processar diferentes valores de 'foi_renovado'
for valor in range(2):
    data = processar_status_material(data, 'foi_renovado', valor, 1.05)
plotar_grafico_dispersao(data, "foi_renovado", "dias_de_emprestimo", 6)

# CONSIDERAÇÕES FINAIS
df_final.isna().sum()
output_file_path = 'df_s_out.csv'
df_final.to_csv(output_file_path, index=False)
