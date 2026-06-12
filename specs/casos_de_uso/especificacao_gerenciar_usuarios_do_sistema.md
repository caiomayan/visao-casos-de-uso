# Especificação de Caso de Uso: Gerenciar usuarios do sistema

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC22 - Gerenciar usuarios do sistema |
| **Objetivo do Sistema** | Ajuste e controle base de acesso de servidores públicos na infraestrutura de software. |
| **Requisito Associado** | RF017 |
| **Atores Envolvidos** | Administrador |
| **O que o usuário vê (Elementos de Interface)** | Tabela crua (Data Grid) listando os nomes dos funcionários públicos do Estado e seus níveis de Perfil no sistema. Modal (janela sobreposta) com o Formulário de Criação. |
| **O que o usuário insere (Dados Fornecidos)** | Campos de texto para Nome/Email; Botão 'Desativar Conta'; Caixas Dropdown listando os perfis técnicos ('Assistente', 'Gestor Regional', etc). |
| **Condição de Entrada** | O Administrador Master abre o Painel Configurações de Pessoas. |
| **Fluxo Principal (Passo a Passo)** | 1. O sistema assegura que só Masters entrem aqui (<<include>> [UC2 - Controlar acesso](especificacao_controlar_acesso.md)).<br>2. O Administrador observa a grade de contas.<br>3. O Administrador aciona 'Adicionar Novo Usuário'.<br>4. O Admin fornece E-mail Institucional e amarra ao perfil operacional correto.<br>5. O sistema faz interface com o provedor de identidade (Clerk) criando o perfil, e dispara notificação de boas-vindas na caixa de e-mail do servidor listado. |
| **Fluxos Alternativos / Desvios** | FA01 - Bloqueio Emergencial: Em vez de criar conta, o admin acha o e-mail de um ex-funcionário na grid e clica no ícone de lixeira. O sistema imediatamente derruba a sessão logada dele. |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Duplicidade de E-mail de Servidor: 'E-mail corporativo fornecido já consta atrelado a outra conta'. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
