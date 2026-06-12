# Especificação de Caso de Uso: Gerenciar usuarios do sistema

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC22 - Gerenciar usuarios do sistema |
| **Objetivo** | Permitir a gestão de usuários, incluindo cadastro, edição, controle de acesso e configuração de permissões. |
| **Requisitos Relacionados** | RF017 |
| **Atores** | Administrador |
| **Condição de Entrada** | O Administrador acessa a aba de Painel de Controle de Usuários. |
| **Fluxo Principal** | 1. O sistema assegura o privilégio master (<<include>> [UC2 - Controlar acesso](especificacao_controlar_acesso.md)).<br>2. O sistema lista a grid de usuários internos (Servidores/Assistentes) cadastrados na SEDH.<br>3. O Administrador clica em 'Adicionar Novo Usuário'.<br>4. O Admin preenche o e-mail, nome e seleciona a Role/Perfil (Ex: Assistente, Gestor Regional).<br>5. O sistema dispara um convite por e-mail para a pessoa criar a senha. |
| **Fluxos Alternativos** | FA01 - Desativar Acesso (Offboarding): No passo 2, o Admin seleciona um usuário existente e clica em 'Revogar Acesso', bloqueando login imediato.<br>FA02 - Editar Permissões: No passo 2, o Admin acessa o perfil de alguém e adiciona/remove módulos específicos. |
| **Fluxos de Exceção** | FE01 - E-mail Duplicado: No passo 4, se o usuário já existir, o sistema exibe 'Este servidor já possui cadastro'. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
