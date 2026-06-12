# Especificação de Caso de Uso: Avaliar inscricoes

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC14 - Avaliar inscricoes |
| **Objetivo** | Possuir funcionalidades relacionadas à avaliação de inscrições em programas ou iniciativas da SEDH. |
| **Requisitos Relacionados** | RF016 |
| **Atores** | Assistente Social |
| **Condição de Entrada** | Existem cidadãos que solicitaram entrada em um programa social e o Assistente está logado. |
| **Fluxo Principal** | 1. A Assistente Social abre a fila de 'Solicitações Pendentes'.<br>2. O sistema exibe a ficha completa preenchida pelo Cidadão, junto aos documentos anexados.<br>3. A Assistente analisa a veracidade e pertinência dos dados segundo os critérios do programa.<br>4. A Assistente clica em 'Aprovar' ou 'Rejeitar'.<br>5. O sistema solicita uma justificativa se for rejeição [FA01].<br>6. O sistema altera o status da inscrição e notifica o cidadão. |
| **Fluxos Alternativos** | FA01 - Justificar Rejeição: No passo 5, um campo de texto obrigatório é exibido para embasamento legal da recusa.<br>FA02 - Solicitar Mais Documentos: No passo 4, em vez de Aprovar/Rejeitar, a Assistente escolhe 'Pendente - Documento', devolvendo o status para o cidadão sem recusar. |
| **Fluxos de Exceção** | FE01 - Anexos Corrompidos: No passo 2, se os arquivos (PDF/Imagens) enviados não abrirem, a Assistente aciona o fluxo FA02. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
