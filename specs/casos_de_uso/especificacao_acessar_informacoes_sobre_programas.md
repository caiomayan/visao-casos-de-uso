# Especificação de Caso de Uso: Acessar informacoes sobre programas

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC19 - Acessar informacoes sobre programas |
| **Objetivo** | Permitir que cidadãos acessem informações sobre programas sociais, ações desenvolvidas e formas de participação. |
| **Requisitos Relacionados** | RF020 |
| **Atores** | Cidadão |
| **Condição de Entrada** | O Cidadão acessa o portal web ou app móvel. |
| **Fluxo Principal** | 1. O sistema verifica se o cidadão está logado. Se sim, (<<include>> [UC1 - Realizar login](especificacao_realizar_login.md)). Caso contrário, mostra a visão pública.<br>2. O cidadão navega pela lista de programas abertos (Cartões e Banners).<br>3. O cidadão clica em 'Saber Mais' em um programa específico.<br>4. O sistema carrega a página detalhada, exibindo Regras, Prazos de Edital e Documentos Exigidos.<br>5. O cidadão pode se sentir motivado e optar por se inscrever [FA01].<br>6. O cidadão pode querer acessar informações institucionais sobre os eixos [FA02].<br>7. O cidadão pode ter dúvidas e solicitar suporte [FA03]. |
| **Fluxos Alternativos** | FA01 - Ir para Inscrição: No passo 5, ele clica no botão 'Inscreva-se', e vai para o (<<include>>/Associação ao [UC20 - Inscrever-se em programa social](especificacao_inscrever_se_em_programa_social.md)).<br>FA02 - Entender Eixos: No passo 6, ele acessa o menu principal e dispara (<<extend>> [UC15 - Apresentar eixos da SEDH](especificacao_apresentar_eixos_da_sedh.md)).<br>FA03 - Dúvidas: No passo 7, ele aciona a Central de Ajuda disparando (<<extend>> [UC21 - Solicitar suporte/melhoria](especificacao_solicitar_suporte_melhoria.md)). |
| **Fluxos de Exceção** | FE01 - Programa Pausado: No passo 4, se o edital estiver encerrado, exibe uma tarja vermelha 'Inscrições Encerradas'. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
