# Previsao-e-analise-de-dados-para-uma-biblioteca

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

## Tratamento dos dados
No tratamento dos dados, foram realizadas as seguintes etapas:

