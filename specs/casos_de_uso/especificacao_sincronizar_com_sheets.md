# Especificação de Caso de Uso: Sincronizar com Sheets

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC25 - Sincronizar com Sheets |
| **Objetivo** | Recuperar e armazenar dados por meio de integração com a API do Google Sheets enquanto essa for a camada de dados adotada. |
| **Requisitos Relacionados** | RF024 |
| **Atores** | Sistema |
| **Condição de Entrada** | O painel (UC4) necessita de dados novos ou um cronograma (job) roda à meia-noite. |
| **Fluxo Principal** | 1. O backend do sistema inicia o worker de sincronização.<br>2. O sistema autentica usando a Service Account contra a API do Google (OAuth2).<br>3. O sistema requisita o conteúdo JSON da(s) aba(s) da planilha principal da SEDH.<br>4. O sistema parseia as linhas, identifica atualizações de dados e insere as informações estruturadas em seu banco de dados local.<br>5. O sistema atualiza o cache e finaliza o log com 'Sincronização com Sucesso'. |
| **Fluxos Alternativos** | FA01 - Sincronização Sob Demanda: No passo 1, o Servidor aperta o botão manual 'Sincronizar Agora' na interface, forçando a execução da rotina imediatamente. |
| **Fluxos de Exceção** | FE01 - Falha na API: No passo 2, se a API do Google retornar Erro 429 (Too Many Requests), o sistema agenda uma retentativa automática (backoff/retry).<br>FE02 - Colunas Modificadas: No passo 4, se o operador da planilha trocou o nome de uma coluna crítica, o sistema aborta o sync parcial e envia um e-mail de alerta ao Administrador. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
