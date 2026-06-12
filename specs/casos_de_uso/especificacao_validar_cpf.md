# Especificação de Caso de Uso: Validar CPF

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC3 - Validar CPF |
| **Objetivo** | Utilizar o Cadastro de Pessoa Física (CPF) como identificador único, realizando a checagem de dados para garantir que um cidadão não receba o mesmo benefício social duas vezes por caminhos diferentes. |
| **Requisitos Relacionados** | RF025 |
| **Atores** | Admin, Sistema |
| **Condição de Entrada** | Um fluxo de cadastro ou inscrição solicita o CPF do Cidadão. |
| **Fluxo Principal** | 1. O sistema recebe a entrada do CPF fornecido pelo ator.<br>2. O sistema executa o algoritmo de validação matemática do CPF (Dígitos verificadores).<br>3. O sistema consulta a base de dados interna da SEDH para verificar se o CPF já está vinculado a outro benefício restritivo.<br>4. O sistema retorna o status de CPF válido e liberado para a operação. |
| **Fluxos Alternativos** | Não existem fluxos alternativos definidos para este caso de uso. |
| **Fluxos de Exceção** | FE01 - CPF Inválido: No passo 2, se a máscara ou a matemática falhar, o sistema exibe 'CPF digitado é inválido'.<br>FE02 - CPF Duplicado/Bloqueado: No passo 3, se o CPF já possuir o benefício, o sistema exibe 'Cidadão já cadastrado neste programa' e encerra o fluxo. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
