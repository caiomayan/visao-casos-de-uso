# Especificação de Caso de Uso: Inscrever-se em programa social

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC20 - Inscrever-se em programa social |
| **Objetivo** | Permitir, na área destinada ao cidadão, a realização de inscrições para participação em iniciativas ofertadas pela SEDH. |
| **Requisitos Relacionados** | RF021 |
| **Atores** | Cidadão |
| **Condição de Entrada** | O cidadão leu o edital e deseja solicitar entrada no benefício. |
| **Fluxo Principal** | 1. O cidadão aciona 'Inscrever-se'. O sistema exige autenticação (<<include>> [UC1 - Realizar login](especificacao_realizar_login.md)).<br>2. O sistema carrega o formulário dinâmico do programa em etapas (Wizard).<br>3. O cidadão preenche dados pessoais, residenciais e anexa comprovantes.<br>4. Ao inserir o CPF, o sistema valida na hora (<<include>> [UC3 - Validar CPF](especificacao_validar_cpf.md)).<br>5. O cidadão revisa o resumo e clica em 'Enviar Inscrição'.<br>6. O sistema salva na base, muda o status para 'Em Análise' e gera um número de protocolo. |
| **Fluxos Alternativos** | FA01 - Salvar Rascunho: No passo 3, o cidadão decide parar na metade e clica em 'Salvar e continuar depois', guardando os dados parciais. |
| **Fluxos de Exceção** | FE01 - Falta de Arquivo Obrigatório: No passo 5, o sistema acusa erro vermelho 'O envio do Comprovante de Residência é obrigatório'. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
