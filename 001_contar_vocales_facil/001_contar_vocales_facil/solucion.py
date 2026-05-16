# 001 · Contar vocales · Fácil
# ─────────────────────────────────────────────────────

def contar_vocales(texto: str) -> dict:
    vocales = 'aeiou'
    texto = texto.lower()
    return {vocal: texto.count(vocal) for vocal in vocales}


if __name__ == "__main__":
    print(contar_vocales("hola mundo"))  # {'a': 1, 'e': 0, 'i': 0, 'o': 2, 'u': 1}
    print(contar_vocales("AEIOU"))       # {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
    print(contar_vocales(""))            # {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}