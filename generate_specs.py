import os
import re

use_cases = [
    {"id": "UC1", "code": "RF001", "name": "Realizar login", "actors": ["Cidadão", "Servidor", "Admin"], "desc": "Permitir que usuários realizem login para acessar as áreas internas da plataforma, especialmente dashboards, relatórios, gestão e módulos administrativos."},
    {"id": "UC2", "code": "RF002", "name": "Controlar acesso por perfil e permissao", "actors": ["Admin", "Sistema"], "desc": "Controlar o acesso dos usuários conforme sessões, perfis e permissões, impedindo que usuários não autorizados acessem funcionalidades restritas."},
    {"id": "UC3", "code": "RF025", "name": "Validar CPF como identificador unico", "actors": ["Admin", "Sistema"], "desc": "Utilizar o Cadastro de Pessoa Física (CPF) como identificador único, realizando a checagem de dados para garantir que um cidadão não receba o mesmo benefício social duas vezes por caminhos diferentes."},
    {"id": "UC4", "code": "RF003", "name": "Visualizar painel de indicadores", "actors": ["Servidor"], "desc": "Apresentar um painel principal com indicadores demográficos, sociais e econômicos consolidados, permitindo uma visão estratégica dos dados da SEDH."},
    {"id": "UC5", "code": "RF004", "name": "Filtrar dados por municipio e regional", "actors": ["Servidor"], "desc": "Permitir filtrar os dados por município e por regional, possibilitando análises territorializadas dos indicadores sociais."},
    {"id": "UC6", "code": "RF005", "name": "Visualizar graficos e tendencias", "actors": ["Servidor"], "desc": "Exibir gráficos para facilitar a interpretação dos dados, incluindo comparações, tendências e variações ao longo do tempo."},
    {"id": "UC7", "code": "RF006", "name": "Identificar padroes e tendencias", "actors": ["Servidor"], "desc": "Permitir identificar padrões, tendências e mudanças nos indicadores sociais, como evolução populacional e variações territoriais."},
    {"id": "UC8", "code": "RF007", "name": "Consolidar dados de multiplos programas", "actors": ["Servidor"], "desc": "Reunir dados de diferentes programas, setores e bases da SEDH em uma plataforma única e organizada."},
    {"id": "UC9", "code": "RF008", "name": "Acompanhar execucao dos programas", "actors": ["Servidor"], "desc": "Permitir o acompanhamento dos programas sociais executados pela SEDH, incluindo informações sobre beneficiários, execução das políticas e dados territoriais."},
    {"id": "UC10", "code": "RF009", "name": "Visualizar pagina do programa", "actors": ["Servidor"], "desc": "Disponibilizar páginas individuais para cada programa social, contendo dados quantitativos, informações descritivas, gráficos, rankings e análises próprias."},
    {"id": "UC11", "code": "RF013", "name": "Visualizar mapa de programas", "actors": ["Servidor"], "desc": "Disponibilizar mapas para visualizar a distribuição dos programas sociais no território paraibano."},
    {"id": "UC12", "code": "RF014", "name": "Visualizar dados por territorio e perfil", "actors": ["Servidor"], "desc": "Permitir a visualização dos dados por município, região e perfil socioeconômico, apoiando decisões baseadas no território."},
    {"id": "UC13", "code": "RF015", "name": "Visualizar rankings comparativos", "actors": ["Servidor"], "desc": "Apresentar rankings e painéis comparativos para apoiar a leitura dos dados por programa, município ou regional."},
    {"id": "UC14", "code": "RF016", "name": "Avaliar inscricoes em programas", "actors": ["Assistente Social"], "desc": "Possuir funcionalidades relacionadas à avaliação de inscrições em programas ou iniciativas da SEDH."},
    {"id": "UC15", "code": "RF022", "name": "Apresentar eixos de atuacao da SEDH", "actors": ["Cidadão"], "desc": "Apresentar os principais eixos de atuação da SEDH, como Segurança Alimentar, Assistência Social, Direitos Humanos, Trabalho e Renda e Economia Solidária."},
    {"id": "UC16", "code": "RF010", "name": "Gerar relatorio automaticamente", "actors": ["Servidor"], "desc": "Gerar relatórios automaticamente, substituindo processos manuais de consolidação e análise de dados."},
    {"id": "UC17", "code": "RF011", "name": "Personalizar relatorio", "actors": ["Servidor"], "desc": "Permitir que o usuário personalize relatórios escolhendo formato completo ou resumido, orientação da página, programas e subseções a serem incluídas."},
    {"id": "UC18", "code": "RF012", "name": "Emitir relatorio em PDF", "actors": ["Servidor"], "desc": "Permitir a emissão de relatórios em PDF de forma rápida, com base nos filtros e configurações escolhidos pelo usuário."},
    {"id": "UC19", "code": "RF020", "name": "Acessar informacoes sobre programas", "actors": ["Cidadão"], "desc": "Permitir que cidadãos acessem informações sobre programas sociais, ações desenvolvidas e formas de participação."},
    {"id": "UC20", "code": "RF021", "name": "Inscrever-se em programa social", "actors": ["Cidadão"], "desc": "Permitir, na área destinada ao cidadão, a realização de inscrições para participação em iniciativas ofertadas pela SEDH."},
    {"id": "UC21", "code": "RF019", "name": "Solicitar suporte ou melhoria", "actors": ["Cidadão"], "desc": "Permitir que usuários solicitem suporte técnico, inclusão de dados ou sugiram melhorias na plataforma."},
    {"id": "UC22", "code": "RF017", "name": "Gerenciar usuarios do sistema", "actors": ["Administrador"], "desc": "Permitir a gestão de usuários, incluindo cadastro, edição, controle de acesso e configuração de permissões."},
    {"id": "UC23", "code": "RF018", "name": "Configurar ajustes administrativos", "actors": ["Administrador"], "desc": "Possuir páginas ou módulos de configuração para ajustes administrativos da plataforma."},
    {"id": "UC24", "code": "RF023", "name": "Instalar como aplicativo movel", "actors": ["Cidadão", "Servidor"], "desc": "Permitir instalação em dispositivos móveis, abrindo como aplicativo a partir do navegador."},
    {"id": "UC25", "code": "RF024", "name": "Sincronizar dados com Google Sheets", "actors": ["Sistema"], "desc": "Recuperar e armazenar dados por meio de integração com a API do Google Sheets enquanto essa for a camada de dados adotada."}
]

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

