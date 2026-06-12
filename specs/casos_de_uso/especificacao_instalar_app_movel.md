# Especificação de Caso de Uso: Instalar app movel

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC24 - Instalar app movel |
| **Objetivo do Sistema** | Instalação da plataforma web (PWA) de forma encapsulada como aplicativo mobile no dispositivo final. |
| **Requisito Associado** | RF023 |
| **Atores Envolvidos** | Cidadão, Servidor |
| **O que o usuário vê (Elementos de Interface)** | Uma barra sutil no rodapé do navegador sugerindo: 'Adicionar Paraíba Social à sua Tela Inicial'. Se aceitar, vê ícone final do programa aparecendo junto com outros Apps no celular. |
| **O que o usuário insere (Dados Fornecidos)** | Toque no botão 'Instalar / Aceitar' da caixa de diálogo nativa do Sistema Operacional (Android / iOS). |
| **Condição de Entrada** | O usuário entra com Chrome ou Safari num smartphone compatível e o Service Worker do sistema é carregado ativamente no background. |
| **Fluxo Principal (Passo a Passo)** | 1. O navegador processa o arquivo `manifest.json` do sistema e exibe o Banner Automático nativo convidando a instalação.<br>2. O usuário toca na opção nativa de 'Adicionar App'.<br>3. O Sistema Operacional cria um atalho contendo ícone oficial em alta resolução.<br>4. O usuário fecha o navegador Safari/Chrome e lança o atalho novo.<br>5. A aplicação agora roda como App Autônomo e abre em tela limpa sem barras de endereços. |
| **Fluxos Alternativos / Desvios** | FA01 - Prompt Manual: Se a dica não abrir sozinha, o usuário utiliza as próprias opções do menu lateral do navegador (botão de 3 pontinhos) e aperta a opção embutida. |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Limite de Espaço Storage: Erro nativo do dispositivo interrompe a criação do atalho do PWA por limite de MB da memória flash do smartphone. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
