# Especificação de Caso de Uso: Filtrar dados

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC5 - Filtrar dados |
| **Objetivo do Sistema** | Permitir filtrar os dados por município e por regional. |
| **Requisito Associado** | RF004 |
| **Atores Envolvidos** | Servidor |
| **O que o usuário vê (Elementos de Interface)** | Modal ou Menu Lateral contendo Caixas de Seleção (Dropdowns) listando Municípios e Regionais de Atendimento. |
| **O que o usuário insere (Dados Fornecidos)** | Seleção de um ou múltiplos municípios, Seleção de regional. |
| **Condição de Entrada** | O Servidor está no painel de indicadores. |
| **Fluxo Principal (Passo a Passo)** | 1. O Servidor clica no botão 'Filtros Avançados'.<br>2. O sistema abre o modal contendo as opções geográficas.<br>3. O Servidor seleciona uma ou mais opções nos campos.<br>4. O Servidor clica em 'Aplicar'.<br>5. O sistema recalcula as agregações e atualiza os gráficos do painel. |
| **Fluxos Alternativos / Desvios** | FA01 - Limpar Filtros: O ator clica em 'Limpar Filtros' para recarregar a visão global do Estado. |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Região sem Dados: O sistema exibe gráficos zerados com 'Nenhum dado encontrado' se o município não tiver programas ativos. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
