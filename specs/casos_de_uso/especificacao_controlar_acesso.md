# Especificação de Caso de Uso: Controlar acesso

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC2 - Controlar acesso |
| **Objetivo do Sistema** | Controlar o acesso dos usuários conforme sessões, perfis e permissões. |
| **Requisito Associado** | RF002 |
| **Atores Envolvidos** | Admin, Sistema |
| **O que o usuário vê (Elementos de Interface)** | Tela solicitada renderizada normalmente ou Tela de Erro 403 (Acesso Negado) caso seja bloqueado. |
| **O que o usuário insere (Dados Fornecidos)** | Nenhum (validação transparente de sessão/cookie em background). |
| **Condição de Entrada** | O ator tenta acessar uma rota ou módulo protegido do sistema. |
| **Fluxo Principal (Passo a Passo)** | 1. O ator solicita o acesso a um módulo restrito.<br>2. O sistema intercepta a requisição e verifica o token de sessão ativo.<br>3. O sistema consulta as permissões vinculadas ao perfil do ator.<br>4. O sistema confirma que o perfil possui acesso àquele recurso.<br>5. O sistema carrega e exibe o módulo solicitado. |
| **Fluxos Alternativos / Desvios** | FA01 - Perfil com Restrição Parcial: No passo 4, se tiver permissão apenas de leitura, o sistema oculta botões de edição. |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Acesso Negado: No passo 4, se não tiver permissão, o sistema exibe 'Acesso Negado (403)' e bloqueia o recurso. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