for uc in use_cases:
    slug = slugify(uc['name'])
    filename = f"especificacao_{slug}.md"
    filepath = os.path.join(base_dir, filename)
    
    actor_str = ", ".join(uc['actors'])
    
    content = f'''# Especificação de Caso de Uso: {uc['name']}

Esta especificação segue o formato tabular estruturado.

| Campo | Descrição |
| :--- | :--- |
| **Caso de Uso** | {uc['id']} - {uc['name']} |
| **Objetivo** | {uc['desc']} |
| **Requisitos Relacionados** | {uc['code']} |
| **Atores** | {actor_str} |
| **Condição de Entrada** | O usuário ({uc['actors'][0]}) acessa a interface correspondente à funcionalidade. |
| **Fluxo Principal** | 1. O ator inicia a funcionalidade.<br>2. O sistema apresenta a interface e solicita os dados necessários.<br>3. O ator insere as informações.<br>4. O sistema valida e processa a ação.<br>5. O sistema retorna uma mensagem de sucesso. |
| **Fluxos Alternativos** | A1. Cancelamento: O ator pode cancelar a ação a qualquer momento antes do processamento, retornando à tela inicial. |
| **Fluxos de Exceção** | E1. Falha de validação ou permissão: O sistema exibe uma mensagem de erro e aborta a operação. |
| **Condição de Saída** | O estado do sistema é atualizado e o objetivo é alcançado com sucesso. |
'''
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Arquivos atualizados com formato de tabela com sucesso.")
