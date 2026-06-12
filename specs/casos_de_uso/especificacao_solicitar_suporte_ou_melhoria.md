# Especificação de Caso de Uso: Solicitar suporte ou melhoria

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC21 - Solicitar suporte ou melhoria |
| **Objetivo do Sistema** | Acesso a Ouvidoria e canais de ajuda técnicos para resolução de dúvidas e melhorias. |
| **Requisito Associado** | RF019 |
| **Atores Envolvidos** | Cidadão |
| **O que o usuário vê (Elementos de Interface)** | Formulário de Abertura de Chamado contendo: Dropdown de Categoria, Caixa de Título (Assunto) e Caixa de Texto Longo (Textarea). |
| **O que o usuário insere (Dados Fornecidos)** | Seleção da Categoria ('Dúvida de Acesso', 'Erro de Tela'), Escrita do texto explicativo da falha encontrada, Upload de Screenshot opcional. |
| **Condição de Entrada** | O usuário encontra problemas ou dúvidas de navegação. |
| **Fluxo Principal (Passo a Passo)** | 1. O ator clica no botão 'Ajuda e Suporte' flutuante na tela.<br>2. O sistema mostra o formulário de ticket da Ouvidoria/Suporte.<br>3. O ator preenche o Assunto e fornece o máximo de detalhes textuais do bug.<br>4. O ator anexa uma imagem da tela (print).<br>5. O ator submete e o sistema confirma com a geração do número do ticket de suporte rastreável. |
| **Fluxos Alternativos / Desvios** | FA01 - Exibir Autoajuda FAQ: Ao digitar palavras como 'senha' no título, o sistema detecta a palavra e recomenda: 'Veja como redefinir sua senha aqui', interceptando o ticket para o usuário nem precisar enviar. |
| **Fluxos de Exceção (Erros e Limites)** | Nenhuma validação de exceção. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
