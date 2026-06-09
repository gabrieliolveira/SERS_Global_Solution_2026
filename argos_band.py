"""
GS2026.1 - Programacao Aplicada ao Monitoramento de Missao Espacial
Projeto: ARGOS Band - Bracelete de IA para apoio a uma missao espacial sustentavel

Contexto do projeto:
Este programa simula um bracelete de IA usado por um astronauta em uma missao
espacial experimental. Como o sistema nao esta rodando em um dispositivo fisico,
a tela do bracelete/celular foi representada no terminal. A IA ARGOS interpreta
os dados da missao e responde perguntas do usuario por texto, simulando um comando
de voz.

Requisitos atendidos:
- Simulacao de temperatura, energia disponivel e comunicacao;
- Monitoramento do status dos modulos da missao;
- Verificacao automatica de superaquecimento, energia critica e falha de comunicacao;
- Tomada de decisao basica com recomendacoes operacionais;
- Menu interativo com repeticao;
- Uso de condicionais, lacos de repeticao, listas/vetores, dicionarios e funcoes;
- Historico das leituras;
- Relatorio resumido;
- Exportacao do historico em CSV;
- Organizacao das informacoes no terminal.

Diferenciais:
- Tema adaptado para um bracelete de IA sem fugir do enunciado;
- IA simulada que responde perguntas sobre status, temperatura, energia,
  comunicacao, tempo e distancia;
- Modo descritivo com recomendacoes para eficiencia energetica e seguranca;
- Indice de criticidade para classificar o risco operacional;
- Status dos modulos: termico, energetico e comunicacao.
"""

from datetime import datetime
import csv
import random
import time


# Limites principais do monitoramento
LIMITE_TEMPERATURA = 80
LIMITE_ENERGIA = 20
ARQUIVO_CSV = "historico_argos_band.csv"

# Cores para organizar a exibicao no terminal
CIANO = "\033[38;5;51m"
VERDE = "\033[38;5;46m"
AMARELO = "\033[38;5;220m"
VERMELHO = "\033[38;5;196m"
NEGRITO = "\033[1m"
FIM = "\033[0m"


def cabecalho(titulo):
    print(f"\n{CIANO}{'=' * 64}{FIM}")
    print(f"{NEGRITO}{titulo.center(64)}{FIM}")
    print(f"{CIANO}{'=' * 64}{FIM}")


def pausar():
    input("\nPressione ENTER para voltar ao bracelete...")


def tela_bracelete(mensagem):
    print(f"\n{CIANO}+{'-' * 42}+{FIM}")
    print(f"{CIANO}|{FIM} {'ARGOS BAND'.center(40)} {CIANO}|{FIM}")
    print(f"{CIANO}|{FIM} {'Assistente de Missao Espacial'.center(40)} {CIANO}|{FIM}")
    print(f"{CIANO}+{'-' * 42}+{FIM}")
    print(f"{mensagem}")


def ler_float(mensagem, minimo=None, maximo=None):
    while True:
        entrada = input(mensagem).replace(",", ".").strip()

        if entrada.replace(".", "").isdigit():
            valor = float(entrada)

            if minimo is not None and valor < minimo:
                print(f"{AMARELO}Valor invalido. Digite um numero maior ou igual a {minimo}.{FIM}")

            elif maximo is not None and valor > maximo:
                print(f"{AMARELO}Valor invalido. Digite um numero menor ou igual a {maximo}.{FIM}")

            else:
                return valor

        else:
            print(f"{VERMELHO}Entrada invalida. Digite apenas numeros.{FIM}")


def ler_comunicacao():
    while True:
        valor = input("Comunicacao com a base (1 = ativa, 0 = falha): ").strip()

        if valor == "0" or valor == "1":
            return int(valor)

        print(f"{AMARELO}Entrada invalida. Digite 1 para ativa ou 0 para falha.{FIM}")


def texto_comunicacao(comunicacao):
    if comunicacao == 1:
        return "Ativa"

    return "Falha"


