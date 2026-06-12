import os
import re

base_dir = r"C:\Users\Caio\Documents\Dev\visao-casos-de-uso\specs\casos_de_uso"
os.makedirs(base_dir, exist_ok=True)

def slugify(text):
    text = text.lower()
    text = re.sub(r'[ãáâà]', 'a', text)
    text = re.sub(r'[éê]', 'e', text)
    text = re.sub(r'[í]', 'i', text)
    text = re.sub(r'[óôõ]', 'o', text)
    text = re.sub(r'[ú]', 'u', text)
    text = re.sub(r'[ç]', 'c', text)
    text = re.sub(r'[^a-z0-9]+', '_', text)
    return text.strip('_')

def md_link(uc_id, uc_name):
    filename = f"especificacao_{slugify(uc_name)}.md"
    return f"[{uc_id} - {uc_name}]({filename})"

# Comprehensive dictionary with unique, highly detailed steps for each use case.
use_cases_data = [
    {
        "id": "UC1", "code": "RF001", "name": "Realizar login", "actors": ["Cidadão", "Servidor", "Admin"],
        "desc": "Permitir que usuários realizem login para acessar as áreas internas da plataforma, especialmente dashboards, relatórios, gestão e módulos administrativos.",
        "pre": "O ator não está autenticado no sistema.",
        "main_flow": [
            "1. O ator acessa a página inicial do sistema e clica em 'Entrar'.",
            "2. O sistema redireciona para a tela de autenticação do Clerk.",
            "3. O ator informa suas credenciais (E-mail e Senha) ou escolhe o login via provedor externo.",
            "4. O Clerk valida as credenciais.",
            "5. O sistema recebe o token de autenticação, registra a sessão e redireciona o ator para o painel apropriado."
        ],
        "alt_flows": [
            "FA01 - Esqueci a Senha: No passo 3, o ator clica em 'Esqueci minha senha', e o sistema envia um e-mail de recuperação."
        ],
        "exc_flows": [
            "FE01 - Credenciais Inválidas: No passo 4, se a senha for incorreta, o sistema exibe 'Usuário ou senha inválidos' e permite tentar novamente."
        ]
    },
    {
        "id": "UC2", "code": "RF002", "name": "Controlar acesso", "actors": ["Admin", "Sistema"],
        "desc": "Controlar o acesso dos usuários conforme sessões, perfis e permissões, impedindo que usuários não autorizados acessem funcionalidades restritas.",
        "pre": "O ator tenta acessar uma rota ou módulo protegido do sistema.",
        "main_flow": [
            "1. O ator solicita o acesso a um módulo restrito (ex: Painel de Indicadores).",
            "2. O sistema intercepta a requisição e verifica o token de sessão ativo.",
            "3. O sistema consulta as permissões vinculadas ao perfil do ator.",
            "4. O sistema confirma que o perfil possui acesso àquele recurso.",
            "5. O sistema carrega e exibe o módulo solicitado."
        ],
        "alt_flows": [
            "FA01 - Perfil com Restrição Parcial: No passo 4, se o ator tiver permissão apenas de leitura, o sistema oculta botões de edição/exclusão na tela carregada."
        ],
        "exc_flows": [
            "FE01 - Acesso Negado: No passo 4, se o ator não tiver permissão, o sistema exibe a página de 'Acesso Negado (Erro 403)' e bloqueia o recurso."
        ]
    },
    {
        "id": "UC3", "code": "RF025", "name": "Validar CPF", "actors": ["Admin", "Sistema"],
        "desc": "Utilizar o Cadastro de Pessoa Física (CPF) como identificador único, realizando a checagem de dados para garantir que um cidadão não receba o mesmo benefício social duas vezes por caminhos diferentes.",
        "pre": "Um fluxo de cadastro ou inscrição solicita o CPF do Cidadão.",
        "main_flow": [
            "1. O sistema recebe a entrada do CPF fornecido pelo ator.",
            "2. O sistema executa o algoritmo de validação matemática do CPF (Dígitos verificadores).",
            "3. O sistema consulta a base de dados interna da SEDH para verificar se o CPF já está vinculado a outro benefício restritivo.",
            "4. O sistema retorna o status de CPF válido e liberado para a operação."
        ],
        "alt_flows": [],
        "exc_flows": [
            "FE01 - CPF Inválido: No passo 2, se a máscara ou a matemática falhar, o sistema exibe 'CPF digitado é inválido'.",
            "FE02 - CPF Duplicado/Bloqueado: No passo 3, se o CPF já possuir o benefício, o sistema exibe 'Cidadão já cadastrado neste programa' e encerra o fluxo."
        ]
    },
    {
        "id": "UC4", "code": "RF003", "name": "Visualizar painel", "actors": ["Servidor"],
        "desc": "Apresentar um painel principal com indicadores demográficos, sociais e econômicos consolidados, permitindo uma visão estratégica dos dados da SEDH.",
        "pre": "O Servidor acessa o endereço principal do Dashboard.",
        "main_flow": [
            f"1. O Servidor efetua o login (<<include>> {md_link('UC1', 'Realizar login')}).",
            f"2. O sistema valida as permissões (<<include>> {md_link('UC2', 'Controlar acesso')}).",
            f"3. O sistema requisita a atualização de dados externos (<<include>> {md_link('UC25', 'Sincronizar com Sheets')}).",
            "4. O sistema renderiza a tela principal com os cartões de indicadores (KPIs globais).",
            "5. O Servidor visualiza os resumos socioeconômicos.",
            "6. O Servidor opta por visualizar os gráficos detalhados [FA01].",
            "7. O Servidor opta por filtrar os dados [FA02].",
            "8. O Servidor opta por consolidar programas específicos [FA03]."
        ],
        "alt_flows": [
            f"FA01 - Visualizar Gráficos: No passo 6, o ator aciona a funcionalidade de gráficos, engatilhando o (<<include>> {md_link('UC6', 'Visualizar gráficos')}).",
            f"FA02 - Aplicar Filtros: No passo 7, o ator expande a barra lateral e aplica recortes territoriais (<<include>> {md_link('UC5', 'Filtrar dados')}).",
            f"FA03 - Consolidar Múltiplos Programas: No passo 8, o ator seleciona mais de um programa para cruzar dados (<<include>> {md_link('UC8', 'Consolidar dados')})."
        ],
        "exc_flows": [
            "FE01 - Falha no Carregamento: No passo 4, se o banco de dados falhar, o sistema apresenta um aviso de 'Dados indisponíveis no momento' com botão de retentativa."
        ]
    },
    {
        "id": "UC5", "code": "RF004", "name": "Filtrar dados", "actors": ["Servidor"],
        "desc": "Permitir filtrar os dados por município e por regional, possibilitando análises territorializadas dos indicadores sociais.",
        "pre": "O Servidor está no painel de indicadores ou em relatórios com dados consolidados.",
        "main_flow": [
            "1. O Servidor clica no botão 'Filtros Avançados'.",
            "2. O sistema abre um modal contendo as opções 'Município' e 'Regional de Ensino/Saúde/Social'.",
            "3. O Servidor seleciona uma ou mais opções nos campos de seleção dropdown.",
            "4. O Servidor clica em 'Aplicar'.",
            "5. O sistema recalcula as agregações de dados com base na nova localidade territorial.",
            "6. O sistema atualiza a tela do painel exibindo apenas os resultados filtrados."
        ],
        "alt_flows": [
            "FA01 - Limpar Filtros: No passo 4, o ator pode clicar em 'Limpar Filtros', fazendo com que o sistema recarregue os dados globais do Estado da Paraíba."
        ],
        "exc_flows": [
            "FE01 - Região sem Dados: No passo 5, se o município não tiver inscritos/dados, o sistema exibe os gráficos e tabelas zerados com a mensagem 'Nenhum dado encontrado para a região'."
        ]
    },
    {
        "id": "UC6", "code": "RF005", "name": "Visualizar graficos", "actors": ["Servidor"],
        "desc": "Exibir gráficos para facilitar a interpretação dos dados, incluindo comparações, tendências e variações ao longo do tempo.",
        "pre": "O Servidor solicitou a visualização gráfica no Painel.",
        "main_flow": [
            "1. O sistema compila o conjunto atual de dados em arrays apropriados para plotagem.",
            "2. O sistema carrega a biblioteca de renderização gráfica (ex: Chart.js ou similar).",
            "3. O sistema exibe um gráfico de barras comparativo (Município x Município).",
            "4. O sistema exibe um gráfico de linhas temporais mostrando o crescimento dos programas nos últimos 12 meses.",
            "5. O Servidor pode passar o mouse (hover) sobre os nós do gráfico para ler os valores exatos."
        ],
        "alt_flows": [
            "FA01 - Alternar Tipo de Gráfico: No passo 3, o ator clica no ícone de engrenagem e troca o gráfico de 'Barras' para 'Pizza' ou 'Dispersão'."
        ],
        "exc_flows": [
            "FE01 - Erro de Renderização: No passo 2, se a biblioteca falhar, o sistema provê um fallback exibindo uma tabela simples em vez do gráfico."
        ]
    },
    {
        "id": "UC7", "code": "RF006", "name": "Identificar padroes", "actors": ["Servidor"],
        "desc": "Permitir identificar padrões, tendências e mudanças nos indicadores sociais, como evolução populacional e variações territoriais.",
        "pre": "O Servidor está acessando o módulo Analítico Avançado.",
        "main_flow": [
            "1. O Servidor acessa a aba 'Análise de Padrões'.",
            "2. O sistema processa uma regressão linear sobre os dados históricos da base.",
            "3. O sistema apresenta caixas de texto com 'Insights Automatizados' (ex: 'O programa X teve um aumento de 20% no Cariri nos últimos 3 meses').",
            "4. O Servidor sinaliza o insight como útil ou não útil."
        ],
        "alt_flows": [
            "FA01 - Exportar Insight: No passo 3, o Servidor pode clicar em 'Exportar Destaque' para baixar uma imagem png contendo a tendência identificada para uso em apresentações."
        ],
        "exc_flows": [
            "FE01 - Dados Insuficientes: No passo 2, se houver menos de 3 meses de histórico, o sistema exibe 'Dados insuficientes para calcular tendências precisas'."
        ]
    },
    {
        "id": "UC8", "code": "RF007", "name": "Consolidar dados", "actors": ["Servidor"],
        "desc": "Reunir dados de diferentes programas, setores e bases da SEDH em uma plataforma única e organizada.",
        "pre": "O Servidor necessita cruzar informações de secretarias ou programas distintos.",
        "main_flow": [
            "1. O Servidor seleciona a opção 'Cruzamento de Programas'.",
            "2. O sistema lista todos os programas com bases de dados ativas (ex: Tá na Mesa, Prato Cheio).",
            "3. O Servidor seleciona 2 ou mais programas e define a chave de união (ex: por Município).",
            "4. O sistema roda uma query de união consolidando os números (ex: Soma total de beneficiários desduplicados).",
            "5. O sistema exibe uma tabela mestre contendo a visão macro consolidada."
        ],
        "alt_flows": [],
        "exc_flows": [
            "FE01 - Bases Incompatíveis: No passo 4, se os dados estruturais dos programas não puderem ser mesclados, o sistema acusa erro de incompatibilidade de layout."
        ]
    },
    {
        "id": "UC9", "code": "RF008", "name": "Acompanhar execucao", "actors": ["Servidor"],
        "desc": "Permitir o acompanhamento dos programas sociais executados pela SEDH, incluindo informações sobre beneficiários, execução das políticas e dados territoriais.",
        "pre": "O Servidor acessa a listagem de Programas em Andamento.",
        "main_flow": [
            "1. O Servidor abre a aba 'Monitoramento de Execução'.",
            "2. O sistema exibe a lista de todos os programas ativos sob responsabilidade da SEDH, com status geral (Dentro da meta / Atrasado).",
            "3. O Servidor clica em um programa específico da lista.",
            f"4. O sistema direciona para a página detalhada do programa (<<include>> {md_link('UC10', 'Visualizar página do programa')}).",
            "5. O Servidor verifica a taxa de conversão (Inscritos vs Beneficiados) e o orçamento executado.",
            "6. O Servidor pode solicitar geração de um relatório de execução [FA01]."
        ],
        "alt_flows": [
            f"FA01 - Gerar Relatório do Programa: No passo 6, o ator aciona o atalho, o que desencadeia (<<include>> {md_link('UC16', 'Gerar relatório automático')})."
        ],
        "exc_flows": []
    },
    {
        "id": "UC10", "code": "RF009", "name": "Visualizar pagina do programa", "actors": ["Servidor"],
        "desc": "Disponibilizar páginas individuais para cada programa social, contendo dados quantitativos, informações descritivas, gráficos, rankings e análises próprias.",
        "pre": "O ator clica em um cartão ou link de um Programa Específico.",
        "main_flow": [
            "1. O sistema carrega os metadados do programa (Nome, Data de Criação, Eixo de Atuação).",
            "2. O sistema renderiza a tela com as informações descritivas e os KPIs isolados desse programa.",
            "3. O Servidor analisa a página.",
            "4. O Servidor pode desejar ver os dados projetados num mapa [FA01].",
            "5. O Servidor pode desejar cruzar com perfis demográficos [FA02].",
            "6. O Servidor pode consultar o ranking de cidades que mais utilizam [FA03]."
        ],
        "alt_flows": [
            f"FA01 - Ver Mapa: No passo 4, o ator clica na aba 'Geolocalização', ativando a extensão (<<extend>> {md_link('UC11', 'Visualizar mapa')}).",
            f"FA02 - Ver Perfis: No passo 5, o ator clica na aba 'Demografia', ativando a extensão (<<extend>> {md_link('UC12', 'Visualizar dados por perfil')}).",
            f"FA03 - Ver Rankings: No passo 6, o ator clica na aba 'Leaderboard', ativando a extensão (<<extend>> {md_link('UC13', 'Visualizar rankings')})."
        ],
        "exc_flows": [
            "FE01 - Programa Inexistente: No passo 1, se o ID do programa for inválido, o sistema redireciona para a lista geral com mensagem 'Programa não encontrado'."
        ]
    },
    {
        "id": "UC11", "code": "RF013", "name": "Visualizar mapa", "actors": ["Servidor"],
        "desc": "Disponibilizar mapas para visualizar a distribuição dos programas sociais no território paraibano.",
        "pre": "O ator ativa a visão de mapa de um Programa Específico.",
        "main_flow": [
            "1. O sistema inicia o módulo de mapa coroplético (Leaflet/Google Maps API) focado no Estado da Paraíba.",
            "2. O sistema busca as coordenadas geográficas dos municípios que possuem o programa ativo.",
            "3. O sistema pinta os polígonos dos municípios com base na densidade de inscritos (escalas de calor).",
            "4. O Servidor dá um zoom e clica em uma cidade específica.",
            "5. O sistema exibe um tooltip/pop-up com os números precisos daquela localidade."
        ],
        "alt_flows": [
            "FA01 - Alternar Camada de Satélite: No passo 1, o ator pode mudar a visualização padrão para Mapa de Satélite."
        ],
        "exc_flows": [
            "FE01 - Erro de Geolocalização: No passo 3, se faltarem dados geográficos (GeoJSON), o sistema exibe os municípios faltando como 'Desconhecidos' fora do mapa."
        ]
    },
    {
        "id": "UC12", "code": "RF014", "name": "Visualizar dados por perfil", "actors": ["Servidor"],
        "desc": "Permitir a visualização dos dados por município, região e perfil socioeconômico, apoiando decisões baseadas no território.",
        "pre": "O ator ativa a aba de Análise de Perfis.",
        "main_flow": [
            "1. O sistema consulta as tabelas de inscritos do programa.",
            "2. O sistema separa os agregados por Idade, Gênero, Faixa de Renda e Nível de Escolaridade.",
            "3. O sistema exibe gráficos demográficos específicos.",
            "4. O Servidor avalia qual faixa populacional está sendo mais impactada."
        ],
        "alt_flows": [
            "FA01 - Exportar CSV de Perfil: No passo 3, o ator pode clicar em 'Baixar Microdados' para obter a tabela CSV correspondente."
        ],
        "exc_flows": []
    },
    {
        "id": "UC13", "code": "RF015", "name": "Visualizar rankings", "actors": ["Servidor"],
        "desc": "Apresentar rankings e painéis comparativos para apoiar a leitura dos dados por programa, município ou regional.",
        "pre": "O ator ativa a aba de Rankings.",
        "main_flow": [
            "1. O sistema ordena os municípios de forma decrescente com base no volume de atendimentos.",
            "2. O sistema renderiza uma tabela no formato 'Top 10' e 'Bottom 10' de adesão.",
            "3. O sistema apresenta setas indicativas de subida/descida no ranking (Trend Up / Trend Down).",
            "4. O Servidor acompanha as regiões que precisam de mais investimento social baseando-se no ranking."
        ],
        "alt_flows": [
            "FA01 - Alterar Critério do Ranking: No passo 1, o ator pode pedir para ordenar por 'Maior Orçamento' em vez de 'Maior Atendimento'."
        ],
        "exc_flows": []
    },
    {
        "id": "UC14", "code": "RF016", "name": "Avaliar inscricoes", "actors": ["Assistente Social"],
        "desc": "Possuir funcionalidades relacionadas à avaliação de inscrições em programas ou iniciativas da SEDH.",
        "pre": "Existem cidadãos que solicitaram entrada em um programa social e o Assistente está logado.",
        "main_flow": [
            "1. A Assistente Social abre a fila de 'Solicitações Pendentes'.",
            "2. O sistema exibe a ficha completa preenchida pelo Cidadão, junto aos documentos anexados.",
            "3. A Assistente analisa a veracidade e pertinência dos dados segundo os critérios do programa.",
            "4. A Assistente clica em 'Aprovar' ou 'Rejeitar'.",
            "5. O sistema solicita uma justificativa se for rejeição [FA01].",
            "6. O sistema altera o status da inscrição e notifica o cidadão."
        ],
        "alt_flows": [
            "FA01 - Justificar Rejeição: No passo 5, um campo de texto obrigatório é exibido para embasamento legal da recusa.",
            "FA02 - Solicitar Mais Documentos: No passo 4, em vez de Aprovar/Rejeitar, a Assistente escolhe 'Pendente - Documento', devolvendo o status para o cidadão sem recusar."
        ],
        "exc_flows": [
            "FE01 - Anexos Corrompidos: No passo 2, se os arquivos (PDF/Imagens) enviados não abrirem, a Assistente aciona o fluxo FA02."
        ]
    },
    {
        "id": "UC15", "code": "RF022", "name": "Apresentar eixos da SEDH", "actors": ["Cidadão"],
        "desc": "Apresentar os principais eixos de atuação da SEDH, como Segurança Alimentar, Assistência Social, Direitos Humanos, Trabalho e Renda e Economia Solidária.",
        "pre": "O cidadão navega pelo portal institucional.",
        "main_flow": [
            "1. O cidadão acessa o menu 'Áreas de Atuação' da SEDH.",
            "2. O sistema renderiza uma grade com os grandes eixos de atuação (Segurança Alimentar, Assistência, etc).",
            "3. O cidadão clica em um dos eixos.",
            "4. O sistema carrega os detalhes institucionais, metas e os programas vinculados a este eixo."
        ],
        "alt_flows": [],
        "exc_flows": []
    },
    {
        "id": "UC16", "code": "RF010", "name": "Gerar relatorio automatico", "actors": ["Servidor"],
        "desc": "Gerar relatórios automaticamente, substituindo processos manuais de consolidação e análise de dados.",
        "pre": "O Servidor está consultando um painel ou aba e clica em 'Exportar/Gerar Relatório'.",
        "main_flow": [
            "1. O Servidor aciona o comando 'Gerar Relatório'.",
            "2. O ator pode optar por customizar as seções do documento [FA01].",
            "3. O sistema varre os indicadores, gráficos e tabelas presentes na tela atual.",
            "4. O sistema formata os dados em um template padrão governamental, com cabeçalho oficial da SEDH e data.",
            "5. O sistema apresenta o relatório estruturado finalizado na tela.",
            "6. O ator pode optar por baixar em formato PDF [FA02]."
        ],
        "alt_flows": [
            f"FA01 - Personalização: No passo 2, o ator engatilha o fluxo opcional (<<extend>> {md_link('UC17', 'Personalizar relatório')}).",
            f"FA02 - PDF: No passo 6, o ator escolhe a saída para download invocando o (<<extend>> {md_link('UC18', 'Emitir relatório em PDF')})."
        ],
        "exc_flows": [
            "FE01 - Timeout de Geração: No passo 3, se o relatório for gigantesco, o sistema avisa: 'Relatório extenso. Enviaremos para o seu e-mail assim que concluir'."
        ]
    },
    {
        "id": "UC17", "code": "RF011", "name": "Personalizar relatorio", "actors": ["Servidor"],
        "desc": "Permitir que o usuário personalize relatórios escolhendo formato completo ou resumido, orientação da página, programas e subseções a serem incluídas.",
        "pre": "O ator iniciou a geração de um relatório e optou por customizá-do.",
        "main_flow": [
            "1. O sistema abre a interface de Configurações de Relatório.",
            "2. O Servidor seleciona 'Modelo Resumido' ou 'Modelo Completo'.",
            "3. O Servidor seleciona as subseções que deseja (ex: Desmarcar 'Tabela Detalhada', manter 'Gráficos').",
            "4. O Servidor clica em 'Aplicar e Gerar'.",
            "5. O sistema devolve o fluxo de volta ao gerador central aplicando os filtros (UC16)."
        ],
        "alt_flows": [],
        "exc_flows": [
            "FE01 - Nenhuma Seção Selecionada: No passo 4, se o usuário desmarcar todas as sessões, o sistema avisa 'Por favor, selecione ao menos uma subseção para o relatório'."
        ]
    },
    {
        "id": "UC18", "code": "RF012", "name": "Emitir relatorio em PDF", "actors": ["Servidor"],
        "desc": "Permitir a emissão de relatórios em PDF de forma rápida, com base nos filtros e configurações escolhidos pelo usuário.",
        "pre": "O relatório finalizado está na tela aguardando a decisão de exportação.",
        "main_flow": [
            "1. O Servidor clica em 'Baixar como PDF'.",
            "2. O sistema envia o HTML consolidado para um serviço de conversão (ex: wkhtmltopdf ou jsPDF).",
            "3. O sistema gera o arquivo físico `.pdf`.",
            "4. O sistema dispara o download para o navegador do Servidor."
        ],
        "alt_flows": [
            "FA01 - Adicionar Marca d'água: No passo 2, o sistema detecta se é uma versão preliminar e carimba 'Confidencial/Rascunho' no fundo do PDF."
        ],
        "exc_flows": [
            "FE01 - Bloqueio de Popup: No passo 4, se o navegador bloquear o download, o sistema exibe um link estático: 'Clique aqui para baixar seu arquivo'."
        ]
    },
    {
        "id": "UC19", "code": "RF020", "name": "Acessar informacoes sobre programas", "actors": ["Cidadão"],
        "desc": "Permitir que cidadãos acessem informações sobre programas sociais, ações desenvolvidas e formas de participação.",
        "pre": "O Cidadão acessa o portal web ou app móvel.",
        "main_flow": [
            f"1. O sistema verifica se o cidadão está logado. Se sim, (<<include>> {md_link('UC1', 'Realizar login')}). Caso contrário, mostra a visão pública.",
            "2. O cidadão navega pela lista de programas abertos (Cartões e Banners).",
            "3. O cidadão clica em 'Saber Mais' em um programa específico.",
            "4. O sistema carrega a página detalhada, exibindo Regras, Prazos de Edital e Documentos Exigidos.",
            "5. O cidadão pode se sentir motivado e optar por se inscrever [FA01].",
            "6. O cidadão pode querer acessar informações institucionais sobre os eixos [FA02].",
            "7. O cidadão pode ter dúvidas e solicitar suporte [FA03]."
        ],
        "alt_flows": [
            f"FA01 - Ir para Inscrição: No passo 5, ele clica no botão 'Inscreva-se', e vai para o (<<include>>/Associação ao {md_link('UC20', 'Inscrever-se em programa social')}).",
            f"FA02 - Entender Eixos: No passo 6, ele acessa o menu principal e dispara (<<extend>> {md_link('UC15', 'Apresentar eixos da SEDH')}).",
            f"FA03 - Dúvidas: No passo 7, ele aciona a Central de Ajuda disparando (<<extend>> {md_link('UC21', 'Solicitar suporte/melhoria')})."
        ],
        "exc_flows": [
            "FE01 - Programa Pausado: No passo 4, se o edital estiver encerrado, exibe uma tarja vermelha 'Inscrições Encerradas'."
        ]
    },
    {
        "id": "UC20", "code": "RF021", "name": "Inscrever-se em programa social", "actors": ["Cidadão"],
        "desc": "Permitir, na área destinada ao cidadão, a realização de inscrições para participação em iniciativas ofertadas pela SEDH.",
        "pre": "O cidadão leu o edital e deseja solicitar entrada no benefício.",
        "main_flow": [
            f"1. O cidadão aciona 'Inscrever-se'. O sistema exige autenticação (<<include>> {md_link('UC1', 'Realizar login')}).",
            "2. O sistema carrega o formulário dinâmico do programa em etapas (Wizard).",
            "3. O cidadão preenche dados pessoais, residenciais e anexa comprovantes.",
            f"4. Ao inserir o CPF, o sistema valida na hora (<<include>> {md_link('UC3', 'Validar CPF')}).",
            "5. O cidadão revisa o resumo e clica em 'Enviar Inscrição'.",
            "6. O sistema salva na base, muda o status para 'Em Análise' e gera um número de protocolo."
        ],
        "alt_flows": [
            "FA01 - Salvar Rascunho: No passo 3, o cidadão decide parar na metade e clica em 'Salvar e continuar depois', guardando os dados parciais."
        ],
        "exc_flows": [
            "FE01 - Falta de Arquivo Obrigatório: No passo 5, o sistema acusa erro vermelho 'O envio do Comprovante de Residência é obrigatório'."
        ]
    },
    {
        "id": "UC21", "code": "RF019", "name": "Solicitar suporte ou melhoria", "actors": ["Cidadão"],
        "desc": "Permitir que usuários solicitem suporte técnico, inclusão de dados ou sugiram melhorias na plataforma.",
        "pre": "O ator (Cidadão ou até Servidor) encontra um problema ou deseja opinar.",
        "main_flow": [
            "1. O ator acessa o link 'Ajuda e Suporte' (ícone de interrogação flutuante ou rodapé).",
            "2. O sistema exibe um formulário de abertura de chamado com Categorias (Dúvida, Sugestão de Melhoria, Reportar Erro).",
            "3. O ator preenche o Assunto, descreve o problema e, se quiser, anexa uma captura de tela (print).",
            "4. O ator envia a solicitação.",
            "5. O sistema registra na fila do administrador e exibe o Número do Ticket na tela."
        ],
        "alt_flows": [
            "FA01 - Base de Conhecimento Rápida: No passo 2, ao digitar o Assunto, o sistema sugere FAQs automaticamente, e o usuário pode fechar o chamado se já estiver respondido ali."
        ],
        "exc_flows": []
    },
    {
        "id": "UC22", "code": "RF017", "name": "Gerenciar usuarios do sistema", "actors": ["Administrador"],
        "desc": "Permitir a gestão de usuários, incluindo cadastro, edição, controle de acesso e configuração de permissões.",
        "pre": "O Administrador acessa a aba de Painel de Controle de Usuários.",
        "main_flow": [
            f"1. O sistema assegura o privilégio master (<<include>> {md_link('UC2', 'Controlar acesso')}).",
            "2. O sistema lista a grid de usuários internos (Servidores/Assistentes) cadastrados na SEDH.",
            "3. O Administrador clica em 'Adicionar Novo Usuário'.",
            "4. O Admin preenche o e-mail, nome e seleciona a Role/Perfil (Ex: Assistente, Gestor Regional).",
            "5. O sistema dispara um convite por e-mail para a pessoa criar a senha."
        ],
        "alt_flows": [
            "FA01 - Desativar Acesso (Offboarding): No passo 2, o Admin seleciona um usuário existente e clica em 'Revogar Acesso', bloqueando login imediato.",
            "FA02 - Editar Permissões: No passo 2, o Admin acessa o perfil de alguém e adiciona/remove módulos específicos."
        ],
        "exc_flows": [
            "FE01 - E-mail Duplicado: No passo 4, se o usuário já existir, o sistema exibe 'Este servidor já possui cadastro'."
        ]
    },
    {
        "id": "UC23", "code": "RF018", "name": "Configurar ajustes administrativos", "actors": ["Administrador"],
        "desc": "Possuir páginas ou módulos de configuração para ajustes administrativos da plataforma.",
        "pre": "O Administrador acessa o módulo 'Configurações de Sistema'.",
        "main_flow": [
            "1. O Administrador seleciona a seção que deseja alterar (Textos Institucionais, Parâmetros de API, Período Letivo/Ano Base).",
            "2. O sistema exibe o formulário com os parâmetros gerais carregados em memória.",
            "3. O Administrador ajusta as chaves de configuração e salva.",
            "4. O sistema escreve as mudanças no banco de dados e limpa o cache global da aplicação para as novas configurações entrarem em vigor."
        ],
        "alt_flows": [],
        "exc_flows": [
            "FE01 - Erro de Cache: No passo 4, se o servidor não puder limpar a memória, exibe 'Configuração salva, mas as alterações podem demorar 5 minutos para refletirem no site'."
        ]
    },
    {
        "id": "UC24", "code": "RF023", "name": "Instalar app movel", "actors": ["Cidadão", "Servidor"],
        "desc": "Permitir instalação em dispositivos móveis, abrindo como aplicativo a partir do navegador.",
        "pre": "O usuário acessa o sistema de um celular Chrome/Safari que suporta Progressive Web Apps (PWA).",
        "main_flow": [
            "1. O sistema carrega a manifest.json e registra o service worker (PWA) em background.",
            "2. O navegador identifica que a aplicação pode ser instalada e exibe um prompt (Banner na tela inferior: 'Adicionar Paraíba Social à Tela Inicial').",
            "3. O usuário aceita a instalação clicando em 'Adicionar'.",
            "4. O sistema operacional gera o atalho na gaveta de apps com o logotipo do programa.",
            "5. O usuário abre o app fora do navegador (em modo standalone/fullscreen)."
        ],
        "alt_flows": [
            "FA01 - Instalação Manual: No passo 2, se o prompt automático não aparecer, o usuário clica nas opções do navegador -> 'Instalar Aplicativo'."
        ],
        "exc_flows": [
            "FE01 - Armazenamento Cheio: No passo 3, o OS do celular cancela a instalação e avisa falta de espaço."
        ]
    },
    {
        "id": "UC25", "code": "RF024", "name": "Sincronizar com Sheets", "actors": ["Sistema"],
        "desc": "Recuperar e armazenar dados por meio de integração com a API do Google Sheets enquanto essa for a camada de dados adotada.",
        "pre": "O painel (UC4) necessita de dados novos ou um cronograma (job) roda à meia-noite.",
        "main_flow": [
            "1. O backend do sistema inicia o worker de sincronização.",
            "2. O sistema autentica usando a Service Account contra a API do Google (OAuth2).",
            "3. O sistema requisita o conteúdo JSON da(s) aba(s) da planilha principal da SEDH.",
            "4. O sistema parseia as linhas, identifica atualizações de dados e insere as informações estruturadas em seu banco de dados local.",
            "5. O sistema atualiza o cache e finaliza o log com 'Sincronização com Sucesso'."
        ],
        "alt_flows": [
            "FA01 - Sincronização Sob Demanda: No passo 1, o Servidor aperta o botão manual 'Sincronizar Agora' na interface, forçando a execução da rotina imediatamente."
        ],
        "exc_flows": [
            "FE01 - Falha na API: No passo 2, se a API do Google retornar Erro 429 (Too Many Requests), o sistema agenda uma retentativa automática (backoff/retry).",
            "FE02 - Colunas Modificadas: No passo 4, se o operador da planilha trocou o nome de uma coluna crítica, o sistema aborta o sync parcial e envia um e-mail de alerta ao Administrador."
        ]
    }
]

