import base64

def criptografar(texto: str) -> str:
    """Codifica o texto em base64."""
    texto_bytes = texto.encode("utf-8")
    base64_bytes = base64.b64encode(texto_bytes)
    return base64_bytes.decode("utf-8")

def descriptografar(texto_codificado: str) -> str:
    """Decodifica o texto de base64 para string original."""
    base64_bytes = texto_codificado.encode("utf-8")
    texto_bytes = base64.b64decode(base64_bytes)
    return texto_bytes.decode("utf-8")