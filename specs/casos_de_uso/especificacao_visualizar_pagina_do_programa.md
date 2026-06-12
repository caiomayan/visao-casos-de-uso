# Especificação de Caso de Uso: Visualizar pagina do programa

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC10 - Visualizar pagina do programa |
| **Objetivo do Sistema** | Disponibilizar páginas individuais para cada programa social. |
| **Requisito Associado** | RF009 |
| **Atores Envolvidos** | Servidor |
| **O que o usuário vê (Elementos de Interface)** | Uma página completa estilo 'Dashboard de Projeto' com Cabeçalho Textual, Barra de Orçamento preenchida, e abas de navegação (Mapa, Perfil, Ranking). |
| **O que o usuário insere (Dados Fornecidos)** | Navegação via cliques nas Abas superiores. |
| **Condição de Entrada** | O ator clica no nome de um Programa Específico. |
| **Fluxo Principal (Passo a Passo)** | 1. O sistema carrega os metadados do programa (Nome, Data, Eixo).<br>2. O sistema renderiza a tela com as informações descritivas e KPIs focados.<br>3. O Servidor analisa a página.<br>4. O Servidor clica na aba de mapa geográfico [FA01].<br>5. O Servidor clica na aba demográfica de perfis [FA02].<br>6. O Servidor clica na aba de liderança de cidades [FA03]. |
| **Fluxos Alternativos / Desvios** | FA01 - Ver Mapa: Ativa (<<extend>> [UC11 - Visualizar mapa](especificacao_visualizar_mapa.md)).<br>FA02 - Ver Perfis: Ativa (<<extend>> [UC12 - Visualizar dados por perfil](especificacao_visualizar_dados_por_perfil.md)).<br>FA03 - Ver Rankings: Ativa (<<extend>> [UC13 - Visualizar rankings](especificacao_visualizar_rankings.md)). |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Programa Inexistente: Sistema avisa 'Programa não encontrado' caso o link esteja corrompido. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
