# Especificação de Caso de Uso: Identificar padroes

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC7 - Identificar padroes |
| **Objetivo do Sistema** | Permitir identificar tendências e mudanças nos indicadores sociais. |
| **Requisito Associado** | RF006 |
| **Atores Envolvidos** | Servidor |
| **O que o usuário vê (Elementos de Interface)** | Caixas de texto (Cards) destacando 'Insights Automatizados' curtos, e botão 'Exportar Destaque'. |
| **O que o usuário insere (Dados Fornecidos)** | Cliques nos botões de feedback do insight (Útil / Não Útil). |
| **Condição de Entrada** | O Servidor acessa o módulo Analítico Avançado. |
| **Fluxo Principal (Passo a Passo)** | 1. O Servidor acessa a aba 'Análise de Padrões'.<br>2. O sistema processa análise matemática básica sobre o histórico.<br>3. O sistema apresenta caixas de texto com insights automáticos (ex: 'O programa X cresceu 20%').<br>4. O Servidor sinaliza se o alerta foi útil para o algoritmo registrar a preferência. |
| **Fluxos Alternativos / Desvios** | FA01 - Exportar Insight: No passo 3, baixar a imagem em formato PNG contendo o insight para uso em slides. |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Dados Insuficientes: Exibição de aviso caso haja menos de 3 meses de histórico para análise confiável. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
