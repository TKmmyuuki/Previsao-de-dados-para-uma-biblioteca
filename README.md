# Previsão de dados para uma biblioteca

## Descrição
Este projeto visa prever o número de dias que um livro levará para ser devolvido após o empréstimo, utilizando modelos de regressão. A análise envolve a limpeza e tratamento dos dados, além da aplicação de vários algoritmos de regressão para criar um modelo preditivo eficiente.

## Índice
- [Importação e limpeza dos dados](##importação-e-limpeza-dos-dados)
- [Tratamento dos dados](#tratamento-dos-dados)
- [Previsão](#previsao)
  -  [Exemplo](#exemplo)

## Importação e limpeza dos dados
1. **Importação dos Dados**:
   Os dados foram obtidos do seguinte link: [GitHub - FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas](https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas).

2. **Limpeza dos Dados**:
   - **Concatenação e exclusão de duplicatas**: Os dados foram concatenados e duplicatas foram removidas.
   - **Tratamento de valores nulos**: Valores nulos ou faltantes foram limpos. Registros sem data de devolução foram excluídos. Para a coluna 'data_renovacao', que possuía valores NaN, foi criada uma nova coluna 'foi_renovado' para indicar se o livro foi renovado.
   - **Criação da coluna target**: A diferença entre 'data_emprestimo' e 'data_devolução' foi calculada para criar a coluna 'dias_de_emprestimo', que servirá como variável target.
     - Remoção de Outliers: Outliers foram identificados e removidos para melhorar a qualidade dos dados.

3. **Mapeamento de Colunas**:
   - Colunas categóricas ('tipo_vinculo_usuario', 'CDU_geral', 'status_material', 'biblioteca', 'colecao') foram mapeadas para valores numéricos.
   - A coluna 'codigo_barras', que continha tanto valores inteiros quanto strings, foi normalizada para inteiros.

## Tratamento dos Dados

Após a limpeza dos dados, foram realizadas as seguintes etapas de tratamento para melhorar o desempenho dos modelos de regressão:

1. **Tratamento de Outliers**:
   - **Identificação e Remoção de Outliers**: Foram aplicados métodos para identificar e tratar outliers em todas as colunas relevantes. Utilizou-se um fator de 1.05 para ajustar os limites e tratar valores extremos que poderiam influenciar negativamente os modelos. Esse processo ajuda a melhorar a robustez e a precisão dos modelos ao reduzir a influência de dados atípicos.

2. **Reagrupamento de Categorias**:
   - **Coluna 'colecao'**: A coluna 'colecao' foi reorganizada para simplificar as categorias e reduzir a complexidade. Isso ajuda a melhorar a performance dos modelos ao ter um conjunto de dados mais limpo e mais coerente.
   - **Coluna 'tipo_vinculo_usuario'**: Similarmente, a coluna 'tipo_vinculo_usuario' teve suas categorias reorganizadas para facilitar a análise e a modelagem. A reagrupação foi feita para assegurar que as categorias fossem mais representativas e melhor ajustadas para a previsão.

Essas etapas de tratamento foram fundamentais para aprimorar a qualidade dos dados e, consequentemente, melhorar a performance dos modelos de regressão utilizados para prever os dias de empréstimo dos livros.

## Previsão

