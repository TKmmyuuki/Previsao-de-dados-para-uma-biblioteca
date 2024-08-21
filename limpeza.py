# BIBLIOTECAS
import pandas as pd
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import LabelEncoder

# IMPORTANDO DATAFRAMES 
df10_1 = pd.read_csv('../dataset/emprestimos-20101.csv')
df10_2 = pd.read_csv('../dataset/emprestimos-20102.csv')
df11_1 = pd.read_csv('../dataset/emprestimos-20111.csv')
df11_2 = pd.read_csv('../dataset/emprestimos-20112.csv')
df12_1 = pd.read_csv('../dataset/emprestimos-20121.csv')
df12_2 = pd.read_csv('../dataset/emprestimos-20122.csv')
df13_1 = pd.read_csv('../dataset/emprestimos-20131.csv')
df13_2 = pd.read_csv('../dataset/emprestimos-20132.csv')
df14_1 = pd.read_csv('../dataset/emprestimos-20141.csv')
df14_2 = pd.read_csv('../dataset/emprestimos-20142.csv')
df15_1 = pd.read_csv('../dataset/emprestimos-20151.csv')
df15_2 = pd.read_csv('../dataset/emprestimos-20152.csv')
df16_1 = pd.read_csv('../dataset/emprestimos-20161.csv')
df16_2 = pd.read_csv('../dataset/emprestimos-20162.csv')
df17_1 = pd.read_csv('../dataset/emprestimos-20171.csv')
df17_2 = pd.read_csv('../dataset/emprestimos-20172.csv')
df18_1 = pd.read_csv('../dataset/emprestimos-20181.csv')
df18_2 = pd.read_csv('../dataset/emprestimos-20182.csv')
df19_1 = pd.read_csv('../dataset/emprestimos-20191.csv')
df19_2 = pd.read_csv('../dataset/emprestimos-20192.csv')
df20_1 = pd.read_csv('../dataset/emprestimos-20201.csv')
# concatenando dados 
df = pd.concat([df10_1,df10_2,df11_1,df11_2,df12_1,df12_2,df13_1,df13_2,
                df14_1,df14_2,df15_1,df15_2,df16_1,df16_2,df17_1,df17_2,
                df18_1,df18_2,df19_1,df19_2,df20_1],ignore_index=True)
df
# explorando os dados
df.info()
df.describe(include='all')
df.value_counts()
''' PROBLEMAS ENCONTRADOS:
    - Dados faltantes 
    - Dados duplicados 
'''
# excluindo valores duplicados
df = df.drop_duplicates()

# importando exemplares
df_exemplares = pd.read_parquet('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/raw/main/Dia_1-Importando_dados/Datasets/dados_exemplares.parquet')
# unindo com o df 
df_completo = df.merge(df_exemplares)
df_completo

# ajustes no df_completo adicionado a coluna CDU_geral
CDU_lista = []
for CDU in df_completo['localizacao']:
  if(CDU < 100):
    CDU_lista.append('Generalidades')
  elif(CDU < 200):
    CDU_lista.append('Filosofia e psicologia')
  elif(CDU < 300):
    CDU_lista.append('Religião')
  elif(CDU < 400):
    CDU_lista.append('Ciências sociais')
  elif(CDU < 500):
    CDU_lista.append('Classe vaga')
  elif(CDU < 600):
    CDU_lista.append('Matemática e ciências naturais')
  elif(CDU < 700):
    CDU_lista.append('Ciências aplicadas')
  elif(CDU < 800):
    CDU_lista.append('Belas artes')
  elif(CDU < 900):
    CDU_lista.append('Linguagem')
  else:
    CDU_lista.append('Geografia. Biografia. História.')
df_completo['CDU_geral'] = CDU_lista
df_completo.drop(columns=['registro_sistema'],inplace=True)
df_completo['matricula_ou_siape'] = df_completo['matricula_ou_siape'].astype('string')


