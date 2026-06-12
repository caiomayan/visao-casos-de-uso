# Especificação de Caso de Uso: Inscrever-se em programa social

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC20 - Inscrever-se em programa social |
| **Objetivo do Sistema** | Realizar cadastro via preenchimento digital de informações. |
| **Requisito Associado** | RF021 |
| **Atores Envolvidos** | Cidadão |
| **O que o usuário vê (Elementos de Interface)** | Formulário sequencial estruturado em etapas (Stepper: Passo 1 - Pessoal, Passo 2 - Contato, Passo 3 - Anexos). Um campo de File Upload em área tracejada para arquivos. |
| **O que o usuário insere (Dados Fornecidos)** | Textos (Nome Completo, Identidade, Renda), CPF, Seleção Sim/Não em questionário socioeconômico e envio físico (Upload) de arquivos PDF ou JPG. |
| **Condição de Entrada** | O cidadão aceitou os termos e quer enviar sua solicitação. |
| **Fluxo Principal (Passo a Passo)** | 1. O cidadão clica em Inscrição. O sistema trava a tela e exige login do governo (<<include>> [UC1 - Realizar login](especificacao_realizar_login.md)).<br>2. O cidadão insere os dados da Ficha de Solicitação.<br>3. Ao preencher o CPF, há disparo de evento Javascript que o envia à checagem de banco da SEDH (<<include>> [UC3 - Validar CPF](especificacao_validar_cpf.md)).<br>4. O cidadão faz o Upload das fotos de Comprovante de Endereço ou Laudos.<br>5. O cidadão clica em 'Finalizar Inscrição'.<br>6. O sistema exibe modal verde com número de protocolo final. |
| **Fluxos Alternativos / Desvios** | FA01 - Salvar Rascunho Automático: Se o usuário fechar a aba no Passo 2 e voltar amanhã, o sistema preserva os campos no LocalStorage. |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Arquivo Muito Grande: Ao enviar o PDF no passo 4, sistema grita 'Tamanho máximo de 5MB ultrapassado' e bloqueia finalização. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
