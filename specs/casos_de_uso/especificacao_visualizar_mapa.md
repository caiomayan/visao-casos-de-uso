# Especificação de Caso de Uso: Visualizar mapa

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC11 - Visualizar mapa |
| **Objetivo** | Disponibilizar mapas para visualizar a distribuição dos programas sociais no território paraibano. |
| **Requisitos Relacionados** | RF013 |
| **Atores** | Servidor |
| **Condição de Entrada** | O ator ativa a visão de mapa de um Programa Específico. |
| **Fluxo Principal** | 1. O sistema inicia o módulo de mapa coroplético (Leaflet/Google Maps API) focado no Estado da Paraíba.<br>2. O sistema busca as coordenadas geográficas dos municípios que possuem o programa ativo.<br>3. O sistema pinta os polígonos dos municípios com base na densidade de inscritos (escalas de calor).<br>4. O Servidor dá um zoom e clica em uma cidade específica.<br>5. O sistema exibe um tooltip/pop-up com os números precisos daquela localidade. |
| **Fluxos Alternativos** | FA01 - Alternar Camada de Satélite: No passo 1, o ator pode mudar a visualização padrão para Mapa de Satélite. |
| **Fluxos de Exceção** | FE01 - Erro de Geolocalização: No passo 3, se faltarem dados geográficos (GeoJSON), o sistema exibe os municípios faltando como 'Desconhecidos' fora do mapa. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
