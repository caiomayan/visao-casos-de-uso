# Especificação de Caso de Uso: Personalizar relatorio

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC17 - Personalizar relatorio |
| **Objetivo** | Permitir que o usuário personalize relatórios escolhendo formato completo ou resumido, orientação da página, programas e subseções a serem incluídas. |
| **Requisitos Relacionados** | RF011 |
| **Atores** | Servidor |
| **Condição de Entrada** | O ator iniciou a geração de um relatório e optou por customizá-do. |
| **Fluxo Principal** | 1. O sistema abre a interface de Configurações de Relatório.<br>2. O Servidor seleciona 'Modelo Resumido' ou 'Modelo Completo'.<br>3. O Servidor seleciona as subseções que deseja (ex: Desmarcar 'Tabela Detalhada', manter 'Gráficos').<br>4. O Servidor clica em 'Aplicar e Gerar'.<br>5. O sistema devolve o fluxo de volta ao gerador central aplicando os filtros (UC16). |
| **Fluxos Alternativos** | Não existem fluxos alternativos definidos para este caso de uso. |
| **Fluxos de Exceção** | FE01 - Nenhuma Seção Selecionada: No passo 4, se o usuário desmarcar todas as sessões, o sistema avisa 'Por favor, selecione ao menos uma subseção para o relatório'. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
