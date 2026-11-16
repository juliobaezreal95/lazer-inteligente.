# -*- coding: utf-8 -*-
"""
Programa Principal — Lazer Inteligente
Interage com o usuário, coleta respostas e exibe recomendação
Versão Ampliada
"""

from src.inferencia import recomendar_atividade


def exibir_explicacao(resultado):
    print("\n" + "=" * 50)
    print("📋 DADOS FORNECIDOS")
    for chave, valor in resultado["dados_entrada"].items():
        print(f"   {chave}: {valor if valor else 'Não informado'}")

    print("\n🔍 REGRAS VERIFICADAS:")
    if resultado["regras_testadas"]:
        print(f"   {', '.join(resultado['regras_testadas'])}")
    else:
        print("   Nenhuma regra de condição avaliada")

    print("\n✅ REGRA APLICADA:")
    print(f"   {resultado['regra']} (fonte {resultado['fonte']})")

    print("\n🎯 RECOMENDAÇÃO FINAL:")
    print(f"   {resultado['conclusao']}")
    print("=" * 50 + "\n")


def main():
    print("🎯 SISTEMA LAZER INTELIGENTE")
    print("Responda às perguntas abaixo para receber uma recomendação.\n")

    dados = {}

    print("1. Quanto tempo você tem disponível?")
    print("   Opções: curto / medio / longo")
    dados["tempo"] = input("   → ").strip().lower() or None

    print("\n2. Qual ambiente você prefere?")
    print("   Opções: interno / externo / indiferente")
    dados["ambiente"] = input("   → ").strip().lower() or None

    print("\n3. Que tipo de atividade você busca?")
    print("   Opções: tranquilidade / movimento / social")
    dados["preferencia"] = input("   → ").strip().lower() or None

    print("\nAnalisando...")
    resultado = recomendar_atividade(dados)
    exibir_explicacao(resultado)


if __name__ == "__main__":
    main()