import os

def buscar_archivo_por_firma(ruta_archivo, firma_hex):
    """
    Busca segmentos de archivo embebidos en un archivo a partir de firmas hexadecimales.
    """
    try:
        with open(ruta_archivo, "rb") as archivo:
            datos = archivo.read()

        # Convertir la firma hexadecimal a bytes si no está ya en formato bytes
        firma_bytes = bytes.fromhex(firma_hex) if isinstance(firma_hex, str) else firma_hex
        indices = []

        # Buscar todas las ocurrencias de la firma
        posicion = datos.find(firma_bytes)
        while posicion != -1:
            indices.append(posicion)
            posicion = datos.find(firma_bytes, posicion + 1)

        if not indices:
            print(f"No se encontraron archivos con la firma {firma_hex} en el archivo proporcionado.")
            return []

        # Extraer segmentos basados en la firma
        segmentos = []
        for i, inicio in enumerate(indices):
            # Determinar el final del segmento (antes del siguiente encabezado)
            fin = indices[i + 1] if i + 1 < len(indices) else len(datos)
            segmento = datos[inicio:fin]
            segmentos.append(segmento)

        return segmentos
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return []

def guardar_archivos(segmentos, directorio_salida, extension):
    """
    Guarda los archivos extraídos en el directorio de salida con una extensión determinada.
    """
    os.makedirs(directorio_salida, exist_ok=True)
    for i, segmento in enumerate(segmentos):
        ruta_salida = os.path.join(directorio_salida, f"archivo_extraido_{i + 1}.{extension}")
        try:
            with open(ruta_salida, "wb") as archivo_salida:
                archivo_salida.write(segmento)
            print(f"Archivo guardado: {ruta_salida}")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

def main():
    ruta_archivo = input("Ingresa la ruta del archivo a analizar: ")

    # Opciones de formatos predefinidos
    firmas_predefinidas = {
        "ZIP": {"firma": "504b0304", "extension": "zip"},
        "PDF": {"firma": "25504446", "extension": "pdf"},
        "PNG": {"firma": "89504e47", "extension": "png"},
        "JPG": {"firma": "ffd8ffe0", "extension": "jpg"},
        "GIF": {"firma": "47494638", "extension": "gif"},
        "RAR": {"firma": "52617221", "extension": "rar"},
    }

    print("\nOpciones disponibles:")
    for i, formato in enumerate(firmas_predefinidas.keys(), start=1):
        print(f"{i}. {formato}")
    print(f"{len(firmas_predefinidas) + 1}. Personalizado (ingresa tu propia firma)")

    opcion = input("\nSelecciona el formato que deseas buscar (número): ")
    if opcion.isdigit() and int(opcion) in range(1, len(firmas_predefinidas) + 2):
        opcion = int(opcion)
    else:
        print("Opción inválida.")
        return

    # Elegir firma a buscar
    if opcion == len(firmas_predefinidas) + 1:  # Opción personalizada
        firma_hex = input("Ingresa la firma hexadecimal que deseas buscar (sin espacios, por ejemplo: 504b0304): ")
        extension = input("Ingresa la extensión del archivo (por ejemplo: zip, pdf, png): ")
    else:
        formato = list(firmas_predefinidas.keys())[opcion - 1]
        firma_hex = firmas_predefinidas[formato]["firma"]
        extension = firmas_predefinidas[formato]["extension"]

    print(f"\nBuscando archivos con la firma {firma_hex}...\n")

    # Buscar segmentos con la firma seleccionada
    segmentos = buscar_archivo_por_firma(ruta_archivo, firma_hex)
    if not segmentos:
        print("No se encontraron archivos con la firma especificada.")
        return

    # Guardar los segmentos encontrados
    directorio_salida = f"archivos_extraidos_{extension}"
    guardar_archivos(segmentos, directorio_salida, extension)

    print("\nProceso completado.")

if __name__ == "__main__":
    main()

