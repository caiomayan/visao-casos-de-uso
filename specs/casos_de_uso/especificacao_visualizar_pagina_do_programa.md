# Especificação de Caso de Uso: Visualizar pagina do programa

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC10 - Visualizar pagina do programa |
| **Objetivo** | Disponibilizar páginas individuais para cada programa social, contendo dados quantitativos, informações descritivas, gráficos, rankings e análises próprias. |
| **Requisitos Relacionados** | RF009 |
| **Atores** | Servidor |
| **Condição de Entrada** | O ator clica em um cartão ou link de um Programa Específico. |
| **Fluxo Principal** | 1. O sistema carrega os metadados do programa (Nome, Data de Criação, Eixo de Atuação).<br>2. O sistema renderiza a tela com as informações descritivas e os KPIs isolados desse programa.<br>3. O Servidor analisa a página.<br>4. O Servidor pode desejar ver os dados projetados num mapa [FA01].<br>5. O Servidor pode desejar cruzar com perfis demográficos [FA02].<br>6. O Servidor pode consultar o ranking de cidades que mais utilizam [FA03]. |
| **Fluxos Alternativos** | FA01 - Ver Mapa: No passo 4, o ator clica na aba 'Geolocalização', ativando a extensão (<<extend>> [UC11 - Visualizar mapa](especificacao_visualizar_mapa.md)).<br>FA02 - Ver Perfis: No passo 5, o ator clica na aba 'Demografia', ativando a extensão (<<extend>> [UC12 - Visualizar dados por perfil](especificacao_visualizar_dados_por_perfil.md)).<br>FA03 - Ver Rankings: No passo 6, o ator clica na aba 'Leaderboard', ativando a extensão (<<extend>> [UC13 - Visualizar rankings](especificacao_visualizar_rankings.md)). |
| **Fluxos de Exceção** | FE01 - Programa Inexistente: No passo 1, se o ID do programa for inválido, o sistema redireciona para a lista geral com mensagem 'Programa não encontrado'. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
