# Especificação de Caso de Uso: Filtrar dados

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC5 - Filtrar dados |
| **Objetivo** | Permitir filtrar os dados por município e por regional, possibilitando análises territorializadas dos indicadores sociais. |
| **Requisitos Relacionados** | RF004 |
| **Atores** | Servidor |
| **Condição de Entrada** | O Servidor está no painel de indicadores ou em relatórios com dados consolidados. |
| **Fluxo Principal** | 1. O Servidor clica no botão 'Filtros Avançados'.<br>2. O sistema abre um modal contendo as opções 'Município' e 'Regional de Ensino/Saúde/Social'.<br>3. O Servidor seleciona uma ou mais opções nos campos de seleção dropdown.<br>4. O Servidor clica em 'Aplicar'.<br>5. O sistema recalcula as agregações de dados com base na nova localidade territorial.<br>6. O sistema atualiza a tela do painel exibindo apenas os resultados filtrados. |
| **Fluxos Alternativos** | FA01 - Limpar Filtros: No passo 4, o ator pode clicar em 'Limpar Filtros', fazendo com que o sistema recarregue os dados globais do Estado da Paraíba. |
| **Fluxos de Exceção** | FE01 - Região sem Dados: No passo 5, se o município não tiver inscritos/dados, o sistema exibe os gráficos e tabelas zerados com a mensagem 'Nenhum dado encontrado para a região'. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
