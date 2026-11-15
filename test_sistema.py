# -*- coding: utf-8 -*-


from src.inferencia import recomendar_atividade


# === TEMPO CURTO ===
def test_R01_leitura():
    res = recomendar_atividade({
        "tempo": "curto", "ambiente": "interno", "preferencia": "tranquilidade"
    })
    assert res["conclusao"] == "Leitura"
    assert res["regra"] == "R01"
    print("✅ R01 passou")


def test_R02_filme():
    res = recomendar_atividade({
        "tempo": "curto", "ambiente": "interno", "preferencia": "movimento"
    })
    assert res["conclusao"] == "Filme ou série"
    assert res["regra"] == "R02"
    print("✅ R02 passou")


def test_R03_caminhada_curto_externo_tranquilo():
    res = recomendar_atividade({
        "tempo": "curto", "ambiente": "externo", "preferencia": "tranquilidade"
    })
    assert res["conclusao"] == "Caminhada ao ar livre"
    assert res["regra"] == "R03"
    print("✅ R03 passou")


def test_R04_caminhada_curto_externo_movimento():
    res = recomendar_atividade({
        "tempo": "curto", "ambiente": "externo", "preferencia": "movimento"
    })
    assert res["conclusao"] == "Caminhada ao ar livre"
    assert res["regra"] == "R04"
    print("✅ R04 passou")


def test_R05_conversa_interno_social():
    res = recomendar_atividade({
        "tempo": "curto", "ambiente": "interno", "preferencia": "social"
    })
    assert res["conclusao"] == "Conversa com amigos ou família"
    assert res["regra"] == "R05"
    print("✅ R05 passou")


def test_R06_conversa_parque():
    res = recomendar_atividade({
        "tempo": "curto", "ambiente": "externo", "preferencia": "social"
    })
    assert res["conclusao"] == "Conversa em um parque ou praça"
    assert res["regra"] == "R06"
    print("✅ R06 passou")


def test_R07_musica():
    res = recomendar_atividade({
        "tempo": "curto", "ambiente": "indiferente", "preferencia": "tranquilidade"
    })
    assert res["conclusao"] == "Ouvir música ou podcast relaxante"
    assert res["regra"] == "R07"
    print("✅ R07 passou")


def test_R08_alongamento():
    res = recomendar_atividade({
        "tempo": "curto", "ambiente": "indiferente", "preferencia": "movimento"
    })
    assert res["conclusao"] == "Alongamento ou exercícios leves"
    assert res["regra"] == "R08"
    print("✅ R08 passou")


def test_R09_chamada():
    res = recomendar_atividade({
        "tempo": "curto", "ambiente": "indiferente", "preferencia": "social"
    })
    assert res["conclusao"] == "Mensagem ou chamada com alguém querido"
    assert res["regra"] == "R09"
    print("✅ R09 passou")


# === TEMPO MÉDIO ===
def test_R10_jogo_grupo():
    res = recomendar_atividade({
        "tempo": "medio", "ambiente": "interno", "preferencia": "social"
    })
    assert res["conclusao"] == "Jogo em grupo"
    assert res["regra"] == "R10"
    print("✅ R10 passou")


def test_R11_leitura_medio():
    res = recomendar_atividade({
        "tempo": "medio", "ambiente": "interno", "preferencia": "tranquilidade"
    })
    assert res["conclusao"] == "Leitura"
    assert res["regra"] == "R11"
    print("✅ R11 passou")


def test_R12_caminhada_medio_externo_movimento():
    res = recomendar_atividade({
        "tempo": "medio", "ambiente": "externo", "preferencia": "movimento"
    })
    assert res["conclusao"] == "Caminhada ao ar livre"
    assert res["regra"] == "R12"
    print("✅ R12 passou")


def test_R13_jogo_ao_ar_livre():
    res = recomendar_atividade({
        "tempo": "medio", "ambiente": "externo", "preferencia": "social"
    })
    assert res["conclusao"] == "Jogo em grupo ao ar livre"
    assert res["regra"] == "R13"
    print("✅ R13 passou")


def test_R14_danca():
    res = recomendar_atividade({
        "tempo": "medio", "ambiente": "interno", "preferencia": "movimento"
    })
    assert res["conclusao"] == "Praticar uma dança ou exercício em casa"
    assert res["regra"] == "R14"
    print("✅ R14 passou")


def test_R15_contemplacao():
    res = recomendar_atividade({
        "tempo": "medio", "ambiente": "externo", "preferencia": "tranquilidade"
    })
    assert res["conclusao"] == "Sentar em um local silencioso e observar a natureza"
    assert res["regra"] == "R15"
    print("✅ R15 passou")


def test_R16_diario():
    res = recomendar_atividade({
        "tempo": "medio", "ambiente": "indiferente", "preferencia": "tranquilidade"
    })
    assert res["conclusao"] == "Escutar um álbum completo ou escrever em um diário"
    assert res["regra"] == "R16"
    print("✅ R16 passou")


def test_R17_bicicleta():
    res = recomendar_atividade({
        "tempo": "medio", "ambiente": "indiferente", "preferencia": "movimento"
    })
    assert res["conclusao"] == "Passeio de bicicleta ou caminhada mais longa"
    assert res["regra"] == "R17"
    print("✅ R17 passou")


