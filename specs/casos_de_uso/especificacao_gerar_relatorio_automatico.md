# Especificação de Caso de Uso: Gerar relatorio automatico

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC16 - Gerar relatorio automatico |
| **Objetivo** | Gerar relatórios automaticamente, substituindo processos manuais de consolidação e análise de dados. |
| **Requisitos Relacionados** | RF010 |
| **Atores** | Servidor |
| **Condição de Entrada** | O Servidor está consultando um painel ou aba e clica em 'Exportar/Gerar Relatório'. |
| **Fluxo Principal** | 1. O Servidor aciona o comando 'Gerar Relatório'.<br>2. O ator pode optar por customizar as seções do documento [FA01].<br>3. O sistema varre os indicadores, gráficos e tabelas presentes na tela atual.<br>4. O sistema formata os dados em um template padrão governamental, com cabeçalho oficial da SEDH e data.<br>5. O sistema apresenta o relatório estruturado finalizado na tela.<br>6. O ator pode optar por baixar em formato PDF [FA02]. |
| **Fluxos Alternativos** | FA01 - Personalização: No passo 2, o ator engatilha o fluxo opcional (<<extend>> [UC17 - Personalizar relatório](especificacao_personalizar_relatorio.md)).<br>FA02 - PDF: No passo 6, o ator escolhe a saída para download invocando o (<<extend>> [UC18 - Emitir relatório em PDF](especificacao_emitir_relatorio_em_pdf.md)). |
| **Fluxos de Exceção** | FE01 - Timeout de Geração: No passo 3, se o relatório for gigantesco, o sistema avisa: 'Relatório extenso. Enviaremos para o seu e-mail assim que concluir'. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
