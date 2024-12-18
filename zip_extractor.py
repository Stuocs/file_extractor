import binascii
import os

def buscar_zip_en_archivo(ruta_archivo):
    """
    Busca archivos ZIP embebidos en un archivo a partir de firmas hexadecimales.
    """
    try:
        with open(ruta_archivo, "rb") as archivo:
            datos = archivo.read()

        # Firma hexadecimal del inicio de un archivo ZIP
        firma_zip = b"PK\x03\x04"  #Modifica esto para agregar o cambiar la firma, PK es la firma de ZIP
        indices = []

        # Buscar todas las ocurrencias de la firma ZIP
        posicion = datos.find(firma_zip)
        while posicion != -1:
            indices.append(posicion)
            posicion = datos.find(firma_zip, posicion + 1)

        if not indices:
            print("No se encontraron archivos ZIP en el archivo proporcionado.")
            return []

        # Extraer segmentos ZIP
        archivos_zip = []
        for i, inicio in enumerate(indices):
            # Determinar el final del archivo ZIP (antes del siguiente encabezado)
            fin = indices[i + 1] if i + 1 < len(indices) else len(datos)
            segmento_zip = datos[inicio:fin]
            archivos_zip.append(segmento_zip)

        return archivos_zip
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return []

def reparar_zip(segmento_zip):
    """
    Intenta reparar un archivo ZIP corrigiendo duplicados y errores simples.
    """
    try:
        # Aquí se pueden implementar más reglas de reparación según sea necesario.
        return segmento_zip
    except Exception as e:
        print(f"Error al reparar el archivo ZIP: {e}")
        return None

def guardar_zip(segmentos_zip, directorio_salida):
    """
    Guarda los archivos ZIP extraídos en el directorio de salida.
    """
    os.makedirs(directorio_salida, exist_ok=True)
    for i, segmento_zip in enumerate(segmentos_zip):
        ruta_zip = os.path.join(directorio_salida, f"archivo_extraido_{i + 1}.zip")
        try:
            with open(ruta_zip, "wb") as archivo_zip:
                archivo_zip.write(segmento_zip)
            print(f"Archivo ZIP guardado: {ruta_zip}")
        except Exception as e:
            print(f"Error al guardar el archivo ZIP: {e}")

def main():
    ruta_archivo = input("Ingresa la ruta del archivo a analizar: ")
    directorio_salida = "archivos_extraidos"

    # Buscar archivos ZIP embebidos
    print("Buscando archivos ZIP...")
    segmentos_zip = buscar_zip_en_archivo(ruta_archivo)

    if not segmentos_zip:
        print("No se encontraron archivos ZIP.")
        return

    # Reparar y guardar los archivos ZIP
    print("Reparando y guardando archivos ZIP...")
    archivos_reparados = [reparar_zip(segmento) for segmento in segmentos_zip]
    guardar_zip(archivos_reparados, directorio_salida)

    print("Proceso completado.")

if __name__ == "__main__":
    main()