def avaliar_modulos(temperatura, energia, comunicacao):
    """Avalia o status dos principais modulos operacionais da missao."""
    modulos = {}

    if temperatura > LIMITE_TEMPERATURA:
        modulos["Modulo termico"] = "CRITICO"
    else:
        modulos["Modulo termico"] = "OPERACIONAL"

    if energia < LIMITE_ENERGIA:
        modulos["Modulo energetico"] = "ECONOMIA"
    else:
        modulos["Modulo energetico"] = "OPERACIONAL"

    if comunicacao == 0:
        modulos["Modulo de comunicacao"] = "FALHA"
    else:
        modulos["Modulo de comunicacao"] = "OPERACIONAL"

    return modulos


def analisar_leitura(temperatura, energia, comunicacao):
    """Analisa as regras principais e devolve alertas, status e criticidade."""
    alertas = []
    criticidade = 0

    if temperatura > LIMITE_TEMPERATURA:
        alertas.append("Alerta de superaquecimento")
        criticidade += 40

    if energia < LIMITE_ENERGIA:
        alertas.append("Energia critica. Modo economia ativado")
        criticidade += 35

    if comunicacao == 0:
        alertas.append("Falha de comunicacao")
        criticidade += 25

    if criticidade == 0:
        status = "NORMAL"
    elif criticidade < 60:
        status = "ATENCAO"
    else:
        status = "CRITICO"

    return alertas, status, criticidade


def cor_status(status):
    if status == "NORMAL":
        return VERDE

    if status == "ATENCAO":
        return AMARELO

    return VERMELHO


def gerar_contexto_missao(historico):
    """
    Gera informacoes descritivas para o bracelete.
    Elas nao substituem os requisitos principais, apenas ajudam a IA simulada
    a responder como um dispositivo inteligente.
    """
    numero_leitura = len(historico) + 1
    tempo_missao = numero_leitura * 5
    distancia_base = 120 + (numero_leitura * 18.5)

    return tempo_missao, distancia_base


def criar_leitura(temperatura, energia, comunicacao, historico):
    alertas, status, criticidade = analisar_leitura(temperatura, energia, comunicacao)
    tempo_missao, distancia_base = gerar_contexto_missao(historico)
    modulos = avaliar_modulos(temperatura, energia, comunicacao)

    leitura = {
        "id": len(historico) + 1,
        "hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "temperatura": temperatura,
        "energia": energia,
        "comunicacao": comunicacao,
        "status": status,
        "criticidade": criticidade,
        "alertas": alertas,
        "tempo_missao": tempo_missao,
        "distancia_base": distancia_base,
        "modulos": modulos,
    }

    historico.append(leitura)
    return leitura


def exibir_status_modulos(leitura):
    print("\nStatus dos modulos da missao:")

    for nome_modulo, status_modulo in leitura["modulos"].items():
        print(f"  {nome_modulo}: {status_modulo}")


def exibir_leitura(leitura, modo_descritivo=False):
    cor = cor_status(leitura["status"])

    print(f"\nLeitura #{leitura['id']} - {leitura['hora']}")
    print(f"Temperatura do traje/nave: {leitura['temperatura']:.1f} C")
    print(f"Energia disponivel da missao: {leitura['energia']:.1f}%")
    print(f"Comunicacao com a base: {texto_comunicacao(leitura['comunicacao'])}")
    print(f"Status operacional: {cor}{leitura['status']}{FIM}")
    print(f"Indice de criticidade: {leitura['criticidade']}%")

    exibir_status_modulos(leitura)

    if modo_descritivo:
        print(f"\nTempo estimado de missao: {leitura['tempo_missao']} minutos")
        print(f"Distancia estimada da base: {leitura['distancia_base']:.1f} km")

    if len(leitura["alertas"]) > 0:
        print(f"\n{VERMELHO}Alertas identificados pela ARGOS:{FIM}")

        for alerta in leitura["alertas"]:
            print(f"  * {alerta}")
    else:
        print(f"\n{VERDE}ARGOS: Nenhum alerta identificado no momento.{FIM}")

    if modo_descritivo:
        explicar_recomendacao(leitura)


