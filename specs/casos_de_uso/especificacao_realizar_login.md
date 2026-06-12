# Especificação de Caso de Uso: Realizar login

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC1 - Realizar login |
| **Objetivo do Sistema** | Permitir que usuários realizem login para acessar as áreas internas da plataforma, especialmente dashboards, relatórios, gestão e módulos administrativos. |
| **Requisito Associado** | RF001 |
| **Atores Envolvidos** | Cidadão, Servidor, Admin |
| **O que o usuário vê (Elementos de Interface)** | Tela de Login contendo campos para e-mail e senha, botão de confirmação e link de recuperação. |
| **O que o usuário insere (Dados Fornecidos)** | E-mail de acesso, Senha. |
| **Condição de Entrada** | O ator não está autenticado no sistema. |
| **Fluxo Principal (Passo a Passo)** | 1. O ator acessa a página inicial do sistema e clica em 'Entrar'.<br>2. O sistema redireciona para a tela de autenticação do Clerk.<br>3. O ator informa suas credenciais (E-mail e Senha) ou escolhe o login via provedor externo.<br>4. O Clerk valida as credenciais.<br>5. O sistema recebe o token de autenticação, registra a sessão e redireciona o ator para o painel apropriado. |
| **Fluxos Alternativos / Desvios** | FA01 - Esqueci a Senha: No passo 3, o ator clica em 'Esqueci minha senha', e o sistema envia um e-mail de recuperação. |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Credenciais Inválidas: No passo 4, se a senha for incorreta, o sistema exibe 'Usuário ou senha inválidos'. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
