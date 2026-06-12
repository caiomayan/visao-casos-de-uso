# Especificação de Caso de Uso: Visualizar painel

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC4 - Visualizar painel |
| **Objetivo** | Apresentar um painel principal com indicadores demográficos, sociais e econômicos consolidados, permitindo uma visão estratégica dos dados da SEDH. |
| **Requisitos Relacionados** | RF003 |
| **Atores** | Servidor |
| **Condição de Entrada** | O Servidor acessa o endereço principal do Dashboard. |
| **Fluxo Principal** | 1. O Servidor efetua o login (<<include>> [UC1 - Realizar login](especificacao_realizar_login.md)).<br>2. O sistema valida as permissões (<<include>> [UC2 - Controlar acesso](especificacao_controlar_acesso.md)).<br>3. O sistema requisita a atualização de dados externos (<<include>> [UC25 - Sincronizar com Sheets](especificacao_sincronizar_com_sheets.md)).<br>4. O sistema renderiza a tela principal com os cartões de indicadores (KPIs globais).<br>5. O Servidor visualiza os resumos socioeconômicos.<br>6. O Servidor opta por visualizar os gráficos detalhados [FA01].<br>7. O Servidor opta por filtrar os dados [FA02].<br>8. O Servidor opta por consolidar programas específicos [FA03]. |
| **Fluxos Alternativos** | FA01 - Visualizar Gráficos: No passo 6, o ator aciona a funcionalidade de gráficos, engatilhando o (<<include>> [UC6 - Visualizar gráficos](especificacao_visualizar_graficos.md)).<br>FA02 - Aplicar Filtros: No passo 7, o ator expande a barra lateral e aplica recortes territoriais (<<include>> [UC5 - Filtrar dados](especificacao_filtrar_dados.md)).<br>FA03 - Consolidar Múltiplos Programas: No passo 8, o ator seleciona mais de um programa para cruzar dados (<<include>> [UC8 - Consolidar dados](especificacao_consolidar_dados.md)). |
| **Fluxos de Exceção** | FE01 - Falha no Carregamento: No passo 4, se o banco de dados falhar, o sistema apresenta um aviso de 'Dados indisponíveis no momento' com botão de retentativa. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
