# Especificação de Caso de Uso: Visualizar painel

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC4 - Visualizar painel |
| **Objetivo do Sistema** | Apresentar um painel principal com indicadores consolidados. |
| **Requisito Associado** | RF003 |
| **Atores Envolvidos** | Servidor |
| **O que o usuário vê (Elementos de Interface)** | Painel de controle com cartões de indicadores (KPIs de inscritos/orçamento), menus laterais e barra superior. |
| **O que o usuário insere (Dados Fornecidos)** | Cliques para navegação nas abas, e seleção de parâmetros nos menus de filtro. |
| **Condição de Entrada** | O Servidor acessa o endereço principal do Dashboard. |
| **Fluxo Principal (Passo a Passo)** | 1. O Servidor efetua o login (<<include>> [UC1 - Realizar login](especificacao_realizar_login.md)).<br>2. O sistema valida as permissões (<<include>> [UC2 - Controlar acesso](especificacao_controlar_acesso.md)).<br>3. O sistema requisita a atualização de dados externos (<<include>> [UC25 - Sincronizar com Sheets](especificacao_sincronizar_com_sheets.md)).<br>4. O sistema renderiza a tela principal com os cartões de indicadores globais.<br>5. O Servidor visualiza os resumos socioeconômicos.<br>6. O Servidor opta por visualizar os gráficos detalhados [FA01].<br>7. O Servidor opta por filtrar os dados [FA02].<br>8. O Servidor opta por consolidar programas específicos [FA03]. |
| **Fluxos Alternativos / Desvios** | FA01 - Gráficos: Ativa (<<include>> [UC6 - Visualizar graficos](especificacao_visualizar_graficos.md)).<br>FA02 - Filtros: Ativa (<<include>> [UC5 - Filtrar dados](especificacao_filtrar_dados.md)).<br>FA03 - Consolidar: Ativa (<<include>> [UC8 - Consolidar dados](especificacao_consolidar_dados.md)). |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Falha no Carregamento: Exibe aviso de 'Dados indisponíveis'. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
