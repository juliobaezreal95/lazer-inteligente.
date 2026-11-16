# -*- coding: utf-8 -*-
"""
Base de Conhecimento — Lazer Inteligente
Arquivo que guarda regras e fontes do sistema especialista
Versão Ampliada — 30 Regras
"""

REGRAS = [
    # === TEMPO CURTO ===
    {
        "id": "R01",
        "fonte": "F01",
        "condicoes": {
            "tempo": "curto",
            "ambiente": "interno",
            "preferencia": "tranquilidade"
        },
        "conclusao": "Leitura"
    },
    {
        "id": "R02",
        "fonte": "F01",
        "condicoes": {
            "tempo": "curto",
            "ambiente": "interno",
            "preferencia": "movimento"
        },
        "conclusao": "Filme ou série"
    },
    {
        "id": "R03",
        "fonte": "F01",
        "condicoes": {
            "tempo": "curto",
            "ambiente": "externo",
            "preferencia": "tranquilidade"
        },
        "conclusao": "Caminhada ao ar livre"
    },
    {
        "id": "R04",
        "fonte": "F02",
        "condicoes": {
            "tempo": "curto",
            "ambiente": "externo",
            "preferencia": "movimento"
        },
        "conclusao": "Caminhada ao ar livre"
    },
    {
        "id": "R05",
        "fonte": "F01",
        "condicoes": {
            "tempo": "curto",
            "ambiente": "interno",
            "preferencia": "social"
        },
        "conclusao": "Conversa com amigos ou família"
    },
    {
        "id": "R06",
        "fonte": "F02",
        "condicoes": {
            "tempo": "curto",
            "ambiente": "externo",
            "preferencia": "social"
        },
        "conclusao": "Conversa em um parque ou praça"
    },
    {
        "id": "R07",
        "fonte": "F01",
        "condicoes": {
            "tempo": "curto",
            "ambiente": "indiferente",
            "preferencia": "tranquilidade"
        },
        "conclusao": "Ouvir música ou podcast relaxante"
    },
    {
        "id": "R08",
        "fonte": "F02",
        "condicoes": {
            "tempo": "curto",
            "ambiente": "indiferente",
            "preferencia": "movimento"
        },
        "conclusao": "Alongamento ou exercícios leves"
    },
    {
        "id": "R09",
        "fonte": "F01",
        "condicoes": {
            "tempo": "curto",
            "ambiente": "indiferente",
            "preferencia": "social"
        },
        "conclusao": "Mensagem ou chamada com alguém querido"
    },

    # === TEMPO MÉDIO ===
    {
        "id": "R10",
        "fonte": "F01",
        "condicoes": {
            "tempo": "medio",
            "ambiente": "interno",
            "preferencia": "social"
        },
        "conclusao": "Jogo em grupo"
    },
    {
        "id": "R11",
        "fonte": "F02",
        "condicoes": {
            "tempo": "medio",
            "ambiente": "interno",
            "preferencia": "tranquilidade"
        },
        "conclusao": "Leitura"
    },
    {
        "id": "R12",
        "fonte": "F01",
        "condicoes": {
            "tempo": "medio",
            "ambiente": "externo",
            "preferencia": "movimento"
        },
        "conclusao": "Caminhada ao ar livre"
    },
    {
        "id": "R13",
        "fonte": "F02",
        "condicoes": {
            "tempo": "medio",
            "ambiente": "externo",
            "preferencia": "social"
        },
        "conclusao": "Jogo em grupo ao ar livre"
    },
    {
        "id": "R14",
        "fonte": "F01",
        "condicoes": {
            "tempo": "medio",
            "ambiente": "interno",
            "preferencia": "movimento"
        },
        "conclusao": "Praticar uma dança ou exercício em casa"
    },
    {
        "id": "R15",
        "fonte": "F02",
        "condicoes": {
            "tempo": "medio",
            "ambiente": "externo",
            "preferencia": "tranquilidade"
        },
        "conclusao": "Sentar em um local silencioso e observar a natureza"
    },
    {
        "id": "R16",
        "fonte": "F01",
        "condicoes": {
            "tempo": "medio",
            "ambiente": "indiferente",
            "preferencia": "tranquilidade"
        },
        "conclusao": "Escutar um álbum completo ou escrever em um diário"
    },
    {
        "id": "R17",
        "fonte": "F02",
        "condicoes": {
            "tempo": "medio",
            "ambiente": "indiferente",
            "preferencia": "movimento"
        },
        "conclusao": "Passeio de bicicleta ou caminhada mais longa"
    },
    {
        "id": "R18",
        "fonte": "F01",
        "condicoes": {
            "tempo": "medio",
            "ambiente": "indiferente",
            "preferencia": "social"
        },
        "conclusao": "Encontro casual com amigos"
    },

    # === TEMPO LONGO ===
    {
        "id": "R19",
        "fonte": "F01",
        "condicoes": {
            "tempo": "longo",
            "ambiente": "indiferente",
            "preferencia": "social"
        },
        "conclusao": "Oficina criativa"
    },
    {
        "id": "R20",
        "fonte": "F02",
        "condicoes": {
            "tempo": "longo",
            "ambiente": "interno",
            "preferencia": "tranquilidade"
        },
        "conclusao": "Leitura de um livro completo"
    },
    {
        "id": "R21",
        "fonte": "F01",
        "condicoes": {
            "tempo": "longo",
            "ambiente": "externo",
            "preferencia": "movimento"
        },
        "conclusao": "Caminhada ao ar livre"
    },
    {
        "id": "R22",
        "fonte": "F02",
        "condicoes": {
            "tempo": "longo",
            "ambiente": "interno",
            "preferencia": "movimento"
        },
        "conclusao": "Cozinhar algo novo ou fazer exercícios completos"
    },
    {
        "id": "R23",
        "fonte": "F01",
        "condicoes": {
            "tempo": "longo",
            "ambiente": "externo",
            "preferencia": "tranquilidade"
        },
        "conclusao": "Visita a um parque, praia ou passeio contemplativo"
    },
    {
        "id": "R24",
        "fonte": "F02",
        "condicoes": {
            "tempo": "longo",
            "ambiente": "externo",
            "preferencia": "social"
        },
        "conclusao": "Piquenique ou passeio em grupo ao ar livre"
    },
    {
        "id": "R25",
        "fonte": "F01",
        "condicoes": {
            "tempo": "longo",
            "ambiente": "interno",
            "preferencia": "social"
        },
        "conclusao": "Jantar ou jogo longo com familiares/amigos"
    },
    {
        "id": "R26",
        "fonte": "F02",
        "condicoes": {
            "tempo": "longo",
            "ambiente": "indiferente",
            "preferencia": "tranquilidade"
        },
        "conclusao": "Projeto pessoal: desenho, escrita ou estudo de algo que goste"
    },
    {
        "id": "R27",
        "fonte": "F01",
        "condicoes": {
            "tempo": "longo",
            "ambiente": "indiferente",
            "preferencia": "movimento"
        },
        "conclusao": "Trilha, passeio esportivo ou visitar um lugar novo"
    },

    # === REGRAS ESPECIAIS ===
    {
        "id": "R28",
        "fonte": "F02",
        "condicoes_especiais": "dado_faltante",
        "conclusao": "Encaminhar para decisão humana"
    },
    {
        "id": "R29",
        "fonte": "F01",
        "condicoes_especiais": "sem_correspondencia",
        "conclusao": "Encaminhar para decisão humana"
    },
    {
        "id": "R30",
        "fonte": "F02",
        "condicoes_especiais": "entrada_invalida",
        "conclusao": "Revise suas respostas e tente novamente"
    }
]

FONTES = {
    "F01": {
        "titulo": "Guia de Atividades de Lazer Comunitário",
        "autor": "Coordenação de Cultura e Lazer",
        "versao": "3.0 / Novembro 2026 — Ampliada"
    },
    "F02": {
        "titulo": "Diretrizes de Bem-Estar e Uso do Tempo Livre",
        "autor": "Equipe de Desenvolvimento Social",
        "versao": "2.2 / Novembro 2026 — Ampliada"
    }
}