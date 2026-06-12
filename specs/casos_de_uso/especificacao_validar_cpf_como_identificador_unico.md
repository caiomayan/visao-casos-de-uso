# Especificação de Caso de Uso: Validar CPF como identificador unico

**ID:** UC3  
**Requisito Relacionado:** RF025  
**Atores Principais:** Admin, Sistema  

## Resumo
Utilizar o Cadastro de Pessoa Física (CPF) como identificador único, realizando a checagem de dados para garantir que um cidadão não receba o mesmo benefício social duas vezes por caminhos diferentes.

## História de Usuário
**Eu como** Admin, 
**quero** validar cpf como identificador unico, 
**para que** seja possível utilizar o Cadastro de Pessoa Física (CPF) como identificador único, realizando a checagem de dados para garantir que um cidadão não receba o mesmo benefício social duas vezes por caminhos diferentes.

## Critérios de Aceitação
- **Cenário 1: Sucesso na operação.** Dado que o usuário possui os acessos necessários, quando a ação for iniciada, então o sistema deve cumprir o objetivo esperado.
- **Cenário 2: Falha ou acesso negado.** Dado que ocorreu um erro ou o usuário não tem permissão, quando a ação for tentada, então o sistema deve abortar e exibir uma mensagem correspondente.

*(Diagrama de atividades omitido para esta especificação textual)*
