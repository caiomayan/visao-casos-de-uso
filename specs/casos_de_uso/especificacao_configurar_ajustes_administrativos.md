# Especificação de Caso de Uso: Configurar ajustes administrativos

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | UC23 - Configurar ajustes administrativos |
| **Objetivo** | Possuir páginas ou módulos de configuração para ajustes administrativos da plataforma. |
| **Requisitos Relacionados** | RF018 |
| **Atores** | Administrador |
| **Condição de Entrada** | O Administrador acessa o módulo 'Configurações de Sistema'. |
| **Fluxo Principal** | 1. O Administrador seleciona a seção que deseja alterar (Textos Institucionais, Parâmetros de API, Período Letivo/Ano Base).<br>2. O sistema exibe o formulário com os parâmetros gerais carregados em memória.<br>3. O Administrador ajusta as chaves de configuração e salva.<br>4. O sistema escreve as mudanças no banco de dados e limpa o cache global da aplicação para as novas configurações entrarem em vigor. |
| **Fluxos Alternativos** | Não existem fluxos alternativos definidos para este caso de uso. |
| **Fluxos de Exceção** | FE01 - Erro de Cache: No passo 4, se o servidor não puder limpar a memória, exibe 'Configuração salva, mas as alterações podem demorar 5 minutos para refletirem no site'. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
