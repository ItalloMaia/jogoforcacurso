#!/usr/bin/env python3
"""
Jogo da Forca - Edição Cultura Nortista
Um jogo simples de forca no terminal, com palavras
ligadas à cultura do Pará e Maranhão.
"""

import random

# Estágios do boneco da forca (0 = nenhum erro, 6 = enforcado)
ESTAGIOS = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """,
]

# Banco de palavras com dicas (tema: cultura do Norte/Nordeste)
PALAVRAS = [
    ("CIRIO", "Grande festa religiosa realizada em Belém do Pará"),
    ("CARIMBO", "Ritmo musical tradicional paraense"),
    ("TACACA", "Prato típico servido quente, com tucupi e jambu"),
    ("BREGA", "Estilo musical muito popular no Pará"),
    ("MARAJO", "Ilha famosa localizada na foz do Rio Amazonas"),
    ("ACAI", "Fruto típico da região amazônica, muito consumido no Pará"),
    ("BUMBA MEU BOI", "Festa e dança folclórica maranhense"),
    ("TAMBOR", "Instrumento usado em rodas de carimbó e reggae paraense"),
    ("BELEM", "Capital do estado do Pará"),
    ("SAO LUIS", "Capital do estado do Maranhão"),
]


def escolher_palavra():
    return random.choice(PALAVRAS)


def mostrar_palavra(palavra, letras_corretas):
    return " ".join(
        [letra if letra in letras_corretas or letra == " " else "_" for letra in palavra]
    )


def jogar():
    palavra, dica = escolher_palavra()
    letras_corretas = set()
    letras_erradas = set()
    erros = 0
    max_erros = len(ESTAGIOS) - 1

    print("=" * 50)
    print("   JOGO DA FORCA - EDIÇÃO CULTURA NORTISTA")
    print("=" * 50)
    print(f"\nDica: {dica}")

    while erros < max_erros:
        print(ESTAGIOS[erros])
        print("Palavra:", mostrar_palavra(palavra, letras_corretas))
        if letras_erradas:
            print("Letras erradas:", ", ".join(sorted(letras_erradas)))

        if all(letra in letras_corretas or letra == " " for letra in palavra):
            print("\nVocê venceu! A palavra era:", palavra)
            break

        chute = input("\nDigite uma letra: ").strip().upper()

        if len(chute) != 1 or not chute.isalpha():
            print("Digite apenas uma letra válida.")
            continue

        if chute in letras_corretas or chute in letras_erradas:
            print("Você já tentou essa letra.")
            continue

        if chute in palavra:
            letras_corretas.add(chute)
        else:
            letras_erradas.add(chute)
            erros += 1
    else:
        print(ESTAGIOS[erros])
        print(f"\nVocê perdeu! A palavra era: {palavra}")

    jogar_novamente = input("\nQuer jogar de novo? (s/n): ").strip().lower()
    if jogar_novamente == "s":
        jogar()
    else:
        print("\nValeu por jogar! Até a próxima.")


if __name__ == "__main__":
    jogar()