def test_R18_encontro():
    res = recomendar_atividade({
        "tempo": "medio", "ambiente": "indiferente", "preferencia": "social"
    })
    assert res["conclusao"] == "Encontro casual com amigos"
    assert res["regra"] == "R18"
    print("✅ R18 passou")


# === TEMPO LONGO ===
def test_R19_oficina():
    res = recomendar_atividade({
        "tempo": "longo", "ambiente": "indiferente", "preferencia": "social"
    })
    assert res["conclusao"] == "Oficina criativa"
    assert res["regra"] == "R19"
    print("✅ R19 passou")


def test_R20_livro():
    res = recomendar_atividade({
        "tempo": "longo", "ambiente": "interno", "preferencia": "tranquilidade"
    })
    assert res["conclusao"] == "Leitura de um livro completo"
    assert res["regra"] == "R20"
    print("✅ R20 passou")


def test_R21_caminhada_longo():
    res = recomendar_atividade({
        "tempo": "longo", "ambiente": "externo", "preferencia": "movimento"
    })
    assert res["conclusao"] == "Caminhada ao ar livre"
    assert res["regra"] == "R21"
    print("✅ R21 passou")


def test_R22_cozinhar():
    res = recomendar_atividade({
        "tempo": "longo", "ambiente": "interno", "preferencia": "movimento"
    })
    assert res["conclusao"] == "Cozinhar algo novo ou fazer exercícios completos"
    assert res["regra"] == "R22"
    print("✅ R22 passou")


def test_R23_passeio_contemplativo():
    res = recomendar_atividade({
        "tempo": "longo", "ambiente": "externo", "preferencia": "tranquilidade"
    })
    assert res["conclusao"] == "Visita a um parque, praia ou passeio contemplativo"
    assert res["regra"] == "R23"
    print("✅ R23 passou")


def test_R24_piquenique():
    res = recomendar_atividade({
        "tempo": "longo", "ambiente": "externo", "preferencia": "social"
    })
    assert res["conclusao"] == "Piquenique ou passeio em grupo ao ar livre"
    assert res["regra"] == "R24"
    print("✅ R24 passou")


def test_R25_jantar():
    res = recomendar_atividade({
        "tempo": "longo", "ambiente": "interno", "preferencia": "social"
    })
    assert res["conclusao"] == "Jantar ou jogo longo com familiares/amigos"
    assert res["regra"] == "R25"
    print("✅ R25 passou")


def test_R26_projeto_pessoal():
    res = recomendar_atividade({
        "tempo": "longo", "ambiente": "indiferente", "preferencia": "tranquilidade"
    })
    assert res["conclusao"] == "Projeto pessoal: desenho, escrita ou estudo de algo que goste"
    assert res["regra"] == "R26"
    print("✅ R26 passou")


def test_R27_trilha():
    res = recomendar_atividade({
        "tempo": "longo", "ambiente": "indiferente", "preferencia": "movimento"
    })
    assert res["conclusao"] == "Trilha, passeio esportivo ou visitar um lugar novo"
    assert res["regra"] == "R27"
    print("✅ R27 passou")


# === REGRAS ESPECIAIS ===
def test_R28_dado_faltante():
    res = recomendar_atividade({
        "tempo": "curto", "ambiente": "interno"
    })
    assert res["conclusao"] == "Encaminhar para decisão humana"
    assert res["regra"] == "R28"
    print("✅ R28 passou")


def test_R29_sem_correspondencia():
    res = recomendar_atividade({
        "tempo": "curto", "ambiente": "interno",  "preferencia": "INEXISTENTE"   
    })
    assert res["conclusao"] == "Encaminhar para decisão humana"
    assert res["regra"] == "R29"
    print("✅ R29 passou")


# === EXECUÇÃO DE TODOS OS TESTES ===
if __name__ == "__main__":
    print("=== Executando todos os testes — Lazer Inteligente ===\n")
    testes = [
        test_R01_leitura,
        test_R02_filme,
        test_R03_caminhada_curto_externo_tranquilo,
        test_R04_caminhada_curto_externo_movimento,
        test_R05_conversa_interno_social,
        test_R06_conversa_parque,
        test_R07_musica,
        test_R08_alongamento,
        test_R09_chamada,
        test_R10_jogo_grupo,
        test_R11_leitura_medio,
        test_R12_caminhada_medio_externo_movimento,
        test_R13_jogo_ao_ar_livre,
        test_R14_danca,
        test_R15_contemplacao,
        test_R16_diario,
        test_R17_bicicleta,
        test_R18_encontro,
        test_R19_oficina,
        test_R20_livro,
        test_R21_caminhada_longo,
        test_R22_cozinhar,
        test_R23_passeio_contemplativo,
        test_R24_piquenique,
        test_R25_jantar,
        test_R26_projeto_pessoal,
        test_R27_trilha,
        test_R28_dado_faltante,
        test_R29_sem_correspondencia
    ]

    passou = 0
    falhou = 0
    for t in testes:
        try:
            t()
            passou += 1
        except AssertionError as e:
            print(f"❌ {t.__name__} FALHOU: {e}")
            falhou += 1

    print(f"\n=== Resultado: {passou} passou, {falhou} falhou ===" )