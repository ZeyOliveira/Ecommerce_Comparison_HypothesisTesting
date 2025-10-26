# Análise de Performance de E-commerce: Avaliando o Valor Médio por Item (Reino Unido vs. Alemanha)

## Visão Geral do Projeto

Este projeto de Ciência de Dados explora o comportamento de compra em uma plataforma de e-commerce, focando na comparação do **valor médio total por item de linha ** entre clientes do Reino Unido e da Alemanha. Utilizando **testes de hipótese** e análise do **tamanho do efeito (Cohen's d)**, o objetivo é ir além da significância estatística para identificar a **relevância prática** dos resultados para a estratégia de negócio.

Demonstra habilidades em manipulação de dados, análise estatística e comunicação de insights acionáveis para stakeholders.

**Link para o Dataset no Kaggle:** https://www.kaggle.com/datasets/carrie1/ecommerce-data/data

## Problema de Negócio & Questão de Pesquisa

Uma empresa de e-commerce busca otimizar suas estratégias de marketing e vendas em diferentes mercados. Surge a questão:
*   `Existe uma diferença estatisticamente significativa no valor médio total por item de linha entre clientes do Reino Unido e da Alemanha?`

## Metodologia & Tecnologias Utilizadas

*   **Linguagem de Programação:** Python
*   **Bibliotecas:**
    *   `pandas` para manipulação de dados.
    *   `numpy` para operações numéricas.
    *   `scipy.stats` para os testes estatísticos.
    *   `statsmodels` para os testes estatísticos.
    *   `seaborn` visualizações.
    *   `matplotlib` visualizações.
*   **Análise Estatística:**
    *   **Testes de Normalidade:** Kosmogorov-Smirnov, Lilliefors, Anderson-Darling para verificar a normalidade dos dados.
    *   **Testes de Homocedasticidade:** Levene e Barlett para avaliar a homogeneidade das variâncias.
    *   **Teste de Hipótese:** Teste t de Student e Welch para duas amostras independentes.
    *   **Tamanho do Efeito:** Cálculo do **Cohen's d** para quantificar a magnitude da diferença observada.
*   **Visualização:** Gráficos para EDA e apresentação de resultados.
*   **Ambiente:** Jupyter Notebook (com VS Code para desenvolvimento).

## Principais Descobertas e Implicações

A análise revelou que, embora o **teste t de Student e Welch** tenha indicado uma **diferença estatisticamente significativa** no valor médio por item entre os dois países (p-value < 0.05), o **tamanho do efeito (Cohen's d) calculado foi praticamente insignificante (d ≈ 0.02)**.

**Interpretação para o Negócio:**
*   A pequena diferença numérica observada entre as médias dos países não se traduz em um impacto prático relevante para a tomada de decisão estratégica ou alocação de recursos.
*   Recrutadores e equipes de produto podem inferir que focar em estratégias de preço ou marketing distintas para estes dois mercados, com base apenas nesta métrica, seria ineficaz ou de baixo retorno.

Este resultado sublinha a importância de complementar a significância estatística com a análise do tamanho do efeito para evitar conclusões precipitadas e garantir que as decisões de negócio sejam fundamentadas em evidências com impacto real.

## Análise Detalhada

Para uma compreensão completa da metodologia, exploração de dados, testes estatísticos aplicados e a interpretação aprofundada dos resultados e recomendações para stakeholders, acesse o notebook principal do projeto:

*   [**`01_eda.ipynb`**](https://github.com/ZeyOliveira/Ecommerce_Comparison_HypothesisTesting/blob/main/notebook/01_eda.ipynb)

## Como Rodar o Projeto

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/ZeyOliveira/Ecommerce_Comparison_HypothesisTesting.git
    cd Ecommerce_Comparison_HypothesisTesting
    ```
2.  **Crie um Ambiente Virtual (Opcional, mas recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    ./venv/Scripts/activate   # Windows
    ```
3.  **Instale as Dependências:**
    ```bash
    pip install requirements.txt
    ```
4.  **Abra e Execute o Notebook:**
    *   Abra o arquivo `01_eda.ipynb` no VS Code ou Jupyter Lab/Notebook.
    *   Execute todas as células para reproduzir a análise.

## Contato

Conecte-se comigo! Estou sempre aberto a discussões sobre dados, projetos e oportunidades na área de TI.

*   **Zeygler**
*   **LinkedIn:** https://www.linkedin.com/in/zeygleroliveira/
*   **GitHub:** https://github.com/ZeyOliveira
