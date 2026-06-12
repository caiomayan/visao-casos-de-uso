# Especificação de Caso de Uso: Emitir relatorio em PDF

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC18 - Emitir relatorio em PDF |
| **Objetivo** | Permitir a emissão de relatórios em PDF de forma rápida, com base nos filtros e configurações escolhidos pelo usuário. |
| **Requisitos Relacionados** | RF012 |
| **Atores** | Servidor |
| **Condição de Entrada** | O relatório finalizado está na tela aguardando a decisão de exportação. |
| **Fluxo Principal** | 1. O Servidor clica em 'Baixar como PDF'.<br>2. O sistema envia o HTML consolidado para um serviço de conversão (ex: wkhtmltopdf ou jsPDF).<br>3. O sistema gera o arquivo físico `.pdf`.<br>4. O sistema dispara o download para o navegador do Servidor. |
| **Fluxos Alternativos** | FA01 - Adicionar Marca d'água: No passo 2, o sistema detecta se é uma versão preliminar e carimba 'Confidencial/Rascunho' no fundo do PDF. |
| **Fluxos de Exceção** | FE01 - Bloqueio de Popup: No passo 4, se o navegador bloquear o download, o sistema exibe um link estático: 'Clique aqui para baixar seu arquivo'. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
