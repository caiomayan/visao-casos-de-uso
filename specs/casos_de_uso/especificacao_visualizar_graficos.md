# Especificação de Caso de Uso: Visualizar graficos

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC6 - Visualizar graficos |
| **Objetivo do Sistema** | Exibir gráficos para facilitar a interpretação dos dados ao longo do tempo. |
| **Requisito Associado** | RF005 |
| **Atores Envolvidos** | Servidor |
| **O que o usuário vê (Elementos de Interface)** | Área central desenhando gráficos de barras (comparativos) e linhas (evolução temporal), com legendas dinâmicas. |
| **O que o usuário insere (Dados Fornecidos)** | Cliques em botões de filtro gráfico (ex: Mudar para formato 'Pizza') e movimento do mouse sobre os gráficos (efeito Hover) para ler números exatos. |
| **Condição de Entrada** | O Servidor solicitou a visualização gráfica no Painel. |
| **Fluxo Principal (Passo a Passo)** | 1. O sistema compila o conjunto atual de dados em arrays para plotagem.<br>2. O sistema carrega a biblioteca de renderização gráfica.<br>3. O sistema exibe um gráfico de barras comparativo entre municípios.<br>4. O sistema exibe um gráfico de linhas mostrando a evolução nos últimos 12 meses.<br>5. O Servidor passa o mouse sobre os gráficos para consultar valores pontuais. |
| **Fluxos Alternativos / Desvios** | FA01 - Alternar Gráfico: No passo 3, trocar formato de barras para pizza. |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Erro de Renderização: Fallback exibindo tabela plana caso o plugin de gráficos não carregue. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
