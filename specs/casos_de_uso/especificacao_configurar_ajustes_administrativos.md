# Especificação de Caso de Uso: Configurar ajustes administrativos

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC23 - Configurar ajustes administrativos |
| **Objetivo do Sistema** | Gerir parâmetros estáticos, chaves (flags) e strings da interface a partir do banco de dados. |
| **Requisito Associado** | RF018 |
| **Atores Envolvidos** | Administrador |
| **O que o usuário vê (Elementos de Interface)** | Painel de controle com abas de separação (ex: 'Variáveis de Integração', 'Textos Home'), preenchidos com Chaves de Interruptor (Toggles On/Off) e campos numéricos. |
| **O que o usuário insere (Dados Fornecidos)** | Ligar/desligar botões toggle de funcionalidades beta, alterar valor numérico ('Total de inscrições por vez'), digitação de textos institucionais das áreas. |
| **Condição de Entrada** | O administrador acessa o submódulo 'Configuração Geral'. |
| **Fluxo Principal (Passo a Passo)** | 1. O sistema recupera e exibe a cópia atual das configurações do banco.<br>2. O Admin navega para a aba de Configuração de Limites do Ano.<br>3. O Admin altera a variável de limite de data final de todos os editais vigentes e aciona 'Salvar Alterações Globais'.<br>4. O sistema atualiza o banco primário.<br>5. O sistema envia sinal de purga de cache a todas as instâncias hospedadas do site, renovando a interface de todos instantaneamente. |
| **Fluxos Alternativos / Desvios** | Nenhum fluxo alternativo obrigatório para este caso. |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Parâmetro Crítico Vazio: Se o Admin apagar toda uma variável obrigatória, o sistema bloqueia o save dizendo 'Valor Não Pode Ser Nulo'. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
