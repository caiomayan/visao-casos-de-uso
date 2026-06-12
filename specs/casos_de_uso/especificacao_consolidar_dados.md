# Especificação de Caso de Uso: Consolidar dados

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC8 - Consolidar dados |
| **Objetivo do Sistema** | Reunir dados de diferentes programas, setores e bases em uma plataforma única. |
| **Requisito Associado** | RF007 |
| **Atores Envolvidos** | Servidor |
| **O que o usuário vê (Elementos de Interface)** | Painel de seleção com caixas de marcação (Checkboxes) listando todos os programas, e uma Tabela final consolidada tipo Planilha (Grid). |
| **O que o usuário insere (Dados Fornecidos)** | Seleção (Click) em quais programas devem ser mesclados e escolha do campo em comum (ex: 'Mesclar por Município'). |
| **Condição de Entrada** | O Servidor necessita cruzar informações de secretarias ou programas distintos. |
| **Fluxo Principal (Passo a Passo)** | 1. O Servidor seleciona a opção 'Cruzamento de Programas'.<br>2. O sistema lista todos os programas com bases de dados ativas.<br>3. O Servidor seleciona 2 ou mais programas e a chave de união.<br>4. O sistema roda a query de união consolidando os números.<br>5. O sistema exibe uma tabela mestre contendo a visão macro. |
| **Fluxos Alternativos / Desvios** | Nenhum fluxo alternativo obrigatório para este caso. |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Bases Incompatíveis: Exibe erro se as estruturas de dados não puderem ser mescladas pela chave escolhida. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
