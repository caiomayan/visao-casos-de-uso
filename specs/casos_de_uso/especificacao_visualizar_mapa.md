# Especificação de Caso de Uso: Visualizar mapa

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC11 - Visualizar mapa |
| **Objetivo do Sistema** | Visualizar a distribuição espacial dos programas no território paraibano. |
| **Requisito Associado** | RF013 |
| **Atores Envolvidos** | Servidor |
| **O que o usuário vê (Elementos de Interface)** | Mapa da Paraíba renderizado (ex: Google Maps API), com as fronteiras das cidades pintadas com intensidade de cor variada (escala de calor). |
| **O que o usuário insere (Dados Fornecidos)** | Movimentos de Rolagem (Zoom in/Zoom out) e Cliques em cima do polígono do Município escolhido. |
| **Condição de Entrada** | O ator ativa a visão de mapa. |
| **Fluxo Principal (Passo a Passo)** | 1. O sistema inicia o módulo de mapa coroplético focado na Paraíba.<br>2. O sistema busca coordenadas geográficas e pinta os municípios.<br>3. O Servidor aproxima e clica no município de Campina Grande, por exemplo.<br>4. O sistema sobrepõe um Tooltip/Pop-up com o total exato de investimentos na cidade escolhida. |
| **Fluxos Alternativos / Desvios** | FA01 - Visão Satélite: Ator alterna o botão de camada de mapa para 'Satélite'. |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Ausência de Polígono: Se faltarem coordenadas geográficas de uma cidade, ela é listada isoladamente numa tabela abaixo do mapa. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
