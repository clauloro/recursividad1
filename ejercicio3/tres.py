def es_palindromo(frase):
    caracteres = ''
    for c in frase:
        if c.isalpha():                         #para verificar si un carácter es una letra
            caracteres += c.lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        elif c.isdigit():                       #para verificar si un carácter es un dígito 
            caracteres += c
    return caracteres == caracteres[::-1]
   
print(es_palindromo("Hello world"))
print(es_palindromo("Salas"))
print(es_palindromo("oSo"))
print(es_palindromo("26762"))