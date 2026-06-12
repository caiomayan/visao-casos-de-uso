# Especificação de Caso de Uso: Gerar relatorio automatico

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC16 - Gerar relatorio automatico |
| **Objetivo do Sistema** | Gerar relatórios de tela automaticamente substituindo tarefas manuais. |
| **Requisito Associado** | RF010 |
| **Atores Envolvidos** | Servidor |
| **O que o usuário vê (Elementos de Interface)** | Visão Prévia (Preview) formatada em uma moldura A4 na tela, incluindo o Brasão oficial do Estado no cabeçalho e os gráficos e tabelas compilados no corpo da página. |
| **O que o usuário insere (Dados Fornecidos)** | Botões de topo de barra para 'Personalizar Estrutura', 'Imprimir' e 'Baixar em PDF'. |
| **Condição de Entrada** | O Servidor está analisando um painel e deseja extrair o panorama em formato documento. |
| **Fluxo Principal (Passo a Passo)** | 1. O Servidor aperta o botão flutuante 'Gerar Relatório Oficial'.<br>2. O Servidor pode personalizar o conteúdo do documento [FA01].<br>3. O sistema captura nativamente o estado atual do painel (tabelas e gráficos formatados).<br>4. O sistema envelopa isso no Template Oficial da SEDH e exibe no formato A4 em tela.<br>5. O Servidor encerra pedindo a exportação para seu computador [FA02]. |
| **Fluxos Alternativos / Desvios** | FA01 - Personalizar: Ativa menu lateral via (<<extend>> [UC17 - Personalizar relatorio](especificacao_personalizar_relatorio.md)).<br>FA02 - Emitir PDF: Inicia o fluxo de arquivo via (<<extend>> [UC18 - Emitir relatorio em PDF](especificacao_emitir_relatorio_em_pdf.md)). |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Tempo Excedido: Se as tabelas ultrapassarem centenas de páginas, ele exibe um loader e promete envio via e-mail corporativo em background. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
