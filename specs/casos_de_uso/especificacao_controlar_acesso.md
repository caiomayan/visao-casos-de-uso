# Especificação de Caso de Uso: Controlar acesso

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC2 - Controlar acesso |
| **Objetivo** | Controlar o acesso dos usuários conforme sessões, perfis e permissões, impedindo que usuários não autorizados acessem funcionalidades restritas. |
| **Requisitos Relacionados** | RF002 |
| **Atores** | Admin, Sistema |
| **Condição de Entrada** | O ator tenta acessar uma rota ou módulo protegido do sistema. |
| **Fluxo Principal** | 1. O ator solicita o acesso a um módulo restrito (ex: Painel de Indicadores).<br>2. O sistema intercepta a requisição e verifica o token de sessão ativo.<br>3. O sistema consulta as permissões vinculadas ao perfil do ator.<br>4. O sistema confirma que o perfil possui acesso àquele recurso.<br>5. O sistema carrega e exibe o módulo solicitado. |
| **Fluxos Alternativos** | FA01 - Perfil com Restrição Parcial: No passo 4, se o ator tiver permissão apenas de leitura, o sistema oculta botões de edição/exclusão na tela carregada. |
| **Fluxos de Exceção** | FE01 - Acesso Negado: No passo 4, se o ator não tiver permissão, o sistema exibe a página de 'Acesso Negado (Erro 403)' e bloqueia o recurso. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
