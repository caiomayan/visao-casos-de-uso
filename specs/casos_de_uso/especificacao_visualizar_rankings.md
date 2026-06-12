# Especificação de Caso de Uso: Visualizar rankings

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC13 - Visualizar rankings |
| **Objetivo do Sistema** | Apresentar rankings para apoiar a leitura comparativa. |
| **Requisito Associado** | RF015 |
| **Atores Envolvidos** | Servidor |
| **O que o usuário vê (Elementos de Interface)** | Lista textual numerada no formato de pódio (Top 1 a 10) e uma tabela com os municípios de piores posições, acompanhados de setas de subida verde e descida vermelha. |
| **O que o usuário insere (Dados Fornecidos)** | Dropdown de seleção de Critério: 'Ordem por Orçamento' ou 'Ordem por Pessoas Atendidas'. |
| **Condição de Entrada** | O ator ativa a aba de Rankings. |
| **Fluxo Principal (Passo a Passo)** | 1. O sistema ordena os municípios ou regionais decrescentemente pelo critério padrão.<br>2. O sistema renderiza a tela de Leaderboard (Top 10 / Bottom 10).<br>3. O sistema insere alertas de variação (trend arrows) mostrando quem subiu ou caiu na última semana.<br>4. O Servidor analisa os dados. |
| **Fluxos Alternativos / Desvios** | FA01 - Mudar Critério: O Servidor altera o Dropdown para ordenar os piores baseados em rejeição de matrículas. |
| **Fluxos de Exceção (Erros e Limites)** | Nenhuma validação de exceção. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
