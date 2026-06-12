# Análise de Casos de Uso - Paraíba Social (SEDH)

Este documento contém o diagrama geral de casos de uso do sistema Paraíba Social.

## Diagrama Geral

```plantuml
@startuml
title Diagrama Geral de Casos de Uso — Paraíba Social (SEDH)

left to right direction
skinparam packageStyle rectangle
skinparam linetype polyline
skinparam nodesep 60
skinparam ranksep 90

' Atores Primários
actor "Cidadão" as Cidadao
actor "Servidor / Gestor" as Servidor
actor "Assistente Social" as Assistente
actor "Administrador" as Admin

Assistente -up-|> Servidor

rectangle "Sistema Paraíba Social" {

  package "Acesso e Segurança" {
    usecase "UC1: Realizar login" as UC1
    usecase "UC2: Controlar acesso" as UC2
    usecase "UC3: Validar CPF" as UC3
  }

  package "Área do Cidadão" {
    usecase "UC19: Acessar info sobre programas" as UC19
    usecase "UC15: Apresentar eixos da SEDH" as UC15
    usecase "UC20: Inscrever-se em programa" as UC20
    usecase "UC21: Solicitar suporte/melhoria" as UC21
  }

  package "Painel de Indicadores" {
    usecase "UC4: Visualizar painel" as UC4
    usecase "UC5: Filtrar dados" as UC5
    usecase "UC6: Visualizar gráficos" as UC6
    usecase "UC7: Identificar padrões" as UC7
    usecase "UC8: Consolidar dados" as UC8
  }

  package "Programas Sociais" {
    usecase "UC9: Acompanhar execução" as UC9
    usecase "UC10: Visualizar página do programa" as UC10
    usecase "UC11: Visualizar mapa" as UC11
    usecase "UC12: Visualizar dados por perfil" as UC12
    usecase "UC13: Visualizar rankings" as UC13
    usecase "UC14: Avaliar inscrições" as UC14
  }

  package "Relatórios" {
    usecase "UC16: Gerar relatório automático" as UC16
    usecase "UC17: Personalizar relatório" as UC17
    usecase "UC18: Emitir relatório em PDF" as UC18
  }

  package "Administração & Plataforma" {
    usecase "UC22: Gerenciar usuários" as UC22
    usecase "UC23: Configurar ajustes" as UC23
    usecase "UC24: Instalar app móvel" as UC24
    usecase "UC25: Sincronizar com Sheets" as UC25
  }
}

' Atores Externos
actor "Clerk (Auth)" as Clerk <<system>>
actor "Google Sheets" as Sheets <<system>>

' Relacionamentos Diretos (Atores)
Cidadao --> UC1
Cidadao --> UC19
Cidadao --> UC20
Cidadao --> UC21
Cidadao --> UC15
Cidadao --> UC24

' Ajuste de limpeza visual: Servidor acessa as funcionalidades principais. 
' As funcionalidades secundárias já são atingidas via <<include>>
Servidor --> UC4
Servidor --> UC9
Servidor --> UC16
Servidor --> UC24

Assistente --> UC14

Admin --> UC1
Admin --> UC22
Admin --> UC23

' Relacionamentos com Sistemas Externos
UC1 -down-> Clerk
UC2 -down-> Clerk
UC25 -down-> Sheets

' Relacionamentos <<include>>
UC4 ..> UC1 : <<include>>
UC4 ..> UC2 : <<include>>
UC4 ..> UC5 : <<include>>
UC4 ..> UC6 : <<include>>
UC4 ..> UC7 : <<include>>
UC4 ..> UC8 : <<include>>
UC4 ..> UC25 : <<include>>

UC22 ..> UC2 : <<include>>

UC9 ..> UC10 : <<include>>
UC16 ..> UC9 : <<include>>

UC20 ..> UC1 : <<include>>
UC20 ..> UC3 : <<include>>

UC19 ..> UC1 : <<include>>

' Relacionamentos <<extend>>
' A seta sempre aponta da funcionalidade opcional para a funcionalidade base
UC17 ..> UC16 : <<extend>>
UC18 ..> UC16 : <<extend>>

UC11 ..> UC10 : <<extend>>
UC12 ..> UC10 : <<extend>>
UC13 ..> UC10 : <<extend>>

UC21 ..> UC19 : <<extend>>
UC15 ..> UC19 : <<extend>>

@enduml
```

> **Nota:** As especificações textuais detalhadas (ou histórias de usuário) de cada um dos casos de uso representados neste diagrama podem ser encontradas nos demais arquivos markdown desta pasta.
