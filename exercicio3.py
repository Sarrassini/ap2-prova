def validar_documento(documento):
    if not documento or not isinstance(documento, str):
        return False
    
    documento_limpo = documento.replace(".", "").replace("-", "").strip()
    
    return documento_limpo.isdigit() and len(documento_limpo) == 11