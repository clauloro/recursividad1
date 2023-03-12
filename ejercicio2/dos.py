def es_palindromo(frase):
    # Eliminar todos los caracteres no alfanuméricos y convertir a minúsculas
    caracteres = [c.lower() for c in frase if c.isalnum()]
    # Eliminar acentos
    caracteres = [c.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u') for c in caracteres]
    
    # Verificar si la cadena es un palíndromo
    def es_palindromo_recursivo(cadena):
        if len(cadena) <= 1:
            return True
        elif cadena[0] == cadena[-1]:
            return es_palindromo_recursivo(cadena[1:-1])
        else:
            return False
    
    return es_palindromo_recursivo(caracteres)
