# Especificação de Caso de Uso: Instalar app movel

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC24 - Instalar app movel |
| **Objetivo** | Permitir instalação em dispositivos móveis, abrindo como aplicativo a partir do navegador. |
| **Requisitos Relacionados** | RF023 |
| **Atores** | Cidadão, Servidor |
| **Condição de Entrada** | O usuário acessa o sistema de um celular Chrome/Safari que suporta Progressive Web Apps (PWA). |
| **Fluxo Principal** | 1. O sistema carrega a manifest.json e registra o service worker (PWA) em background.<br>2. O navegador identifica que a aplicação pode ser instalada e exibe um prompt (Banner na tela inferior: 'Adicionar Paraíba Social à Tela Inicial').<br>3. O usuário aceita a instalação clicando em 'Adicionar'.<br>4. O sistema operacional gera o atalho na gaveta de apps com o logotipo do programa.<br>5. O usuário abre o app fora do navegador (em modo standalone/fullscreen). |
| **Fluxos Alternativos** | FA01 - Instalação Manual: No passo 2, se o prompt automático não aparecer, o usuário clica nas opções do navegador -> 'Instalar Aplicativo'. |
| **Fluxos de Exceção** | FE01 - Armazenamento Cheio: No passo 3, o OS do celular cancela a instalação e avisa falta de espaço. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
