def generar_llave_ascii_dinamica(longitud, semilla=12345):
    multiplicador = 1103515245
    incremento = 12345
    modulo = 2**31

    estado = semilla
    llave = ""

    for _ in range(longitud):
        estado = (multiplicador * estado + incremento) % modulo
        codigo_ascii = 32 + (estado % 95)
        llave += chr(codigo_ascii)

    return llave


def cifrar_ascii_con_llave_fija(texto_plano, llave_fija):
    texto_cifrado = ""

    for indice in range(len(texto_plano)):
        codigo_texto = ord(texto_plano[indice])
        k = ord(llave_fija[indice % len(llave_fija)])
        codigo_cifrado = codigo_texto ^ k
        texto_cifrado += chr(codigo_cifrado)

    return texto_cifrado


def descifrar_ascii_con_llave_fija(texto_cifrado, llave_fija):
    texto_plano = ""

    for indice in range(len(texto_cifrado)):
        codigo_cifrado = ord(texto_cifrado[indice])
        k = ord(llave_fija[indice % len(llave_fija)])
        codigo_plano = codigo_cifrado ^ k
        texto_plano += chr(codigo_plano)

    return texto_plano


def cifrar_ascii_con_llave_dinamica(texto_plano, semilla=12345):
    llave_dinamica = generar_llave_ascii_dinamica(len(texto_plano), semilla)
    texto_cifrado = ""

    for indice in range(len(texto_plano)):
        codigo_texto = ord(texto_plano[indice])
        k = ord(llave_dinamica[indice])
        codigo_cifrado = codigo_texto ^ k
        texto_cifrado += chr(codigo_cifrado)

    return texto_cifrado, llave_dinamica


def descifrar_ascii_con_llave_dinamica(texto_cifrado, llave_dinamica):
    texto_plano = ""

    for indice in range(len(texto_cifrado)):
        codigo_cifrado = ord(texto_cifrado[indice])
        k = ord(llave_dinamica[indice])
        codigo_plano = codigo_cifrado ^ k
        texto_plano += chr(codigo_plano)

    return texto_plano


texto_usuario = input("Ingrese un texto (ASCII): ")

tamanio_llave = int(input("Ingrese el tamaño de llave dinámica a generar: "))
llave_generada = generar_llave_ascii_dinamica(tamanio_llave, semilla=2026)
print("\nLlave dinámica generada:")
print(llave_generada)

