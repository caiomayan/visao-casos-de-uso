# Especificação de Caso de Uso: Visualizar graficos

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC6 - Visualizar graficos |
| **Objetivo** | Exibir gráficos para facilitar a interpretação dos dados, incluindo comparações, tendências e variações ao longo do tempo. |
| **Requisitos Relacionados** | RF005 |
| **Atores** | Servidor |
| **Condição de Entrada** | O Servidor solicitou a visualização gráfica no Painel. |
| **Fluxo Principal** | 1. O sistema compila o conjunto atual de dados em arrays apropriados para plotagem.<br>2. O sistema carrega a biblioteca de renderização gráfica (ex: Chart.js ou similar).<br>3. O sistema exibe um gráfico de barras comparativo (Município x Município).<br>4. O sistema exibe um gráfico de linhas temporais mostrando o crescimento dos programas nos últimos 12 meses.<br>5. O Servidor pode passar o mouse (hover) sobre os nós do gráfico para ler os valores exatos. |
| **Fluxos Alternativos** | FA01 - Alternar Tipo de Gráfico: No passo 3, o ator clica no ícone de engrenagem e troca o gráfico de 'Barras' para 'Pizza' ou 'Dispersão'. |
| **Fluxos de Exceção** | FE01 - Erro de Renderização: No passo 2, se a biblioteca falhar, o sistema provê um fallback exibindo uma tabela simples em vez do gráfico. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
