# -*- coding: utf-8 -*-
"""
Motor de Inferência — Lazer Inteligente
Encadeamento à frente
Versão Ampliada para 30 Regras
"""

from src.base_conhecimento import REGRAS


def recomendar_atividade(dados_usuario):
    regras_testadas = []
    regras_aplicadas = []
    conclusao = None
    regra_aplicada = None
    fonte_aplicada = None

    campos_obrigatorios = ["tempo", "ambiente", "preferencia"]
    tem_dado_faltante = any(
        campo not in dados_usuario or dados_usuario[campo] is None
        for campo in campos_obrigatorios
    )

    if tem_dado_faltante:
        for regra in REGRAS:
            if regra.get("condicoes_especiais") == "dado_faltante":
                regras_aplicadas.append(regra["id"])
                conclusao = regra["conclusao"]
                regra_aplicada = regra["id"]
                fonte_aplicada = regra["fonte"]
                break
        return {
            "dados_entrada": dados_usuario,
            "regras_testadas": regras_testadas,
            "regras_aplicadas": regras_aplicadas,
            "conclusao": conclusao,
            "regra": regra_aplicada,
            "fonte": fonte_aplicada,
            "dado_faltante": True
        }

    for regra in REGRAS:
        if "condicoes_especiais" in regra:
            continue

        regras_testadas.append(regra["id"])
        condicoes = regra["condicoes"]
        corresponde = True

        for chave, valor_esperado in condicoes.items():
            if dados_usuario.get(chave) != valor_esperado:
                corresponde = False
                break

        if corresponde:
            regras_aplicadas.append(regra["id"])
            conclusao = regra["conclusao"]
            regra_aplicada = regra["id"]
            fonte_aplicada = regra["fonte"]
            break

    if conclusao is None:
        regras_aplicadas.append("R29")
        conclusao = "Encaminhar para decisão humana"
        regra_aplicada = "R29"
        fonte_aplicada = "F01"

    return {
        "dados_entrada": dados_usuario,
        "regras_testadas": regras_testadas,
        "regras_aplicadas": regras_aplicadas,
        "conclusao": conclusao,
        "regra": regra_aplicada,
        "fonte": fonte_aplicada,
        "dado_faltante": False
    }