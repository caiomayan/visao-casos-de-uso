# Especificação de Caso de Uso: Identificar padroes

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC7 - Identificar padroes |
| **Objetivo** | Permitir identificar padrões, tendências e mudanças nos indicadores sociais, como evolução populacional e variações territoriais. |
| **Requisitos Relacionados** | RF006 |
| **Atores** | Servidor |
| **Condição de Entrada** | O Servidor está acessando o módulo Analítico Avançado. |
| **Fluxo Principal** | 1. O Servidor acessa a aba 'Análise de Padrões'.<br>2. O sistema processa uma regressão linear sobre os dados históricos da base.<br>3. O sistema apresenta caixas de texto com 'Insights Automatizados' (ex: 'O programa X teve um aumento de 20% no Cariri nos últimos 3 meses').<br>4. O Servidor sinaliza o insight como útil ou não útil. |
| **Fluxos Alternativos** | FA01 - Exportar Insight: No passo 3, o Servidor pode clicar em 'Exportar Destaque' para baixar uma imagem png contendo a tendência identificada para uso em apresentações. |
| **Fluxos de Exceção** | FE01 - Dados Insuficientes: No passo 2, se houver menos de 3 meses de histórico, o sistema exibe 'Dados insuficientes para calcular tendências precisas'. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
