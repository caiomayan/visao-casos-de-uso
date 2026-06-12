# Especificação de Caso de Uso: Visualizar dados por perfil

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC12 - Visualizar dados por perfil |
| **Objetivo** | Permitir a visualização dos dados por município, região e perfil socioeconômico, apoiando decisões baseadas no território. |
| **Requisitos Relacionados** | RF014 |
| **Atores** | Servidor |
| **Condição de Entrada** | O ator ativa a aba de Análise de Perfis. |
| **Fluxo Principal** | 1. O sistema consulta as tabelas de inscritos do programa.<br>2. O sistema separa os agregados por Idade, Gênero, Faixa de Renda e Nível de Escolaridade.<br>3. O sistema exibe gráficos demográficos específicos.<br>4. O Servidor avalia qual faixa populacional está sendo mais impactada. |
| **Fluxos Alternativos** | FA01 - Exportar CSV de Perfil: No passo 3, o ator pode clicar em 'Baixar Microdados' para obter a tabela CSV correspondente. |
| **Fluxos de Exceção** | Não existem fluxos de exceção críticos para este caso de uso. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
