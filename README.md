# ARGOS Band

## Monitoramento Energético e Operacional para Missões Espaciais Sustentáveis

O **ARGOS Band** é uma solução computacional desenvolvida para a Global Solution 2026.

O projeto simula um bracelete inteligente utilizado por um astronauta em uma missão espacial experimental. A proposta é monitorar dados operacionais da missão, interpretar situações críticas e apoiar decisões automáticas relacionadas à segurança, eficiência energética e sustentabilidade.

---

## Objetivo do projeto

O objetivo do ARGOS Band é simular um sistema inteligente de monitoramento capaz de receber, interpretar e exibir dados da missão espacial, incluindo:

- Temperatura da nave ou do traje
- Energia disponível da missão
- Comunicação com a base
- Status dos módulos operacionais

A partir desses dados, o sistema gera alertas automáticos, calcula um índice de criticidade e recomenda ações básicas em situações de risco.

---

## Contexto da solução

Em uma missão espacial, o uso eficiente da energia é essencial para manter os sistemas funcionando com segurança. Caso a energia fique baixa, a comunicação falhe ou a temperatura ultrapasse limites seguros, o sistema precisa identificar rapidamente o problema e orientar uma resposta operacional.

O ARGOS Band representa esse cenário por meio de uma aplicação em Python executada no terminal. A tela do terminal simula a interface do bracelete ou dispositivo de apoio ao astronauta.

---

## Funcionalidades implementadas

O sistema possui as seguintes funcionalidades:

- Registro manual de dados da missão
- Simulação automática de sensores
- Simulação contínua de múltiplas leituras
- Análise automática da situação operacional
- Geração de alertas
- Classificação do status da missão
- Avaliação do status dos módulos
- Histórico de leituras
- Relatório resumido da missão
- Exportação do histórico em CSV
- IA simulada por perguntas e respostas
- Modo descritivo com recomendações operacionais

---

## Dados monitorados

### Temperatura

Representa a temperatura da nave ou do traje espacial.

Regra principal:

```text
Temperatura acima de 80 °C → Alerta de superaquecimento
```

### Energia disponível

Representa o nível de energia disponível para a missão.

Regra principal:

```text
Energia abaixo de 20% → Energia crítica. Modo economia ativado
```

### Comunicação

Representa a conexão entre o astronauta e a base de controle.

Regra principal:

```text
Comunicação = 0 → Falha de comunicação
Comunicação = 1 → Comunicação ativa
```

### Status dos módulos

O sistema avalia três módulos principais:

- Módulo térmico
- Módulo energético
- Módulo de comunicação

Cada módulo pode ser classificado como operacional, crítico, em economia ou com falha.

---

## Regras de análise

O ARGOS Band utiliza regras condicionais para interpretar as leituras da missão.

| Condição            | Alerta gerado                          | Impacto na criticidade |
| ------------------- | -------------------------------------- | ---------------------- |
| Temperatura > 80 °C | Alerta de superaquecimento             | +40                    |
| Energia < 20%       | Energia crítica. Modo economia ativado | +35                    |
| Comunicação = 0     | Falha de comunicação                   | +25                    |

Com base na criticidade total, o sistema define o status da missão:

| Criticidade | Status  |
| ----------- | ------- |
| 0           | NORMAL  |
| 1 a 59      | ATENÇÃO |
| 60 ou mais  | CRÍTICO |

---

## Tomada de decisão automática

Além de identificar problemas, o sistema também recomenda ações automáticas.

Exemplos:

- Se a energia estiver baixa, o sistema recomenda manter o modo de economia ativado.
- Se houver superaquecimento, o sistema recomenda priorizar o controle térmico.
- Se a comunicação falhar, o sistema recomenda restabelecer o sinal com a base.
- Se o status estiver crítico, o sistema recomenda priorizar energia, controle térmico e comunicação.

Essas decisões simulam uma resposta operacional básica diante de situações críticas em uma missão espacial.

---

## IA ARGOS

O sistema possui uma IA simulada chamada **ARGOS**, que responde perguntas feitas pelo usuário no terminal.

Exemplos de perguntas:

```text
Como está a missão?
Qual a temperatura?
Qual a energia?
Tem comunicação?
Status dos módulos?
Qual a distância?
```

A ARGOS responde com base na última leitura registrada ou simulada.

---

## Estrutura do projeto

```text
├── argos_band.py
├── README.md
└── historico_argos_band.csv
```

O arquivo `historico_argos_band.csv` é gerado automaticamente quando o usuário escolhe a opção de exportação no menu.

---

## Relação com sustentabilidade

O projeto se relaciona com sustentabilidade ao propor uma solução de uso inteligente da energia em uma missão espacial experimental.

Quando a energia disponível está baixa, o ARGOS Band ativa o modo de economia e recomenda a priorização dos sistemas essenciais. Isso representa uma estratégia de redução de desperdício energético e melhor aproveitamento dos recursos disponíveis.

---

## Tecnologias utilizadas

- Python
- Terminal como interface simulada
- Módulo `random` para simulação de sensores
- Módulo `datetime` para registro de horário
- Módulo `csv` para exportação do histórico
- Estruturas condicionais
- Laços de repetição
- Funções
- Listas e dicionários

---

## Integrantes

```text
Temitope Kuku da Silva Ogunbanjo · 573772
Gabrieli de Lima Pettena de Oliveira · 569799

```
