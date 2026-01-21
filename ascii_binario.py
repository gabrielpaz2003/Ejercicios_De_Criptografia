def convertir_ascii_a_binario(texto, separador=" "):
    for caracter in texto:
        if ord(caracter) > 127:
            raise ValueError(f"Se encontró un caracter fuera de ASCII: {caracter}")
    binarios = []
    for caracter in texto:
        codigo = ord(caracter)
        binario = format(codigo, "08b")
        binarios.append(binario)

    return separador.join(binarios)

texto_usuario = input("Ingrese una palabra o frase (ASCII): ")

try:
    resultado = convertir_ascii_a_binario(texto_usuario)
    print("\nBinario (8 bits por caracter):")
    print(resultado)

except ValueError as error:
    print(f"\nError: {error}")
