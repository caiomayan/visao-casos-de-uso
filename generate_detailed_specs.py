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

use_cases_data = [
    {
        "id": "UC1", "code": "RF001", "name": "Realizar login", "actors": ["Cidadão", "Servidor", "Admin"],
        "desc": "Permitir que usuários realizem login para acessar as áreas internas da plataforma, especialmente dashboards, relatórios, gestão e módulos administrativos.",
        "pre": "O ator não está autenticado no sistema.",
        "data_seen": "Tela de Login contendo campos para e-mail e senha, botão de confirmação e link de recuperação.",
        "data_input": "E-mail de acesso, Senha.",
        "main_flow": [
            "1. O ator acessa a página inicial do sistema e clica em 'Entrar'.",
            "2. O sistema redireciona para a tela de autenticação do Clerk.",
            "3. O ator informa suas credenciais (E-mail e Senha) ou escolhe o login via provedor externo.",
            "4. O Clerk valida as credenciais.",
            "5. O sistema recebe o token de autenticação, registra a sessão e redireciona o ator para o painel apropriado."
        ],
        "alt_flows": ["FA01 - Esqueci a Senha: No passo 3, o ator clica em 'Esqueci minha senha', e o sistema envia um e-mail de recuperação."],
        "exc_flows": ["FE01 - Credenciais Inválidas: No passo 4, se a senha for incorreta, o sistema exibe 'Usuário ou senha inválidos'."]
    },
    {
        "id": "UC2", "code": "RF002", "name": "Controlar acesso", "actors": ["Admin", "Sistema"],
        "desc": "Controlar o acesso dos usuários conforme sessões, perfis e permissões.",
        "pre": "O ator tenta acessar uma rota ou módulo protegido do sistema.",
        "data_seen": "Tela solicitada renderizada normalmente ou Tela de Erro 403 (Acesso Negado) caso seja bloqueado.",
        "data_input": "Nenhum (validação transparente de sessão/cookie em background).",
        "main_flow": [
            "1. O ator solicita o acesso a um módulo restrito.",
            "2. O sistema intercepta a requisição e verifica o token de sessão ativo.",
            "3. O sistema consulta as permissões vinculadas ao perfil do ator.",
            "4. O sistema confirma que o perfil possui acesso àquele recurso.",
            "5. O sistema carrega e exibe o módulo solicitado."
        ],
        "alt_flows": ["FA01 - Perfil com Restrição Parcial: No passo 4, se tiver permissão apenas de leitura, o sistema oculta botões de edição."],
        "exc_flows": ["FE01 - Acesso Negado: No passo 4, se não tiver permissão, o sistema exibe 'Acesso Negado (403)' e bloqueia o recurso."]
    },
    {
        "id": "UC3", "code": "RF025", "name": "Validar CPF", "actors": ["Admin", "Sistema"],
        "desc": "Utilizar o Cadastro de Pessoa Física (CPF) como identificador único na checagem de dados.",
        "pre": "Um fluxo de cadastro ou inscrição solicita o CPF do Cidadão.",
        "data_seen": "Processamento invisível ao usuário direto; ou Notificação de erro ('CPF Inválido/Duplicado') no formulário de origem.",
        "data_input": "Número de CPF digitado pelo Cidadão (11 dígitos).",
        "main_flow": [
            "1. O sistema recebe a entrada do CPF fornecido pelo ator.",
            "2. O sistema executa o algoritmo de validação matemática do CPF.",
            "3. O sistema consulta a base de dados interna da SEDH para verificar se já está vinculado.",
            "4. O sistema retorna o status de CPF válido e liberado para a operação."
        ],
        "alt_flows": [],
        "exc_flows": ["FE01 - CPF Inválido: Falha na matemática.", "FE02 - CPF Duplicado: Cidadão já cadastrado."]
    },
    {
        "id": "UC4", "code": "RF003", "name": "Visualizar painel", "actors": ["Servidor"],
        "desc": "Apresentar um painel principal com indicadores consolidados.",
        "pre": "O Servidor acessa o endereço principal do Dashboard.",
        "data_seen": "Painel de controle com cartões de indicadores (KPIs de inscritos/orçamento), menus laterais e barra superior.",
        "data_input": "Cliques para navegação nas abas, e seleção de parâmetros nos menus de filtro.",
        "main_flow": [
            f"1. O Servidor efetua o login (<<include>> {md_link('UC1', 'Realizar login')}).",
            f"2. O sistema valida as permissões (<<include>> {md_link('UC2', 'Controlar acesso')}).",
            f"3. O sistema requisita a atualização de dados externos (<<include>> {md_link('UC25', 'Sincronizar com Sheets')}).",
            "4. O sistema renderiza a tela principal com os cartões de indicadores globais.",
            "5. O Servidor visualiza os resumos socioeconômicos.",
            "6. O Servidor opta por visualizar os gráficos detalhados [FA01].",
            "7. O Servidor opta por filtrar os dados [FA02].",
            "8. O Servidor opta por consolidar programas específicos [FA03]."
        ],
        "alt_flows": [
            f"FA01 - Gráficos: Ativa (<<include>> {md_link('UC6', 'Visualizar graficos')}).",
            f"FA02 - Filtros: Ativa (<<include>> {md_link('UC5', 'Filtrar dados')}).",
            f"FA03 - Consolidar: Ativa (<<include>> {md_link('UC8', 'Consolidar dados')})."
        ],
        "exc_flows": ["FE01 - Falha no Carregamento: Exibe aviso de 'Dados indisponíveis'."]
    },
    {
        "id": "UC5", "code": "RF004", "name": "Filtrar dados", "actors": ["Servidor"],
        "desc": "Permitir filtrar os dados por município e por regional.",
        "pre": "O Servidor está no painel de indicadores.",
        "data_seen": "Modal ou Menu Lateral contendo Caixas de Seleção (Dropdowns) listando Municípios e Regionais de Atendimento.",
        "data_input": "Seleção de um ou múltiplos municípios, Seleção de regional.",
        "main_flow": [
            "1. O Servidor clica no botão 'Filtros Avançados'.",
            "2. O sistema abre o modal contendo as opções geográficas.",
            "3. O Servidor seleciona uma ou mais opções nos campos.",
            "4. O Servidor clica em 'Aplicar'.",
            "5. O sistema recalcula as agregações e atualiza os gráficos do painel."
        ],
        "alt_flows": ["FA01 - Limpar Filtros: O ator clica em 'Limpar Filtros' para recarregar a visão global do Estado."],
        "exc_flows": ["FE01 - Região sem Dados: O sistema exibe gráficos zerados com 'Nenhum dado encontrado' se o município não tiver programas ativos."]
    },
    {
        "id": "UC6", "code": "RF005", "name": "Visualizar graficos", "actors": ["Servidor"],
        "desc": "Exibir gráficos para facilitar a interpretação dos dados ao longo do tempo.",
        "pre": "O Servidor solicitou a visualização gráfica no Painel.",
        "data_seen": "Área central desenhando gráficos de barras (comparativos) e linhas (evolução temporal), com legendas dinâmicas.",
        "data_input": "Cliques em botões de filtro gráfico (ex: Mudar para formato 'Pizza') e movimento do mouse sobre os gráficos (efeito Hover) para ler números exatos.",
        "main_flow": [
            "1. O sistema compila o conjunto atual de dados em arrays para plotagem.",
            "2. O sistema carrega a biblioteca de renderização gráfica.",
            "3. O sistema exibe um gráfico de barras comparativo entre municípios.",
            "4. O sistema exibe um gráfico de linhas mostrando a evolução nos últimos 12 meses.",
            "5. O Servidor passa o mouse sobre os gráficos para consultar valores pontuais."
        ],
        "alt_flows": ["FA01 - Alternar Gráfico: No passo 3, trocar formato de barras para pizza."],
        "exc_flows": ["FE01 - Erro de Renderização: Fallback exibindo tabela plana caso o plugin de gráficos não carregue."]
    },
    {
        "id": "UC7", "code": "RF006", "name": "Identificar padroes", "actors": ["Servidor"],
        "desc": "Permitir identificar tendências e mudanças nos indicadores sociais.",
        "pre": "O Servidor acessa o módulo Analítico Avançado.",
        "data_seen": "Caixas de texto (Cards) destacando 'Insights Automatizados' curtos, e botão 'Exportar Destaque'.",
        "data_input": "Cliques nos botões de feedback do insight (Útil / Não Útil).",
        "main_flow": [
            "1. O Servidor acessa a aba 'Análise de Padrões'.",
            "2. O sistema processa análise matemática básica sobre o histórico.",
            "3. O sistema apresenta caixas de texto com insights automáticos (ex: 'O programa X cresceu 20%').",
            "4. O Servidor sinaliza se o alerta foi útil para o algoritmo registrar a preferência."
        ],
        "alt_flows": ["FA01 - Exportar Insight: No passo 3, baixar a imagem em formato PNG contendo o insight para uso em slides."],
        "exc_flows": ["FE01 - Dados Insuficientes: Exibição de aviso caso haja menos de 3 meses de histórico para análise confiável."]
    },
    {
        "id": "UC8", "code": "RF007", "name": "Consolidar dados", "actors": ["Servidor"],
        "desc": "Reunir dados de diferentes programas, setores e bases em uma plataforma única.",
        "pre": "O Servidor necessita cruzar informações de secretarias ou programas distintos.",
        "data_seen": "Painel de seleção com caixas de marcação (Checkboxes) listando todos os programas, e uma Tabela final consolidada tipo Planilha (Grid).",
        "data_input": "Seleção (Click) em quais programas devem ser mesclados e escolha do campo em comum (ex: 'Mesclar por Município').",
        "main_flow": [
            "1. O Servidor seleciona a opção 'Cruzamento de Programas'.",
            "2. O sistema lista todos os programas com bases de dados ativas.",
            "3. O Servidor seleciona 2 ou mais programas e a chave de união.",
            "4. O sistema roda a query de união consolidando os números.",
            "5. O sistema exibe uma tabela mestre contendo a visão macro."
        ],
        "alt_flows": [],
        "exc_flows": ["FE01 - Bases Incompatíveis: Exibe erro se as estruturas de dados não puderem ser mescladas pela chave escolhida."]
    },
    {
        "id": "UC9", "code": "RF008", "name": "Acompanhar execucao", "actors": ["Servidor"],
        "desc": "Permitir o acompanhamento dos programas sociais executados pela SEDH.",
        "pre": "O Servidor acessa a listagem de Programas.",
        "data_seen": "Tabela com lista de programas contendo Nome, Responsável, Orçamento Gasto (%) e Status colorido.",
        "data_input": "Campo de pesquisa por texto (Nome do programa) e Clique para acessar detalhes.",
        "main_flow": [
            "1. O Servidor abre a aba 'Monitoramento de Execução'.",
            "2. O sistema exibe a lista de todos os programas ativos com status geral.",
            "3. O Servidor clica em um programa específico.",
            f"4. O sistema direciona para (<<include>> {md_link('UC10', 'Visualizar pagina do programa')}).",
            "5. O Servidor verifica a taxa de conversão (Inscritos vs Beneficiados).",
            "6. O Servidor solicita geração de relatório do acompanhamento [FA01]."
        ],
        "alt_flows": [f"FA01 - Gerar Relatório: Dispara (<<include>> {md_link('UC16', 'Gerar relatorio automatico')})."],
        "exc_flows": []
    },
    {
        "id": "UC10", "code": "RF009", "name": "Visualizar pagina do programa", "actors": ["Servidor"],
        "desc": "Disponibilizar páginas individuais para cada programa social.",
        "pre": "O ator clica no nome de um Programa Específico.",
        "data_seen": "Uma página completa estilo 'Dashboard de Projeto' com Cabeçalho Textual, Barra de Orçamento preenchida, e abas de navegação (Mapa, Perfil, Ranking).",
        "data_input": "Navegação via cliques nas Abas superiores.",
        "main_flow": [
            "1. O sistema carrega os metadados do programa (Nome, Data, Eixo).",
            "2. O sistema renderiza a tela com as informações descritivas e KPIs focados.",
            "3. O Servidor analisa a página.",
            "4. O Servidor clica na aba de mapa geográfico [FA01].",
            "5. O Servidor clica na aba demográfica de perfis [FA02].",
            "6. O Servidor clica na aba de liderança de cidades [FA03]."
        ],
        "alt_flows": [
            f"FA01 - Ver Mapa: Ativa (<<extend>> {md_link('UC11', 'Visualizar mapa')}).",
            f"FA02 - Ver Perfis: Ativa (<<extend>> {md_link('UC12', 'Visualizar dados por perfil')}).",
            f"FA03 - Ver Rankings: Ativa (<<extend>> {md_link('UC13', 'Visualizar rankings')})."
        ],
        "exc_flows": ["FE01 - Programa Inexistente: Sistema avisa 'Programa não encontrado' caso o link esteja corrompido."]
    },
    {
        "id": "UC11", "code": "RF013", "name": "Visualizar mapa", "actors": ["Servidor"],
        "desc": "Visualizar a distribuição espacial dos programas no território paraibano.",
        "pre": "O ator ativa a visão de mapa.",
        "data_seen": "Mapa da Paraíba renderizado (ex: Google Maps API), com as fronteiras das cidades pintadas com intensidade de cor variada (escala de calor).",
        "data_input": "Movimentos de Rolagem (Zoom in/Zoom out) e Cliques em cima do polígono do Município escolhido.",
        "main_flow": [
            "1. O sistema inicia o módulo de mapa coroplético focado na Paraíba.",
            "2. O sistema busca coordenadas geográficas e pinta os municípios.",
            "3. O Servidor aproxima e clica no município de Campina Grande, por exemplo.",
            "4. O sistema sobrepõe um Tooltip/Pop-up com o total exato de investimentos na cidade escolhida."
        ],
        "alt_flows": ["FA01 - Visão Satélite: Ator alterna o botão de camada de mapa para 'Satélite'."],
        "exc_flows": ["FE01 - Ausência de Polígono: Se faltarem coordenadas geográficas de uma cidade, ela é listada isoladamente numa tabela abaixo do mapa."]
    },
    {
        "id": "UC12", "code": "RF014", "name": "Visualizar dados por perfil", "actors": ["Servidor"],
        "desc": "Visualização dos dados demográficos dos atendidos pelo programa.",
        "pre": "O ator ativa a aba Demográfica.",
        "data_seen": "Painel de Gráficos de Pizza ou de Barras Horizontais com recortes de Idade (0-18, 18-35...), Gênero, Renda e Nível Escolar.",
        "data_input": "Botão de 'Exportar Relatório CSV' ou Passar o Mouse (Hover) sobre os recortes para ver o valor exato.",
        "main_flow": [
            "1. O sistema consulta as tabelas demográficas daquele programa.",
            "2. O sistema separa e calcula percentuais por Faixa Etária, Gênero, Renda e Escolaridade.",
            "3. O sistema renderiza os gráficos específicos na tela.",
            "4. O Servidor visualiza os painéis para verificar a distribuição e o público primário afetado."
        ],
        "alt_flows": ["FA01 - Exportar Dados Abertos: O ator clica em 'Baixar Microdados' para gerar a tabela .csv anônima."],
        "exc_flows": []
    },
    {
        "id": "UC13", "code": "RF015", "name": "Visualizar rankings", "actors": ["Servidor"],
        "desc": "Apresentar rankings para apoiar a leitura comparativa.",
        "pre": "O ator ativa a aba de Rankings.",
        "data_seen": "Lista textual numerada no formato de pódio (Top 1 a 10) e uma tabela com os municípios de piores posições, acompanhados de setas de subida verde e descida vermelha.",
        "data_input": "Dropdown de seleção de Critério: 'Ordem por Orçamento' ou 'Ordem por Pessoas Atendidas'.",
        "main_flow": [
            "1. O sistema ordena os municípios ou regionais decrescentemente pelo critério padrão.",
            "2. O sistema renderiza a tela de Leaderboard (Top 10 / Bottom 10).",
            "3. O sistema insere alertas de variação (trend arrows) mostrando quem subiu ou caiu na última semana.",
            "4. O Servidor analisa os dados."
        ],
        "alt_flows": ["FA01 - Mudar Critério: O Servidor altera o Dropdown para ordenar os piores baseados em rejeição de matrículas."],
        "exc_flows": []
    },
    {
        "id": "UC14", "code": "RF016", "name": "Avaliar inscricoes", "actors": ["Assistente Social"],
        "desc": "Análise de inscrições submetidas por cidadãos.",
        "pre": "O cidadão enviou a inscrição (via UC20) e ela encontra-se na Fila de Análise.",
        "data_seen": "Tela dividida: Lado esquerdo exibe as respostas do formulário (Nome, Renda Informada); Lado direito exibe as fotos ou PDFs dos comprovantes para auditoria visual. Botões verde (Aprovar) e vermelho (Rejeitar).",
        "data_input": "Cliques nos botões de Aprovar/Rejeitar; Preenchimento da caixa de texto (textarea) para inserir o Motivo da Recusa Técnica.",
        "main_flow": [
            "1. A Assistente Social abre a fila de 'Solicitações Pendentes'.",
            "2. O sistema exibe o painel de avaliação unificado com documentos anexados abertos nativamente no lado direito da tela.",
            "3. A Assistente lê e confronta o que foi digitado com o que foi anexado.",
            "4. A Assistente clica em 'Aprovar' ou 'Rejeitar'.",
            "5. Se rejeitar, o sistema exige uma justificativa de texto [FA01].",
            "6. O sistema grava o status auditado e notifica o Cidadão por e-mail."
        ],
        "alt_flows": [
            "FA01 - Exigir Justificativa: No passo 5, trava o avanço até o ator justificar legalmente a recusa.",
            "FA02 - Solicitar Reenvio (Pendente): Em vez de rejeitar de vez, o ator clica em 'Pedir Novo Documento', deixando o ticket em suspenso."
        ],
        "exc_flows": ["FE01 - Anexo Corrompido: A imagem enviada pelo cidadão não carrega, forçando o acionamento automático da pendência via FA02."]
    },
    {
        "id": "UC15", "code": "RF022", "name": "Apresentar eixos da SEDH", "actors": ["Cidadão"],
        "desc": "Apresentar os principais eixos de atuação da secretaria de forma didática.",
        "pre": "O cidadão acessa o menu institucional.",
        "data_seen": "Página estática informativa (Landing Page) contendo Grandes Blocos Iconográficos com ilustrações dos eixos (Segurança Alimentar, Direitos Humanos, etc). Textos descritivos logo abaixo.",
        "data_input": "Cliques nos botões 'Saber mais' ou ícones para expandir os textos detalhados de cada bloco.",
        "main_flow": [
            "1. O cidadão acessa o link 'Conheça nossos Eixos de Atuação'.",
            "2. O sistema renderiza os blocos visuais de áreas finalísticas.",
            "3. O cidadão clica no bloco de 'Assistência Social'.",
            "4. O sistema expande o texto com o objetivo do eixo e os programas vinculados (com hiperlinks para acesso)."
        ],
        "alt_flows": [],
        "exc_flows": []
    },
    {
        "id": "UC16", "code": "RF010", "name": "Gerar relatorio automatico", "actors": ["Servidor"],
        "desc": "Gerar relatórios de tela automaticamente substituindo tarefas manuais.",
        "pre": "O Servidor está analisando um painel e deseja extrair o panorama em formato documento.",
        "data_seen": "Visão Prévia (Preview) formatada em uma moldura A4 na tela, incluindo o Brasão oficial do Estado no cabeçalho e os gráficos e tabelas compilados no corpo da página.",
        "data_input": "Botões de topo de barra para 'Personalizar Estrutura', 'Imprimir' e 'Baixar em PDF'.",
        "main_flow": [
            "1. O Servidor aperta o botão flutuante 'Gerar Relatório Oficial'.",
            "2. O Servidor pode personalizar o conteúdo do documento [FA01].",
            "3. O sistema captura nativamente o estado atual do painel (tabelas e gráficos formatados).",
            "4. O sistema envelopa isso no Template Oficial da SEDH e exibe no formato A4 em tela.",
            "5. O Servidor encerra pedindo a exportação para seu computador [FA02]."
        ],
        "alt_flows": [
            f"FA01 - Personalizar: Ativa menu lateral via (<<extend>> {md_link('UC17', 'Personalizar relatorio')}).",
            f"FA02 - Emitir PDF: Inicia o fluxo de arquivo via (<<extend>> {md_link('UC18', 'Emitir relatorio em PDF')})."
        ],
        "exc_flows": ["FE01 - Tempo Excedido: Se as tabelas ultrapassarem centenas de páginas, ele exibe um loader e promete envio via e-mail corporativo em background."]
    },
    {
        "id": "UC17", "code": "RF011", "name": "Personalizar relatorio", "actors": ["Servidor"],
        "desc": "Permitir personalizar a estrutura dos relatórios formatados.",
        "pre": "O ator clicou em 'Configurações do Relatório' durante o processo de visualização.",
        "data_seen": "Menu lateral retrátil (Drawer) com Caixas de Seleção (Checkboxes) listando os blocos que compõem o documento: 'Incluir Resumo de Texto', 'Incluir Análise Demográfica', 'Incluir Lista de Nomes'.",
        "data_input": "Checagem (Marcação) visual das caixas listando o que o usuário deseja na impressão. Botão de 'Aplicar Seleção'.",
        "main_flow": [
            "1. O sistema mostra um menu deslizante ao lado direito.",
            "2. O ator desmarca a opção 'Incluir Detalhamento de Tabelas Brutas' para deixar o relatório mais limpo.",
            "3. O ator escolhe a orientação de layout 'Retrato' ou 'Paisagem'.",
            "4. O ator clica em 'Aplicar Modificações'.",
            "5. O sistema recarrega a janela do UC base ocultando as seções apagadas pelo usuário."
        ],
        "alt_flows": [],
        "exc_flows": ["FE01 - Seleção Vazia: O sistema bloqueia a aplicação se o ator desmarcar todas as caixas, exibindo 'Você deve selecionar no mínimo uma sessão'."]
    },
    {
        "id": "UC18", "code": "RF012", "name": "Emitir relatorio em PDF", "actors": ["Servidor"],
        "desc": "Consolidar os dados em arquivo portável e emitir PDF para download rápido.",
        "pre": "O relatório na tela encontra-se finalizado e o usuário solicitou o download.",
        "data_seen": "Indicador de Carregamento ('Gerando PDF...') seguido pelas janelas nativas do navegador para indicar onde salvar o arquivo físico no computador.",
        "data_input": "Definição opcional do nome do arquivo (ex: Relatorio_Jan2026.pdf) na janela de sistema operacional local.",
        "main_flow": [
            "1. O ator clica no botão com ícone de PDF.",
            "2. O sistema despacha a visualização HTML atual para um conversor backend seguro.",
            "3. O backend carimba data, assinatura digital ou hash criptográfico garantindo que é um doc original.",
            "4. O backend converte as fontes e vetores para o arquivo binário .pdf real.",
            "5. O sistema envia a resposta ao Browser, forçando a janela de download automático no navegador do ator."
        ],
        "alt_flows": ["FA01 - Adição de Rascunho: O servidor estampa a palavra 'Preliminar' como marca d'água invisível de PDF, caso o período consultado ainda não tenha acabado."],
        "exc_flows": ["FE01 - Erro de Biblioteca de Conversão: Exibe 'Falha de Servidor ao Gerar PDF. Tente novamente mais tarde'."]
    },
    {
        "id": "UC19", "code": "RF020", "name": "Acessar informacoes sobre programas", "actors": ["Cidadão"],
        "desc": "Consultar na área pública as informações de todos os projetos governamentais.",
        "pre": "O Cidadão navega ao portal aberto.",
        "data_seen": "Lista de Cartões informativos (Cards) organizados em grades. Cada um mostra: Título do Edital, Status, Ícone do Eixo de Atuação.",
        "data_input": "Termos de pesquisa na barra de busca (Buscar por Programa) e cliques nos próprios cartões informativos.",
        "main_flow": [
            f"1. O sistema verifica a autenticação transparente (<<include>> {md_link('UC1', 'Realizar login')}), mas permite acesso público.",
            "2. O sistema exibe o grid de editais e programas.",
            "3. O Cidadão clica em um programa de transferência de renda.",
            "4. O sistema carrega a descrição oficial detalhada de contrapartidas, regras de participação e valores do auxílio.",
            "5. O cidadão pode querer entender melhor as diretrizes do governo antes [FA01].",
            "6. O cidadão percebe que não tem direito e quer questionar o edital [FA02].",
            "7. O cidadão entende os requisitos e deseja se cadastrar diretamente pela página [FA03]."
        ],
        "alt_flows": [
            f"FA01 - Áreas da SEDH: (<<extend>> {md_link('UC15', 'Apresentar eixos da SEDH')}).",
            f"FA02 - Sugestões/Reclamações: (<<extend>> {md_link('UC21', 'Solicitar suporte ou melhoria')}).",
            f"FA03 - Fazer Cadastro: Botão central que leva a (<<include>> implicitamente no fluxo {md_link('UC20', 'Inscrever-se em programa social')})."
        ],
        "exc_flows": ["FE01 - Página Não Encontrada: Programa retirado do ar exibe erro 404 e recomenda acesso à home."]
    },
    {
        "id": "UC20", "code": "RF021", "name": "Inscrever-se em programa social", "actors": ["Cidadão"],
        "desc": "Realizar cadastro via preenchimento digital de informações.",
        "pre": "O cidadão aceitou os termos e quer enviar sua solicitação.",
        "data_seen": "Formulário sequencial estruturado em etapas (Stepper: Passo 1 - Pessoal, Passo 2 - Contato, Passo 3 - Anexos). Um campo de File Upload em área tracejada para arquivos.",
        "data_input": "Textos (Nome Completo, Identidade, Renda), CPF, Seleção Sim/Não em questionário socioeconômico e envio físico (Upload) de arquivos PDF ou JPG.",
        "main_flow": [
            f"1. O cidadão clica em Inscrição. O sistema trava a tela e exige login do governo (<<include>> {md_link('UC1', 'Realizar login')}).",
            "2. O cidadão insere os dados da Ficha de Solicitação.",
            f"3. Ao preencher o CPF, há disparo de evento Javascript que o envia à checagem de banco da SEDH (<<include>> {md_link('UC3', 'Validar CPF')}).",
            "4. O cidadão faz o Upload das fotos de Comprovante de Endereço ou Laudos.",
            "5. O cidadão clica em 'Finalizar Inscrição'.",
            "6. O sistema exibe modal verde com número de protocolo final."
        ],
        "alt_flows": ["FA01 - Salvar Rascunho Automático: Se o usuário fechar a aba no Passo 2 e voltar amanhã, o sistema preserva os campos no LocalStorage."],
        "exc_flows": ["FE01 - Arquivo Muito Grande: Ao enviar o PDF no passo 4, sistema grita 'Tamanho máximo de 5MB ultrapassado' e bloqueia finalização."]
    },
    {
        "id": "UC21", "code": "RF019", "name": "Solicitar suporte ou melhoria", "actors": ["Cidadão"],
        "desc": "Acesso a Ouvidoria e canais de ajuda técnicos para resolução de dúvidas e melhorias.",
        "pre": "O usuário encontra problemas ou dúvidas de navegação.",
        "data_seen": "Formulário de Abertura de Chamado contendo: Dropdown de Categoria, Caixa de Título (Assunto) e Caixa de Texto Longo (Textarea).",
        "data_input": "Seleção da Categoria ('Dúvida de Acesso', 'Erro de Tela'), Escrita do texto explicativo da falha encontrada, Upload de Screenshot opcional.",
        "main_flow": [
            "1. O ator clica no botão 'Ajuda e Suporte' flutuante na tela.",
            "2. O sistema mostra o formulário de ticket da Ouvidoria/Suporte.",
            "3. O ator preenche o Assunto e fornece o máximo de detalhes textuais do bug.",
            "4. O ator anexa uma imagem da tela (print).",
            "5. O ator submete e o sistema confirma com a geração do número do ticket de suporte rastreável."
        ],
        "alt_flows": ["FA01 - Exibir Autoajuda FAQ: Ao digitar palavras como 'senha' no título, o sistema detecta a palavra e recomenda: 'Veja como redefinir sua senha aqui', interceptando o ticket para o usuário nem precisar enviar."],
        "exc_flows": []
    },
    {
        "id": "UC22", "code": "RF017", "name": "Gerenciar usuarios do sistema", "actors": ["Administrador"],
        "desc": "Ajuste e controle base de acesso de servidores públicos na infraestrutura de software.",
        "pre": "O Administrador Master abre o Painel Configurações de Pessoas.",
        "data_seen": "Tabela crua (Data Grid) listando os nomes dos funcionários públicos do Estado e seus níveis de Perfil no sistema. Modal (janela sobreposta) com o Formulário de Criação.",
        "data_input": "Campos de texto para Nome/Email; Botão 'Desativar Conta'; Caixas Dropdown listando os perfis técnicos ('Assistente', 'Gestor Regional', etc).",
        "main_flow": [
            f"1. O sistema assegura que só Masters entrem aqui (<<include>> {md_link('UC2', 'Controlar acesso')}).",
            "2. O Administrador observa a grade de contas.",
            "3. O Administrador aciona 'Adicionar Novo Usuário'.",
            "4. O Admin fornece E-mail Institucional e amarra ao perfil operacional correto.",
            "5. O sistema faz interface com o provedor de identidade (Clerk) criando o perfil, e dispara notificação de boas-vindas na caixa de e-mail do servidor listado."
        ],
        "alt_flows": ["FA01 - Bloqueio Emergencial: Em vez de criar conta, o admin acha o e-mail de um ex-funcionário na grid e clica no ícone de lixeira. O sistema imediatamente derruba a sessão logada dele."],
        "exc_flows": ["FE01 - Duplicidade de E-mail de Servidor: 'E-mail corporativo fornecido já consta atrelado a outra conta'."]
    },
    {
        "id": "UC23", "code": "RF018", "name": "Configurar ajustes administrativos", "actors": ["Administrador"],
        "desc": "Gerir parâmetros estáticos, chaves (flags) e strings da interface a partir do banco de dados.",
        "pre": "O administrador acessa o submódulo 'Configuração Geral'.",
        "data_seen": "Painel de controle com abas de separação (ex: 'Variáveis de Integração', 'Textos Home'), preenchidos com Chaves de Interruptor (Toggles On/Off) e campos numéricos.",
        "data_input": "Ligar/desligar botões toggle de funcionalidades beta, alterar valor numérico ('Total de inscrições por vez'), digitação de textos institucionais das áreas.",
        "main_flow": [
            "1. O sistema recupera e exibe a cópia atual das configurações do banco.",
            "2. O Admin navega para a aba de Configuração de Limites do Ano.",
            "3. O Admin altera a variável de limite de data final de todos os editais vigentes e aciona 'Salvar Alterações Globais'.",
            "4. O sistema atualiza o banco primário.",
            "5. O sistema envia sinal de purga de cache a todas as instâncias hospedadas do site, renovando a interface de todos instantaneamente."
        ],
        "alt_flows": [],
        "exc_flows": ["FE01 - Parâmetro Crítico Vazio: Se o Admin apagar toda uma variável obrigatória, o sistema bloqueia o save dizendo 'Valor Não Pode Ser Nulo'."]
    },
    {
        "id": "UC24", "code": "RF023", "name": "Instalar app movel", "actors": ["Cidadão", "Servidor"],
        "desc": "Instalação da plataforma web (PWA) de forma encapsulada como aplicativo mobile no dispositivo final.",
        "pre": "O usuário entra com Chrome ou Safari num smartphone compatível e o Service Worker do sistema é carregado ativamente no background.",
        "data_seen": "Uma barra sutil no rodapé do navegador sugerindo: 'Adicionar Paraíba Social à sua Tela Inicial'. Se aceitar, vê ícone final do programa aparecendo junto com outros Apps no celular.",
        "data_input": "Toque no botão 'Instalar / Aceitar' da caixa de diálogo nativa do Sistema Operacional (Android / iOS).",
        "main_flow": [
            "1. O navegador processa o arquivo `manifest.json` do sistema e exibe o Banner Automático nativo convidando a instalação.",
            "2. O usuário toca na opção nativa de 'Adicionar App'.",
            "3. O Sistema Operacional cria um atalho contendo ícone oficial em alta resolução.",
            "4. O usuário fecha o navegador Safari/Chrome e lança o atalho novo.",
            "5. A aplicação agora roda como App Autônomo e abre em tela limpa sem barras de endereços."
        ],
        "alt_flows": ["FA01 - Prompt Manual: Se a dica não abrir sozinha, o usuário utiliza as próprias opções do menu lateral do navegador (botão de 3 pontinhos) e aperta a opção embutida."],
        "exc_flows": ["FE01 - Limite de Espaço Storage: Erro nativo do dispositivo interrompe a criação do atalho do PWA por limite de MB da memória flash do smartphone."]
    },
    {
        "id": "UC25", "code": "RF024", "name": "Sincronizar com Sheets", "actors": ["Sistema"],
        "desc": "Atualização e integração com API de fontes externas.",
        "pre": "Job agendado é iniciado (CRON) ou disparo forçado na interface de Administrador.",
        "data_seen": "Visão técnica invisível de background. Para administradores, apenas um painel de Logs de Status confirmando Data do Último Sync bem-sucedido.",
        "data_input": "Absolutamente nenhum input de teclado requerido, é máquina falando com máquina (M2M) exceto credenciais pré-programadas do GCP (Google Cloud Project).",
        "main_flow": [
            "1. O servidor Node.js/Python acorda e inicia o script de Worker em fila de processamento.",
            "2. O sistema realiza handshake JWT autenticando o serviço perante o servidor das APIs Cloud do Google.",
            "3. O sistema roda método GET requerendo os blocos de dados de formato aberto na planilha central das SEDH.",
            "4. A API devolve o JSON; O sistema detecta colunas inalteradas (fazendo parse rápido) e detecta atualizações, salvando no banco POSTGRESQL ou Mongo nativo.",
            "5. O sistema termina silenciosamente e marca log verde (Sucesso) pro Dashboard UC4 acessar atualizado imediatamente."
        ],
        "alt_flows": ["FA01 - Botão Manual: O Admin vai no submódulo e clica em Forçar Atualização Imediata (Trigger Sync), bypassando a rotina da noite."],
        "exc_flows": [
            "FE01 - Limite Google: Erro 429 Too Many Requests emitido pelo Google, script aciona protocolo 'Backoff Exponencial' de retentativa 5 min depois.",
            "FE02 - Planilha Corrompida ou Alterada por Humano Inadequado: As colunas sumiram. O Worker cancela o Sync parcial pra não estragar banco atual e joga alerta."
        ]
    }
]