def explicar_recomendacao(leitura):
    print(f"\n{CIANO}Modo descritivo da ARGOS:{FIM}")

    if leitura["status"] == "NORMAL":
        print("A missao esta estavel. A recomendacao e manter o monitoramento periodico e o uso eficiente da energia.")

    elif leitura["status"] == "ATENCAO":
        print("Existe pelo menos uma variavel fora do ideal. A recomendacao e reduzir o consumo dos sistemas nao essenciais.")

    else:
        print("A missao esta em estado critico. A recomendacao e priorizar energia, controle termico e comunicacao com a base.")


def inserir_dados(historico, modo_descritivo):
    cabecalho("REGISTRAR DADOS DO TRAJE")
    tela_bracelete("Entrada manual de sensores do bracelete.")

    temperatura = ler_float("Temperatura da nave/traje em C: ")
    energia = ler_float("Energia disponivel da missao em %: ", minimo=0, maximo=100)
    comunicacao = ler_comunicacao()

    leitura = criar_leitura(temperatura, energia, comunicacao, historico)

    print(f"\n{VERDE}Dados registrados com sucesso pela ARGOS.{FIM}")
    exibir_leitura(leitura, modo_descritivo)
    pausar()


def simular_sensor():
    temperatura = round(random.uniform(25, 75), 1)
    energia = round(random.uniform(35, 100), 1)

    # Comunicacao ativa aparece mais vezes para simular uma missao geralmente estavel
    comunicacao = random.choice([1, 1, 1, 1, 0])

    return temperatura, energia, comunicacao


def simular_uma_leitura(historico, modo_descritivo):
    cabecalho("SIMULAR SENSORES DO BRACELETE")
    tela_bracelete("ARGOS esta coletando dados simulados dos sensores.")

    print("Coletando dados", end="")

    for contador in range(3):
        time.sleep(0.25)
        print(".", end="", flush=True)

    print()

    temperatura, energia, comunicacao = simular_sensor()
    leitura = criar_leitura(temperatura, energia, comunicacao, historico)

    exibir_leitura(leitura, modo_descritivo)
    pausar()


def simulacao_continua(historico, modo_descritivo):
    cabecalho("SIMULACAO CONTINUA")

    quantidade = int(ler_float("Quantas leituras deseja simular? ", minimo=1, maximo=20))
    intervalo = ler_float("Intervalo entre leituras em segundos (0 a 3): ", minimo=0, maximo=3)

    for contador in range(quantidade):
        print(f"\nColeta automatica {contador + 1} de {quantidade}")
        temperatura, energia, comunicacao = simular_sensor()
        leitura = criar_leitura(temperatura, energia, comunicacao, historico)
        exibir_leitura(leitura, modo_descritivo)
        time.sleep(intervalo)

    print(f"\n{VERDE}Simulacao finalizada. {quantidade} leitura(s) registrada(s).{FIM}")
    pausar()


def visualizar_status(historico, modo_descritivo):
    cabecalho("STATUS ATUAL DA MISSAO")

    if len(historico) == 0:
        print("Nenhuma leitura registrada ainda.")
    else:
        exibir_leitura(historico[-1], modo_descritivo)

    pausar()


def executar_analise(historico, modo_descritivo):
    cabecalho("ANALISE AUTOMATICA DA ARGOS")

    if len(historico) == 0:
        print("Nenhuma leitura registrada. Insira ou simule dados primeiro.")
    else:
        ultima_leitura = historico[-1]
        print("ARGOS esta analisando a ultima leitura registrada...")
        time.sleep(0.5)
        exibir_leitura(ultima_leitura, modo_descritivo)

    pausar()