for uc in use_cases_data:
    filename = f"especificacao_{slugify(uc['name'])}.md"
    filepath = os.path.join(base_dir, filename)
    
    actor_str = ", ".join(uc['actors'])
    
    # Format main flows
    main_flow_str = "<br>".join(uc['main_flow'])
    
    # Format alternative flows with generic FA message if empty
    alt_flow_str = "<br>".join(uc['alt_flows']) if uc['alt_flows'] else "Não existem fluxos alternativos definidos para este caso de uso."
    
    # Format exception flows with generic FE message if empty
    exc_flow_str = "<br>".join(uc['exc_flows']) if uc['exc_flows'] else "Não existem fluxos de exceção críticos para este caso de uso."
    
    content = f'''# Especificação de Caso de Uso: {uc['name']}

Esta especificação detalhada mapeia os fluxos da interface e integração conforme as melhores práticas, referenciando ativamente outras funcionalidades.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | {uc['id']} - {uc['name']} |
| **Objetivo** | {uc['desc']} |
| **Requisitos Relacionados** | {uc['code']} |
| **Atores** | {actor_str} |
| **Condição de Entrada** | {uc['pre']} |
| **Fluxo Principal** | {main_flow_str} |
| **Fluxos Alternativos** | {alt_flow_str} |
| **Fluxos de Exceção** | {exc_flow_str} |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo foi alcançado com sucesso através da tela/ação final. |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Voltar para a Visão Geral de Casos de Uso (Diagrama)</a>
</div>
'''
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Todas as 25 especificacoes foram reescritas com detalhes unicos, tags FA e cross-links! 🚀")
