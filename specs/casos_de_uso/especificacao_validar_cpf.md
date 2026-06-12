# Especificação de Caso de Uso: Validar CPF

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC3 - Validar CPF |
| **Objetivo do Sistema** | Utilizar o Cadastro de Pessoa Física (CPF) como identificador único na checagem de dados. |
| **Requisito Associado** | RF025 |
| **Atores Envolvidos** | Admin, Sistema |
| **O que o usuário vê (Elementos de Interface)** | Processamento invisível ao usuário direto; ou Notificação de erro ('CPF Inválido/Duplicado') no formulário de origem. |
| **O que o usuário insere (Dados Fornecidos)** | Número de CPF digitado pelo Cidadão (11 dígitos). |
| **Condição de Entrada** | Um fluxo de cadastro ou inscrição solicita o CPF do Cidadão. |
| **Fluxo Principal (Passo a Passo)** | 1. O sistema recebe a entrada do CPF fornecido pelo ator.<br>2. O sistema executa o algoritmo de validação matemática do CPF.<br>3. O sistema consulta a base de dados interna da SEDH para verificar se já está vinculado.<br>4. O sistema retorna o status de CPF válido e liberado para a operação. |
| **Fluxos Alternativos / Desvios** | Nenhum fluxo alternativo obrigatório para este caso. |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - CPF Inválido: Falha na matemática.<br>FE02 - CPF Duplicado: Cidadão já cadastrado. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