def responder_pergunta(pergunta, historico, modo_descritivo):
    if len(historico) == 0:
        return "ARGOS: Ainda nao existe leitura registrada. Registre ou simule sensores primeiro."

    leitura = historico[-1]
    texto = pergunta.lower()
    if "modulo" in texto or "módulo" in texto or "modulos" in texto or "módulos" in texto:
        resposta = "ARGOS: Status dos modulos: "
        resposta += ", ".join(
            f"{nome} = {status}" for nome, status in leitura["modulos"].items()
        )
        resposta += "."

    elif "status" in texto or "missao" in texto or "missão" in texto or "risco" in texto:
        resposta = f"ARGOS: O status atual da missao e {leitura['status']} com criticidade de {leitura['criticidade']}%."
    elif "temperatura" in texto or "calor" in texto or "superaquecimento" in texto:
        resposta = f"ARGOS: A temperatura atual e {leitura['temperatura']:.1f} C."
        if leitura["temperatura"] > LIMITE_TEMPERATURA:
            resposta += " Existe risco de superaquecimento."

    elif "energia" in texto or "combustivel" in texto or "bateria" in texto:
        resposta = f"ARGOS: A energia disponivel da missao esta em {leitura['energia']:.1f}%."
        if leitura["energia"] < LIMITE_ENERGIA:
            resposta += " Recomendo manter o modo de economia de energia ativado."

    elif "comunicacao" in texto or "comunicação" in texto or "sinal" in texto or "base" in texto:
        resposta = f"ARGOS: A comunicacao com a base esta {texto_comunicacao(leitura['comunicacao']).lower()}."
        if leitura["comunicacao"] == 0:
            resposta += " Tente restabelecer o sinal antes de executar novas manobras."

    elif "tempo" in texto:
        resposta = f"ARGOS: O tempo estimado de missao e de {leitura['tempo_missao']} minutos."

    elif "distancia" in texto or "distância" in texto:
        resposta = f"ARGOS: A distancia estimada da base e de {leitura['distancia_base']:.1f} km."

    elif "ajuda" in texto or "opcoes" in texto or "opções" in texto:
        resposta = "ARGOS: Voce pode perguntar sobre status, temperatura, energia, comunicacao, modulos, tempo ou distancia."

    else:
        resposta = "ARGOS: Nao reconheci a pergunta. Tente perguntar sobre status, temperatura, energia, comunicacao, modulos, tempo ou distancia."

    if modo_descritivo:
        resposta += " Modo descritivo ativo: consulte a analise automatica para ver recomendacoes completas."

    return resposta


def conversar_com_argos(historico, modo_descritivo):
    cabecalho("CONVERSAR COM A IA ARGOS")
    tela_bracelete("Digite como se estivesse falando por voz com o bracelete.")
    print("Exemplos: 'como esta a missao?', 'qual a energia?', 'tem comunicacao?', 'status dos modulos?'")
    print("Digite 'sair' para voltar ao menu.\n")

    while True:
        pergunta = input("Voce: ").strip()

        if pergunta.lower() == "sair":
            break

        resposta = responder_pergunta(pergunta, historico, modo_descritivo)
        print(resposta)


def alternar_modo_descritivo(modo_descritivo):
    cabecalho("MODO DESCRITIVO")

    if modo_descritivo:
        modo_descritivo = False
        print(f"{AMARELO}Modo descritivo desativado.{FIM}")
    else:
        modo_descritivo = True
        print(f"{VERDE}Modo descritivo ativado.{FIM}")
        print("A ARGOS passara a mostrar energia, distancia estimada, tempo de missao, modulos e recomendacoes.")

    pausar()
    return modo_descritivo


def mostrar_historico(historico):
    cabecalho("HISTORICO DAS LEITURAS")

    if len(historico) == 0:
        print("Nenhuma leitura foi registrada.")
    else:
        for leitura in historico:
            status_formatado = f"{cor_status(leitura['status'])}{leitura['status']}{FIM}"

            print(
                f"#{leitura['id']:02d} | {leitura['hora']} | "
                f"Temp: {leitura['temperatura']:5.1f} C | "
                f"Energia: {leitura['energia']:5.1f}% | "
                f"Comunicacao: {texto_comunicacao(leitura['comunicacao']):5s} | "
                f"Status: {status_formatado}"
            )

    pausar()


