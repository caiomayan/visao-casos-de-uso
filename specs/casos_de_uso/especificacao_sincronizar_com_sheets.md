# Especificação de Caso de Uso: Sincronizar com Sheets

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC25 - Sincronizar com Sheets |
| **Objetivo do Sistema** | Atualização e integração com API de fontes externas. |
| **Requisito Associado** | RF024 |
| **Atores Envolvidos** | Sistema |
| **O que o usuário vê (Elementos de Interface)** | Visão técnica invisível de background. Para administradores, apenas um painel de Logs de Status confirmando Data do Último Sync bem-sucedido. |
| **O que o usuário insere (Dados Fornecidos)** | Absolutamente nenhum input de teclado requerido, é máquina falando com máquina (M2M) exceto credenciais pré-programadas do GCP (Google Cloud Project). |
| **Condição de Entrada** | Job agendado é iniciado (CRON) ou disparo forçado na interface de Administrador. |
| **Fluxo Principal (Passo a Passo)** | 1. O servidor Node.js/Python acorda e inicia o script de Worker em fila de processamento.<br>2. O sistema realiza handshake JWT autenticando o serviço perante o servidor das APIs Cloud do Google.<br>3. O sistema roda método GET requerendo os blocos de dados de formato aberto na planilha central das SEDH.<br>4. A API devolve o JSON; O sistema detecta colunas inalteradas (fazendo parse rápido) e detecta atualizações, salvando no banco POSTGRESQL ou Mongo nativo.<br>5. O sistema termina silenciosamente e marca log verde (Sucesso) pro Dashboard UC4 acessar atualizado imediatamente. |
| **Fluxos Alternativos / Desvios** | FA01 - Botão Manual: O Admin vai no submódulo e clica em Forçar Atualização Imediata (Trigger Sync), bypassando a rotina da noite. |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Limite Google: Erro 429 Too Many Requests emitido pelo Google, script aciona protocolo 'Backoff Exponencial' de retentativa 5 min depois.<br>FE02 - Planilha Corrompida ou Alterada por Humano Inadequado: As colunas sumiram. O Worker cancela o Sync parcial pra não estragar banco atual e joga alerta. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
