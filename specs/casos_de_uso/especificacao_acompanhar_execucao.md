# Especificação de Caso de Uso: Acompanhar execucao

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC9 - Acompanhar execucao |
| **Objetivo do Sistema** | Permitir o acompanhamento dos programas sociais executados pela SEDH. |
| **Requisito Associado** | RF008 |
| **Atores Envolvidos** | Servidor |
| **O que o usuário vê (Elementos de Interface)** | Tabela com lista de programas contendo Nome, Responsável, Orçamento Gasto (%) e Status colorido. |
| **O que o usuário insere (Dados Fornecidos)** | Campo de pesquisa por texto (Nome do programa) e Clique para acessar detalhes. |
| **Condição de Entrada** | O Servidor acessa a listagem de Programas. |
| **Fluxo Principal (Passo a Passo)** | 1. O Servidor abre a aba 'Monitoramento de Execução'.<br>2. O sistema exibe a lista de todos os programas ativos com status geral.<br>3. O Servidor clica em um programa específico.<br>4. O sistema direciona para (<<include>> [UC10 - Visualizar pagina do programa](especificacao_visualizar_pagina_do_programa.md)).<br>5. O Servidor verifica a taxa de conversão (Inscritos vs Beneficiados).<br>6. O Servidor solicita geração de relatório do acompanhamento [FA01]. |
| **Fluxos Alternativos / Desvios** | FA01 - Gerar Relatório: Dispara (<<include>> [UC16 - Gerar relatorio automatico](especificacao_gerar_relatorio_automatico.md)). |
| **Fluxos de Exceção (Erros e Limites)** | Nenhuma validação de exceção. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
