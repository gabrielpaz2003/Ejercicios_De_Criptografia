def cesar_cifrar(mensaje, desplazamiento):
    resultado = ""
    desplazamiento = desplazamiento % 26

    for caracter in mensaje:
        codigo = ord(caracter)

        if 65 <= codigo <= 90:
            indice = codigo - 65
            nuevo = (indice + desplazamiento) % 26
            resultado += chr(65 + nuevo)
        elif 97 <= codigo <= 122:
            indice = codigo - 97
            nuevo = (indice + desplazamiento) % 26
            resultado += chr(97 + nuevo)
        else:
            resultado += caracter

    return resultado


def cesar_descifrar(mensaje, desplazamiento):
    return cesar_cifrar(mensaje, -desplazamiento)


def rot13(mensaje):
    return cesar_cifrar(mensaje, 13)


def vigenere_cifrar(mensaje, clave):
    clave_mayus = ""
    for letra in clave:
        codigo = ord(letra)
        if 65 <= codigo <= 90:
            clave_mayus += letra
        elif 97 <= codigo <= 122:
            clave_mayus += chr(codigo - 32)

    resultado = ""
    indice_clave = 0

    for caracter in mensaje:
        codigo = ord(caracter)

        if 65 <= codigo <= 90:
            letra_clave = clave_mayus[indice_clave % len(clave_mayus)]
            k = ord(letra_clave) - 65

            indice = codigo - 65
            nuevo = (indice + k) % 26
            resultado += chr(65 + nuevo)

            indice_clave += 1

        elif 97 <= codigo <= 122:
            letra_clave = clave_mayus[indice_clave % len(clave_mayus)]
            k = ord(letra_clave) - 65

            indice = codigo - 97
            nuevo = (indice + k) % 26
            resultado += chr(97 + nuevo)

            indice_clave += 1

        else:
            resultado += caracter

    return resultado


def vigenere_descifrar(mensaje, clave):
    clave_mayus = ""
    for letra in clave:
        codigo = ord(letra)
        if 65 <= codigo <= 90:
            clave_mayus += letra
        elif 97 <= codigo <= 122:
            clave_mayus += chr(codigo - 32)

    resultado = ""
    indice_clave = 0

    for caracter in mensaje:
        codigo = ord(caracter)

        if 65 <= codigo <= 90:
            letra_clave = clave_mayus[indice_clave % len(clave_mayus)]
            k = ord(letra_clave) - 65

            indice = codigo - 65
            nuevo = (indice - k) % 26
            resultado += chr(65 + nuevo)

            indice_clave += 1

        elif 97 <= codigo <= 122:
            letra_clave = clave_mayus[indice_clave % len(clave_mayus)]
            k = ord(letra_clave) - 65

            indice = codigo - 97
            nuevo = (indice - k) % 26
            resultado += chr(97 + nuevo)

            indice_clave += 1

        else:
            resultado += caracter

    return resultado


def analisis_frecuencia(mensaje):
    contador = {}
    total = 0

    for caracter in mensaje:
        codigo = ord(caracter)

        if 65 <= codigo <= 90:
            letra = caracter
            contador[letra] = contador.get(letra, 0) + 1
            total += 1
        elif 97 <= codigo <= 122:
            letra = chr(codigo - 32)
            contador[letra] = contador.get(letra, 0) + 1
            total += 1

    tabla = []
    for letra in contador:
        apariciones = contador[letra]
        porcentaje = (apariciones * 100) / total if total else 0
        tabla.append((letra, apariciones, porcentaje))

    tabla.sort(key=lambda fila: fila[1], reverse=True)
    return tabla



def analisis_frecuencia(mensaje_cifrado):
    # Aquí no nos ponemos "finos" con estadística, porque César tiene solo 26 shifts.
    # Lo más práctico es probar todos y ver cuál genera un texto que tenga sentido.
    #
    # El patrón (por defecto "FLAG{") ayuda a detectar rápido el correcto.
    
    
    patron_buscado = input("¿Qué patrón estás buscando? (ej: PASSWORD{): ")

    if mensaje_cifrado is None or len(mensaje_cifrado.strip()) == 0:
        print("No hay mensaje para analizar.")
        return None, None

    if patron_buscado is None or len(patron_buscado.strip()) == 0:
        patron_buscado = "FLAG{"

    patron_buscado = patron_buscado.strip()

    encontrado_shift = None
    encontrado_texto = None

    for k in range(26):
        plano = cesar_descifrar(mensaje_cifrado, k)

        # buscamos el patrón tal cual; si el user puso "flag{" en minúscula también ayuda
        if patron_buscado in plano or patron_buscado.lower() in plano.lower():
            encontrado_shift = k
            encontrado_texto = plano
            break

    if encontrado_shift is None:
        print("\nNo encontré el patrón con ningún desplazamiento (0-25).")
        print("Tip: probá con 'FLAG{' o con una palabra que esperes ver en el texto.")
        return None, None

    print("\nListo. Esto fue lo que encontré:")
    print("Shift detectado:", encontrado_shift)
    print("Texto descifrado:")
    print(encontrado_texto)

    return encontrado_shift, encontrado_texto

## Aca puedo hacer la llamada a las funciones que necesite:

#print(cesar_descifrar("IODJ{FHVUD_FLIUDGR}", 3))
#print(rot13("SYNT{FRPERG_SYNT_EBBG13}"))


print(analisis_frecuencia("SV OHU JVUZLNBPKV, OHU LUJVUAYHKV BUH MSHN WHYH LS ZPNBPLUAL KLZHMPV MSHN{JYFWAV_HUHSFZPZ}"))


