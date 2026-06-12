# Especificação de Caso de Uso: Avaliar inscricoes

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC14 - Avaliar inscricoes |
| **Objetivo do Sistema** | Análise de inscrições submetidas por cidadãos. |
| **Requisito Associado** | RF016 |
| **Atores Envolvidos** | Assistente Social |
| **O que o usuário vê (Elementos de Interface)** | Tela dividida: Lado esquerdo exibe as respostas do formulário (Nome, Renda Informada); Lado direito exibe as fotos ou PDFs dos comprovantes para auditoria visual. Botões verde (Aprovar) e vermelho (Rejeitar). |
| **O que o usuário insere (Dados Fornecidos)** | Cliques nos botões de Aprovar/Rejeitar; Preenchimento da caixa de texto (textarea) para inserir o Motivo da Recusa Técnica. |
| **Condição de Entrada** | O cidadão enviou a inscrição (via UC20) e ela encontra-se na Fila de Análise. |
| **Fluxo Principal (Passo a Passo)** | 1. A Assistente Social abre a fila de 'Solicitações Pendentes'.<br>2. O sistema exibe o painel de avaliação unificado com documentos anexados abertos nativamente no lado direito da tela.<br>3. A Assistente lê e confronta o que foi digitado com o que foi anexado.<br>4. A Assistente clica em 'Aprovar' ou 'Rejeitar'.<br>5. Se rejeitar, o sistema exige uma justificativa de texto [FA01].<br>6. O sistema grava o status auditado e notifica o Cidadão por e-mail. |
| **Fluxos Alternativos / Desvios** | FA01 - Exigir Justificativa: No passo 5, trava o avanço até o ator justificar legalmente a recusa.<br>FA02 - Solicitar Reenvio (Pendente): Em vez de rejeitar de vez, o ator clica em 'Pedir Novo Documento', deixando o ticket em suspenso. |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Anexo Corrompido: A imagem enviada pelo cidadão não carrega, forçando o acionamento automático da pendência via FA02. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
