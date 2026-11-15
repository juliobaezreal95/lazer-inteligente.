# lazer-inteligente.
Sistema Especialista de Recomendação de Atividades

# Lazer Inteligente — Sistema Especialista

## 1. Decisão Apoiada
O sistema recomenda uma atividade de lazer com base em três informações: tempo disponível, ambiente preferido e tipo de atividade desejada. Versão ampliada com **30 regras** de conhecimento.

## 2. Escopo e Limites
- **Usuário:** pessoa buscando sugestão de lazer
- **Entradas:**
  - `tempo`: curto | medio | longo
  - `ambiente`: interno | externo | indiferente
  - `preferencia`: tranquilidade | movimento | social
- **Saídas:** 27 atividades específicas + 3 respostas especiais
- **NÃO decide:** orçamento, restrições de saúde, localização real, condições climáticas, disponibilidade de equipamentos

## 3. Estrutura das Pastas

A4_Lazer_Inteligente/
├── README.md
├── src/
│   ├── __init__.py
│   ├── base_conhecimento.py
│   ├── inferencia.py
│   └── executar.py
├── tests/
│   ├── __init__.py
│   └── test_sistema.py
└── docs/
    ├── escopo_e_fontes.md
    ├── tabela_de_decisao.md
    └── matriz_regra-caso-fonte.md

## 4. Requisitos
- Python 3.8 ou superior
- Usa apenas biblioteca padrão — sem instalação de pacotes extras

## 5. Como Executar

### ▶️ Executar o sistema principal
```bash
python -m src.executar
