# Especificação de Caso de Uso: Acessar informacoes sobre programas

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | UC19 - Acessar informacoes sobre programas |
| **Objetivo do Sistema** | Consultar na área pública as informações de todos os projetos governamentais. |
| **Requisito Associado** | RF020 |
| **Atores Envolvidos** | Cidadão |
| **O que o usuário vê (Elementos de Interface)** | Lista de Cartões informativos (Cards) organizados em grades. Cada um mostra: Título do Edital, Status, Ícone do Eixo de Atuação. |
| **O que o usuário insere (Dados Fornecidos)** | Termos de pesquisa na barra de busca (Buscar por Programa) e cliques nos próprios cartões informativos. |
| **Condição de Entrada** | O Cidadão navega ao portal aberto. |
| **Fluxo Principal (Passo a Passo)** | 1. O sistema verifica a autenticação transparente (<<include>> [UC1 - Realizar login](especificacao_realizar_login.md)), mas permite acesso público.<br>2. O sistema exibe o grid de editais e programas.<br>3. O Cidadão clica em um programa de transferência de renda.<br>4. O sistema carrega a descrição oficial detalhada de contrapartidas, regras de participação e valores do auxílio.<br>5. O cidadão pode querer entender melhor as diretrizes do governo antes [FA01].<br>6. O cidadão percebe que não tem direito e quer questionar o edital [FA02].<br>7. O cidadão entende os requisitos e deseja se cadastrar diretamente pela página [FA03]. |
| **Fluxos Alternativos / Desvios** | FA01 - Áreas da SEDH: (<<extend>> [UC15 - Apresentar eixos da SEDH](especificacao_apresentar_eixos_da_sedh.md)).<br>FA02 - Sugestões/Reclamações: (<<extend>> [UC21 - Solicitar suporte ou melhoria](especificacao_solicitar_suporte_ou_melhoria.md)).<br>FA03 - Fazer Cadastro: Botão central que leva a (<<include>> implicitamente no fluxo [UC20 - Inscrever-se em programa social](especificacao_inscrever_se_em_programa_social.md)). |
| **Fluxos de Exceção (Erros e Limites)** | FE01 - Página Não Encontrada: Programa retirado do ar exibe erro 404 e recomenda acesso à home. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
