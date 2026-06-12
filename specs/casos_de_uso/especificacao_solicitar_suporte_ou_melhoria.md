# Especificação de Caso de Uso: Solicitar suporte ou melhoria

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC21 - Solicitar suporte ou melhoria |
| **Objetivo** | Permitir que usuários solicitem suporte técnico, inclusão de dados ou sugiram melhorias na plataforma. |
| **Requisitos Relacionados** | RF019 |
| **Atores** | Cidadão |
| **Condição de Entrada** | O ator (Cidadão ou até Servidor) encontra um problema ou deseja opinar. |
| **Fluxo Principal** | 1. O ator acessa o link 'Ajuda e Suporte' (ícone de interrogação flutuante ou rodapé).<br>2. O sistema exibe um formulário de abertura de chamado com Categorias (Dúvida, Sugestão de Melhoria, Reportar Erro).<br>3. O ator preenche o Assunto, descreve o problema e, se quiser, anexa uma captura de tela (print).<br>4. O ator envia a solicitação.<br>5. O sistema registra na fila do administrador e exibe o Número do Ticket na tela. |
| **Fluxos Alternativos** | FA01 - Base de Conhecimento Rápida: No passo 2, ao digitar o Assunto, o sistema sugere FAQs automaticamente, e o usuário pode fechar o chamado se já estiver respondido ali. |
| **Fluxos de Exceção** | Não existem fluxos de exceção críticos para este caso de uso. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