def relatorio_resumido(historico):
    cabecalho("RELATORIO RESUMIDO DA MISSAO")

    if len(historico) == 0:
        print("Nao ha dados suficientes para gerar o relatorio.")
        pausar()
        return

    total = len(historico)
    temperatura_media = sum(leitura["temperatura"] for leitura in historico) / total
    energia_media = sum(leitura["energia"] for leitura in historico) / total
    falhas_comunicacao = sum(1 for leitura in historico if leitura["comunicacao"] == 0)
    leituras_criticas = sum(1 for leitura in historico if leitura["status"] == "CRITICO")
    modulos_em_falha = sum(
        1
        for leitura in historico
        for status_modulo in leitura["modulos"].values()
        if status_modulo in ["CRITICO", "ECONOMIA", "FALHA"]
    )
    maior_criticidade = max(historico, key=lambda leitura: leitura["criticidade"])

    print(f"Total de leituras: {total}")
    print(f"Temperatura media: {temperatura_media:.1f} C")
    print(f"Energia media: {energia_media:.1f}%")
    print(f"Falhas de comunicacao: {falhas_comunicacao}")
    print(f"Leituras criticas: {leituras_criticas}")
    print(f"Ocorrencias em modulos nao operacionais: {modulos_em_falha}")

    print("\nLeitura de maior risco:")
    exibir_leitura(maior_criticidade, True)

    pausar()


def exportar_csv(historico):
    cabecalho("EXPORTAR HISTORICO")

    if len(historico) == 0:
        print("Nao ha historico para exportar.")
        pausar()
        return

    with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as arquivo:
        campos = [
            "id",
            "hora",
            "temperatura",
            "energia",
            "comunicacao",
            "status",
            "criticidade",
            "tempo_missao",
            "distancia_base",
            "modulo_termico",
            "modulo_energetico",
            "modulo_comunicacao",
            "alertas",
        ]

        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()

        for leitura in historico:
            linha = leitura.copy()

            linha["modulo_termico"] = leitura["modulos"]["Modulo termico"]
            linha["modulo_energetico"] = leitura["modulos"]["Modulo energetico"]
            linha["modulo_comunicacao"] = leitura["modulos"]["Modulo de comunicacao"]

            linha.pop("modulos", None)

            if len(leitura["alertas"]) > 0:
                linha["alertas"] = "; ".join(leitura["alertas"])
            else:
                linha["alertas"] = "Sem alertas"

            escritor.writerow(linha)

    print(f"{VERDE}Historico exportado para o arquivo: {ARQUIVO_CSV}{FIM}")
    pausar()


def exibir_menu(modo_descritivo):
    cabecalho("ARGOS BAND - BRACELETE DE IA")

    if modo_descritivo:
        estado_modo = "ATIVADO"
    else:
        estado_modo = "DESATIVADO"

    print(f"Modo descritivo: {estado_modo}")
    print("1 - Registrar dados do traje")
    print("2 - Simular sensores do bracelete")
    print("3 - Visualizar status atual")
    print("4 - Executar analise automatica")
    print("5 - Conversar com a IA ARGOS")
    print("6 - Ativar/desativar modo descritivo")
    print("7 - Historico das leituras")
    print("8 - Simulacao continua dos sensores")
    print("9 - Relatorio resumido da missao")
    print("10 - Exportar historico em CSV")
    print("0 - Desligar bracelete")


def main():
    historico = []
    modo_descritivo = False

    while True:
        exibir_menu(modo_descritivo)
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            inserir_dados(historico, modo_descritivo)

        elif opcao == "2":
            simular_uma_leitura(historico, modo_descritivo)

        elif opcao == "3":
            visualizar_status(historico, modo_descritivo)

        elif opcao == "4":
            executar_analise(historico, modo_descritivo)

        elif opcao == "5":
            conversar_com_argos(historico, modo_descritivo)

        elif opcao == "6":
            modo_descritivo = alternar_modo_descritivo(modo_descritivo)

        elif opcao == "7":
            mostrar_historico(historico)

        elif opcao == "8":
            simulacao_continua(historico, modo_descritivo)

        elif opcao == "9":
            relatorio_resumido(historico)

        elif opcao == "10":
            exportar_csv(historico)

        elif opcao == "0":
            print(f"\n{CIANO}Bracelete desligado. Missao finalizada com seguranca.{FIM}")
            break

        else:
            print(f"\n{AMARELO}Opcao invalida. Tente novamente.{FIM}")
            time.sleep(0.8)


if __name__ == "__main__":
    main()
