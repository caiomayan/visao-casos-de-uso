# Especificação de Caso de Uso: Consolidar dados

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC8 - Consolidar dados |
| **Objetivo** | Reunir dados de diferentes programas, setores e bases da SEDH em uma plataforma única e organizada. |
| **Requisitos Relacionados** | RF007 |
| **Atores** | Servidor |
| **Condição de Entrada** | O Servidor necessita cruzar informações de secretarias ou programas distintos. |
| **Fluxo Principal** | 1. O Servidor seleciona a opção 'Cruzamento de Programas'.<br>2. O sistema lista todos os programas com bases de dados ativas (ex: Tá na Mesa, Prato Cheio).<br>3. O Servidor seleciona 2 ou mais programas e define a chave de união (ex: por Município).<br>4. O sistema roda uma query de união consolidando os números (ex: Soma total de beneficiários desduplicados).<br>5. O sistema exibe uma tabela mestre contendo a visão macro consolidada. |
| **Fluxos Alternativos** | Não existem fluxos alternativos definidos para este caso de uso. |
| **Fluxos de Exceção** | FE01 - Bases Incompatíveis: No passo 4, se os dados estruturais dos programas não puderem ser mesclados, o sistema acusa erro de incompatibilidade de layout. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
