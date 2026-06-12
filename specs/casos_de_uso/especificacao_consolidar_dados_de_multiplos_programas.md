# Especificação de Caso de Uso: Consolidar dados de multiplos programas

Esta especificação segue o formato tabular estruturado.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC8 - Consolidar dados de multiplos programas |
| **Objetivo** | Reunir dados de diferentes programas, setores e bases da SEDH em uma plataforma única e organizada. |
| **Requisitos Relacionados** | RF007 |
| **Atores** | Servidor |
| **Condição de Entrada** | O usuário (Servidor) acessa a interface correspondente à funcionalidade. |
| **Fluxo Principal** | 1. O ator inicia a funcionalidade.<br>2. O sistema apresenta a interface e solicita os dados necessários.<br>3. O ator insere as informações.<br>4. O sistema valida e processa a ação.<br>5. O sistema retorna uma mensagem de sucesso. |
| **Fluxos Alternativos** | A1. Cancelamento: O ator pode cancelar a ação a qualquer momento antes do processamento, retornando à tela inicial. |
| **Fluxos de Exceção** | E1. Falha de validação ou permissão: O sistema exibe uma mensagem de erro e aborta a operação. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo é alcançado com sucesso. |