for uc in use_cases_data:
    filename = f"especificacao_{slugify(uc['name'])}.md"
    filepath = os.path.join(base_dir, filename)
    
    actor_str = ", ".join(uc['actors'])
    main_flow_str = "<br>".join(uc['main_flow'])
    alt_flow_str = "<br>".join(uc['alt_flows']) if uc['alt_flows'] else "Nenhum fluxo alternativo obrigatório para este caso."
    exc_flow_str = "<br>".join(uc['exc_flows']) if uc['exc_flows'] else "Nenhuma validação de exceção."
    
    content = f'''# Especificação de Caso de Uso: {uc['name']}

Esta especificação segue a metodologia de tabelas formais completas (Elicitação de Funcionalidades baseada no Diagrama e Documento Base de Requisitos).

| Parâmetro de Especificação | Descrição |
| :--- | :--- |
| **Identificador** | {uc['id']} - {uc['name']} |
| **Objetivo do Sistema** | {uc['desc']} |
| **Requisito Associado** | {uc['code']} |
| **Atores Envolvidos** | {actor_str} |
| **O que o usuário vê (Elementos de Interface)** | {uc['data_seen']} |
| **O que o usuário insere (Dados Fornecidos)** | {uc['data_input']} |
| **Condição de Entrada** | {uc['pre']} |
| **Fluxo Principal (Passo a Passo)** | {main_flow_str} |
| **Fluxos Alternativos / Desvios** | {alt_flow_str} |
| **Fluxos de Exceção (Erros e Limites)** | {exc_flow_str} |

<br>
<div align="center">
  <a href="analise_casos_de_uso.md">⬅ Retornar para o Painel Geral do Diagrama de Casos de Uso</a>
</div>
'''
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("SUCESSO: Os 25 arquivos .md foram gerados com 2 novas colunas explicitly respondendo as questoes da banca.")
