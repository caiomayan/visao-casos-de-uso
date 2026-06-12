# Especificação de Caso de Uso: Acompanhar execucao

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC9 - Acompanhar execucao |
| **Objetivo** | Permitir o acompanhamento dos programas sociais executados pela SEDH, incluindo informações sobre beneficiários, execução das políticas e dados territoriais. |
| **Requisitos Relacionados** | RF008 |
| **Atores** | Servidor |
| **Condição de Entrada** | O Servidor acessa a listagem de Programas em Andamento. |
| **Fluxo Principal** | 1. O Servidor abre a aba 'Monitoramento de Execução'.<br>2. O sistema exibe a lista de todos os programas ativos sob responsabilidade da SEDH, com status geral (Dentro da meta / Atrasado).<br>3. O Servidor clica em um programa específico da lista.<br>4. O sistema direciona para a página detalhada do programa (<<include>> [UC10 - Visualizar página do programa](especificacao_visualizar_pagina_do_programa.md)).<br>5. O Servidor verifica a taxa de conversão (Inscritos vs Beneficiados) e o orçamento executado.<br>6. O Servidor pode solicitar geração de um relatório de execução [FA01]. |
| **Fluxos Alternativos** | FA01 - Gerar Relatório do Programa: No passo 6, o ator aciona o atalho, o que desencadeia (<<include>> [UC16 - Gerar relatório automático](especificacao_gerar_relatorio_automatico.md)). |
| **Fluxos de Exceção** | Não existem fluxos de exceção críticos para este caso de uso. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
