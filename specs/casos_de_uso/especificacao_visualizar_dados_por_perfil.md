# Especificação de Caso de Uso: Visualizar dados por perfil

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC12 - Visualizar dados por perfil |
| **Objetivo do Sistema** | Visualização dos dados demográficos dos atendidos pelo programa. |
| **Requisito Associado** | RF014 |
| **Atores Envolvidos** | Servidor |
| **O que o usuário vê (Elementos de Interface)** | Painel de Gráficos de Pizza ou de Barras Horizontais com recortes de Idade (0-18, 18-35...), Gênero, Renda e Nível Escolar. |
| **O que o usuário insere (Dados Fornecidos)** | Botão de 'Exportar Relatório CSV' ou Passar o Mouse (Hover) sobre os recortes para ver o valor exato. |
| **Condição de Entrada** | O ator ativa a aba Demográfica. |
| **Fluxo Principal (Passo a Passo)** | 1. O sistema consulta as tabelas demográficas daquele programa.<br>2. O sistema separa e calcula percentuais por Faixa Etária, Gênero, Renda e Escolaridade.<br>3. O sistema renderiza os gráficos específicos na tela.<br>4. O Servidor visualiza os painéis para verificar a distribuição e o público primário afetado. |
| **Fluxos Alternativos / Desvios** | FA01 - Exportar Dados Abertos: O ator clica em 'Baixar Microdados' para gerar a tabela .csv anônima. |
| **Fluxos de Exceção (Erros e Limites)** | Nenhuma validação de exceção. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
