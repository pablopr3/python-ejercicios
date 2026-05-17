# 001 · Contar vocales · Fácil
# ─────────────────────────────────────────────────────

from collections import Counter


def contar_vocales(texto: str) -> dict[str, int]:
    """
    Cuenta cuántas veces aparece cada vocal en un texto.

    Args:
        texto: Texto a analizar.

    Returns:
        Diccionario con el total de cada vocal.
    """

    contador = Counter(c for c in texto.lower() if c in "aeiou")

    return {
        vocal: contador.get(vocal, 0)
        for vocal in "aeiou"
    }


if __name__ == "__main__":
    ejemplos = [
        "hola mundo",
        "AEIOU",
        "",
    ]

    for texto in ejemplos:
        print(f'"{texto}" -> {contar_vocales(texto)}')