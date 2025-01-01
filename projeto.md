---
title: "Cronograma: Fundamentos de Programação"
author: Albert E. F. Muritiba
date: 22-02-2024
output: pdf_document
---

# Projeto Final: Análise de Desempenho Acadêmico com Python

## Objetivo Geral
Desenvolver um programa em Python para realizar a análise estatística de um conjunto de dados fictício de desempenho acadêmico. O objetivo é aplicar conceitos de programação aprendidos ao longo do semestre, incluindo manipulação de coleções, uso de funções, cálculos estatísticos e visualizações gráficas.

---

## Conjunto de Dados
Um arquivo CSV será fornecido contendo informações sobre o desempenho de uma turma fictícia. O formato será:

| ID   | Nome               | Disciplina       | Nota1 | Nota2 | Frequência (%) |
|------|--------------------|------------------|-------|-------|----------------|
| 1    | Ana Beatriz Silva  | Estatística      | 8.5   | 7.0   | 90             |
| 2    | João Alex Pereira  | Matemática       | 6.0   | 5.5   | 75             |
| ...  | ...                | ...              | ...   | ...   | ...            |

---

## Requisitos do Programa

### 1. **Leitura e Estruturação dos Dados**
   - Importar os dados do arquivo CSV utilizando a biblioteca `pandas`.
   - Mostrar as 5 primeiras linhas dos dados no console para validação.

### 2. **Cálculos Estatísticos**
   - Calcular as seguintes estatísticas:
     - Média, mediana e desvio padrão das notas (separadas por disciplina).
     - Frequência média da turma.
   - Identificar os alunos com desempenho abaixo da média em cada disciplina.

### 3. **Classificação do Desempenho**
   - Criar uma nova coluna indicando a situação do aluno:
     - **"Aprovado"**: Média ≥ 7 e frequência ≥ 75%.
     - **"Recuperação"**: 5 ≤ Média < 7.
     - **"Reprovado"**: Média < 5 ou frequência < 75%.

### 4. **Visualizações Gráficas**
   - Criar os seguintes gráficos:
     - Histograma das notas (Nota1 e Nota2 separadamente).
     - Gráfico de barras com a distribuição de alunos por situação ("Aprovado", "Recuperação", "Reprovado").
     - Boxplot para comparar a dispersão das notas por disciplina.

### 5. **Modularização**
   - Estruturar o programa em funções bem definidas:
     - `ler_dados()`: Leitura e carregamento dos dados.
     - `calcular_estatisticas()`: Realização dos cálculos estatísticos.
     - `classificar_alunos()`: Determinação da situação dos alunos.
     - `gerar_graficos()`: Criação e exibição dos gráficos.

---

## Exemplo de Fluxo do Programa
1. **Leitura do Arquivo**: 
   - O programa lê o arquivo CSV e exibe as primeiras linhas para confirmação.
2. **Cálculo de Estatísticas**: 
   - O usuário escolhe calcular as estatísticas gerais ou apenas de uma disciplina.
3. **Classificação de Alunos**: 
   - A situação dos alunos é determinada e exibida.
4. **Geração de Gráficos**: 
   - Gráficos são exibidos para visualizar os dados de maneira intuitiva.

---

## Avaliação
- **Funcionalidade do Código**: 50%
- **Organização do Código**: 20%
- **Qualidade das Visualizações**: 20%
- **Documentação e Relatório**: 10%

---

## Entrega
- **Formato**: Arquivo Python (.py) contendo o código e um relatório com as respostas para as análises realizadas.
- **Data**: Até o último dia do semestre.

---

## Observação
O conjunto de dados fictício será gerado e fornecido pelo professor, utilizando um script Python. O arquivo conterá informações simuladas para garantir que todos os alunos trabalhem com o mesmo material.