# VERIFICAÇÃO DE DADOS NULOS
# analisando data de devolução 
devolveu = df_completo.loc[df_completo['data_devolucao'].isna()]
devolveu
# excluir todos esses dados --> não é possivel emprestar um livro q não foi devolvido
df_completo = df_completo.dropna(subset=['data_devolucao'])
df_completo['CDU_geral'].value_counts()

# analisando data_renovacao
# aqueles q está com NaN em data_renovacao é pq eles não foram renovados, então vamos criar uma coluna bool (foi ou não renovado)
# substituir NaN por zero
df_completo['data_renovacao'].fillna(0, inplace=True)
df_completo['foi_renovado'] = np.where(df_completo['data_renovacao'] == 0, 0, 1)
df_completo


# CRIANDO COLUNA TARGET
# descobrindo por quantos dias foi feito o empréstimo 
df_completo['data_emprestimo'] = pd.to_datetime(df_completo['data_emprestimo'])
df_completo['data_devolucao'] = pd.to_datetime(df_completo['data_devolucao'])
df_completo['dias_de_emprestimo'] = (df_completo['data_devolucao'] - df_completo['data_emprestimo']).dt.days
df_completo
df_completo.drop(columns=['data_emprestimo', 'data_renovacao', 'data_devolucao', 'localizacao', 'id_exemplar'], inplace=True)

# Identificando outliers na coluna dias_de_emprestimo visualmente e contando-os
Q1 = df_completo['dias_de_emprestimo'].quantile(0.25)
Q3 = df_completo['dias_de_emprestimo'].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers_iqr = df_completo[(df_completo['dias_de_emprestimo'] < limite_inferior) | (df_completo['dias_de_emprestimo'] > limite_superior)]
quantidade_outliers = outliers_iqr.shape[0]

print(f"Quantidade de outliers identificados pelo IQR: {quantidade_outliers}")
df_completo.shape
# deletando outliers 
df_completo = df_completo[(df_completo['dias_de_emprestimo'] >= limite_inferior) & (df_completo['dias_de_emprestimo'] <= limite_superior)]


# Transformando dados em numeros 
    # tipo_vinculo_usuario
    # CDU_geral   
    # status_material 
    # biblioteca  
    # colecao
df_completo['tipo_vinculo_usuario'].unique()
tipo_vinculo_usuario_map = {'ALUNO DE GRADUAÇÃO':0, 'ALUNO DE PÓS-GRADUAÇÃO':1, 'DOCENTE':2,
       'SERVIDOR TÉCNICO-ADMINISTRATIVO': 3, 'DOCENTE EXTERNO': 4,
       'ALUNO MÉDIO/TÉCNICO': 5, 'USUÁRIO EXTERNO': 6, 'OUTROS': 7}
df_completo['CDU_geral'].unique()
CDU_geral_map = {'Ciências aplicadas':0, 'Linguagem':1, 'Ciências sociais':2,
       'Geografia. Biografia. História.':3,
       'Matemática e ciências naturais':4, 'Religião':5, 'Generalidades':6,
       'Filosofia e psicologia':7, 'Belas artes':8}
