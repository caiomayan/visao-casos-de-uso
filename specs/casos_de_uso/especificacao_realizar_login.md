# Especificação de Caso de Uso: Realizar login

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC1 - Realizar login |
| **Objetivo** | Permitir que usuários realizem login para acessar as áreas internas da plataforma, especialmente dashboards, relatórios, gestão e módulos administrativos. |
| **Requisitos Relacionados** | RF001 |
| **Atores** | Cidadão, Servidor, Admin |
| **Condição de Entrada** | O ator não está autenticado no sistema. |
| **Fluxo Principal** | 1. O ator acessa a página inicial do sistema e clica em 'Entrar'.<br>2. O sistema redireciona para a tela de autenticação do Clerk.<br>3. O ator informa suas credenciais (E-mail e Senha) ou escolhe o login via provedor externo.<br>4. O Clerk valida as credenciais.<br>5. O sistema recebe o token de autenticação, registra a sessão e redireciona o ator para o painel apropriado. |
| **Fluxos Alternativos** | FA01 - Esqueci a Senha: No passo 3, o ator clica em 'Esqueci minha senha', e o sistema envia um e-mail de recuperação. |
| **Fluxos de Exceção** | FE01 - Credenciais Inválidas: No passo 4, se a senha for incorreta, o sistema exibe 'Usuário ou senha inválidos' e permite tentar novamente. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
