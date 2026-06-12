# Especificação de Caso de Uso: Emitir relatorio em PDF

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC18 - Emitir relatorio em PDF |
| **Objetivo do Sistema** | Consolidar os dados em arquivo portável e emitir PDF para download rápido. |
| **Requisito Associado** | RF012 |
| **Atores Envolvidos** | Servidor |
| **O que o usuário vê (Elementos de Interface)** | Indicador de Carregamento ('Gerando PDF...') seguido pelas janelas nativas do navegador para indicar onde salvar o arquivo físico no computador. |
| **O que o usuário insere (Dados Fornecidos)** | Definição opcional do nome do arquivo (ex: Relatorio_Jan2026.pdf) na janela de sistema operacional local. |
| **Condição de Entrada** | O relatório na tela encontra-se finalizado e o usuário solicitou o download. |
| **Fluxo Principal (Passo a Passo)** | 1. O ator clica no botão com ícone de PDF.<br>2. O sistema despacha a visualização HTML atual para um conversor backend seguro.<br>3. O backend carimba data, assinatura digital ou hash criptográfico garantindo que é um doc original.<br>4. O backend converte as fontes e vetores para o arquivo binário .pdf real.<br>5. O sistema envia a resposta ao Browser, forçando a janela de download automático no navegador do ator. |
| **Fluxos Alternativos / Desvios** | FA01 - Adição de Rascunho: O servidor estampa a palavra 'Preliminar' como marca d'água invisível de PDF, caso o período consultado ainda não tenha acabado. |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Erro de Biblioteca de Conversão: Exibe 'Falha de Servidor ao Gerar PDF. Tente novamente mais tarde'. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