df_completo['status_material'].unique()
status_material_map = {'REGULAR': 0, 'ESPECIAL': 1, 'NÃO CIRCULA': 2}
df_completo['biblioteca'].unique()
biblioteca_map = {'Biblioteca Central Zila Mamede':0,
       'Biblioteca Setorial Prof. Rodolfo Helinski - Escola Agrícola de Jundiaí - EAJ  - Macaiba':1,
       'Biblioteca Setorial Bertha Cruz Enders - \xadEscola de Saúde da UFRN - ESUFRN':2,
       'Biblioteca Setorial do Centro Ciências da Saúde - CCS':3,
       'Biblioteca Setorial Prof. Alberto Moreira Campos - \xadDepartamento de Odontologia':4,
       'Biblioteca Setorial Prof. Ronaldo Xavier de Arruda - CCET':5,
       'Biblioteca Setorial do Centro de Ciências Humanas, Letras e Artes - CCHLA':6,
       'Biblioteca Setorial Prof. Horácio Nicolas Solimo - \xad Engenharia Química - EQ - CT':7,
       'Biblioteca Setorial Prof. Francisco Gurgel De Azevedo - Instituto Química - IQ':8,
       'Biblioteca Setorial do Centro Ciências Sociais Aplicadas - CCSA':9,
       'Biblioteca Setorial do Departamento de Artes - DEART':10,
       'Biblioteca Setorial Prof. Dr. Marcelo Bezerra de Melo Tinôco - DARQ - \xadCT':11,
       'Biblioteca Setorial Árvore do Conhecimento - Instituto do Cérebro - ICe':12,
       'Biblioteca Setorial Moacyr de Góes - CE':13,
       'Biblioteca Setorial Prof. Leopoldo Nelson - \xadCentro de Biociências - CB':14,
       'Biblioteca Setorial Dr. Paulo Bezerra - EMCM/RN - Caicó': 15,
       'Biblioteca Setorial Pe. Jaime Diniz - Escola de Música - EMUFRN':16,
       'Biblioteca Setorial Profª. Maria Lúcia da Costa Bezerra - \xadCERES\xad - Caicó':17,
       'Biblioteca Setorial Profª. Maria José Mamede Galvão - FELCS - Currais Novos':18,
       'Biblioteca Setorial do Núcleo de Educação da Infância - NEI':19,
       'Biblioteca Setorial da Faculdade de Ciências da Saúde do Trairi - FACISA - Santa Cruz':20,
       'Biblioteca Setorial do Núcleo de Ensino Superior do Agreste - NESA - Nova Cruz':21}
df_completo['colecao'].unique()
colecao_map = {'Acervo Circulante':0, 'Folhetos':1, 'Teses':2, 'Dissertações':3,
       'Monografias':4, 'Publicações de Autores do RN':5,
       'Publicações da UFRN':6, 'Multimeios':7, 'Coleção Mossoroense':8,
       'Eventos':15, 'Trabalho Acadêmico':9, 'Obras de Referência':10,
       'Obras Raras':11, 'Literatura de Cordel':12, 'Coleção Zila Mamede': 13,
       'Necessidades Educacionais Específicas': 14}
df_completo['tipo_vinculo_usuario'] = df_completo['tipo_vinculo_usuario'].map(tipo_vinculo_usuario_map)
df_completo['CDU_geral'] = df_completo['CDU_geral'].map(CDU_geral_map)
df_completo['status_material'] = df_completo['status_material'].map(status_material_map)
df_completo['biblioteca'] = df_completo['biblioteca'].map(biblioteca_map)
df_completo['colecao'] = df_completo['colecao'].map(colecao_map)
df_completo.info()


# Arrumando codigo de barras
  # PROBLEMA: tinha código com apenas números e outros com letras 
df = df_completo[df_completo['codigo_barras'].str.contains('[a-zA-Z]')]
df_completo['codigo_barras'] = pd.to_numeric(df_completo['codigo_barras'], errors='coerce')
df_completo = df_completo.dropna(subset=['codigo_barras'])

colunas_para_separar = ['codigo_barras']
transformado = df[colunas_para_separar]
for column in transformado.columns:
    if transformado[column].dtype == 'object':
        df[column] = label_encoder.fit_transform(df[column])
df.info()
df_final = pd.concat([df, df_completo], ignore_index=True)
df_final.info()
df_final = df_final.drop('matricula_ou_siape', axis=1)


# CONSIDERAÇÕES FINAIS
df_final.isna().sum()
output_file_path = 'df_arrumado.csv'
df_final.to_csv(output_file_path, index=False)
data = pd.read_csv('df_arrumado.csv')
data.info()