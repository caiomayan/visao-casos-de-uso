# Especificação de Caso de Uso: Visualizar rankings

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC13 - Visualizar rankings |
| **Objetivo** | Apresentar rankings e painéis comparativos para apoiar a leitura dos dados por programa, município ou regional. |
| **Requisitos Relacionados** | RF015 |
| **Atores** | Servidor |
| **Condição de Entrada** | O ator ativa a aba de Rankings. |
| **Fluxo Principal** | 1. O sistema ordena os municípios de forma decrescente com base no volume de atendimentos.<br>2. O sistema renderiza uma tabela no formato 'Top 10' e 'Bottom 10' de adesão.<br>3. O sistema apresenta setas indicativas de subida/descida no ranking (Trend Up / Trend Down).<br>4. O Servidor acompanha as regiões que precisam de mais investimento social baseando-se no ranking. |
| **Fluxos Alternativos** | FA01 - Alterar Critério do Ranking: No passo 1, o ator pode pedir para ordenar por 'Maior Orçamento' em vez de 'Maior Atendimento'. |
| **Fluxos de Exceção** | Não existem fluxos de exceção críticos para este caso de uso. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
