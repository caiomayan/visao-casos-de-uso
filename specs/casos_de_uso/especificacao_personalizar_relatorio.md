# Especificação de Caso de Uso: Personalizar relatorio

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC17 - Personalizar relatorio |
| **Objetivo do Sistema** | Permitir personalizar a estrutura dos relatórios formatados. |
| **Requisito Associado** | RF011 |
| **Atores Envolvidos** | Servidor |
| **O que o usuário vê (Elementos de Interface)** | Menu lateral retrátil (Drawer) com Caixas de Seleção (Checkboxes) listando os blocos que compõem o documento: 'Incluir Resumo de Texto', 'Incluir Análise Demográfica', 'Incluir Lista de Nomes'. |
| **O que o usuário insere (Dados Fornecidos)** | Checagem (Marcação) visual das caixas listando o que o usuário deseja na impressão. Botão de 'Aplicar Seleção'. |
| **Condição de Entrada** | O ator clicou em 'Configurações do Relatório' durante o processo de visualização. |
| **Fluxo Principal (Passo a Passo)** | 1. O sistema mostra um menu deslizante ao lado direito.<br>2. O ator desmarca a opção 'Incluir Detalhamento de Tabelas Brutas' para deixar o relatório mais limpo.<br>3. O ator escolhe a orientação de layout 'Retrato' ou 'Paisagem'.<br>4. O ator clica em 'Aplicar Modificações'.<br>5. O sistema recarrega a janela do UC base ocultando as seções apagadas pelo usuário. |
| **Fluxos Alternativos / Desvios** | Nenhum fluxo alternativo obrigatório para este caso. |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Seleção Vazia: O sistema bloqueia a aplicação se o ator desmarcar todas as caixas, exibindo 'Você deve selecionar no mínimo uma sessão'. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
