def convertir_ascii_a_binario(texto, separador=" "):
    binarios = []
    for caracter in texto:
        codigo = ord(caracter)
        binario = format(codigo, "08b")
        binarios.append(binario)
    return separador.join(binarios)


def convertir_base64_a_binario(texto_base64, separador=" "):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    limpio = ""
    for c in texto_base64:
        if c != "\n" and c != "\t" and c != " " and c != "\r":
            limpio += c

    padding = 0
    while limpio.endswith("="):
        padding += 1
        limpio = limpio[:-1]

    bits = ""
    for c in limpio:
        indice = alfabeto.index(c)
        bits += format(indice, "06b")

    if padding == 1:
        bits = bits[:-2]
    elif padding == 2:
        bits = bits[:-4]

    binarios = []
    for i in range(0, len(bits), 8):
        byte_bits = bits[i:i + 8]
        binarios.append(byte_bits)

    return separador.join(binarios)


def convertir_binario_a_base64(texto_binario):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binario = texto_binario.replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")

    while len(binario) % 8 != 0:
        binario += "0"

    bits6 = []
    for i in range(0, len(binario), 6):
        grupo = binario[i:i + 6]
        if len(grupo) < 6:
            grupo += "0" * (6 - len(grupo))
        bits6.append(grupo)

    resultado = ""
    for grupo in bits6:
        valor = int(grupo, 2)
        resultado += alfabeto[valor]

    sobrante = (len(texto_binario.replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")) % 24)
    if sobrante == 8:
        resultado = resultado[:-2] + "=="
    elif sobrante == 16:
        resultado = resultado[:-1] + "="

    return resultado


def convertir_binario_a_ascii(texto_binario):
    binario = texto_binario.replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")

    texto = ""
    for i in range(0, len(binario), 8):
        byte_bits = binario[i:i + 8]
        codigo = int(byte_bits, 2)
        texto += chr(codigo)

    return texto


def convertir_base64_a_ascii(texto_base64):
    binario = convertir_base64_a_binario(texto_base64, separador="")
    return convertir_binario_a_ascii(binario)


def aplicar_xor_a_binarios(binario_1, binario_2, separador=" "):
    b1 = binario_1.replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")
    b2 = binario_2.replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")

    resultado = ""
    for i in range(len(b1)):
        if b1[i] == b2[i]:
            resultado += "0"
        else:
            resultado += "1"

    if separador == "":
        return resultado

    grupos = []
    for i in range(0, len(resultado), 8):
        grupos.append(resultado[i:i + 8])

    return separador.join(grupos)


# -----------------------------
# Llamadas (sin main)
# -----------------------------

texto_usuario = input("Ingrese texto ASCII: ")
print("ASCII -> BINARIO:")
print(convertir_ascii_a_binario(texto_usuario))

texto_base64 = input("\nIngrese texto BASE64: ")
print("BASE64 -> BINARIO:")
print(convertir_base64_a_binario(texto_base64))

binario_usuario = input("\nIngrese BINARIO para convertir a BASE64: ")
print("BINARIO -> BASE64:")
print(convertir_binario_a_base64(binario_usuario))

binario_usuario_2 = input("\nIngrese BINARIO para convertir a ASCII: ")
print("BINARIO -> ASCII:")
print(convertir_binario_a_ascii(binario_usuario_2))

texto_base64_2 = input("\nIngrese BASE64 para convertir a ASCII: ")
print("BASE64 -> ASCII (vía binario):")
print(convertir_base64_a_ascii(texto_base64_2))

binario_xor_1 = input("\nIngrese binario 1 para XOR: ")
binario_xor_2 = input("Ingrese binario 2 para XOR: ")
print("XOR:")
print(aplicar_xor_a_binarios(binario_xor_1, binario_xor_2))
