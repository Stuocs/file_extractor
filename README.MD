# File Extraction Tool

This project provides two versions of a file extraction tool:

1. **Original Version**: Focuses solely on extracting ZIP files embedded within other files based on their hexadecimal signature.
2. **Updated Version**: Expands the functionality to support multiple file formats (ZIP, PDF, PNG, JPG, GIF, RAR, and more), allowing users to search for files embedded in other files based on their hexadecimal signatures.

## English

### Overview

The file extraction tool allows you to extract embedded files from other files by searching for specific hexadecimal signatures. You can extract various types of files (ZIP, PDF, PNG, JPG, GIF, RAR) or even specify a custom signature for different file types.

### Features

- **Original Version**:
    - Extracts only ZIP files embedded in other files using the ZIP file signature (`PK\x03\x04`).
- **Updated Version**:
    - Supports ZIP, PDF, PNG, JPG, GIF, and RAR file formats, as well as custom hexadecimal signatures for more flexibility.
    - Allows users to input their own signature to search for any file type.
  
### Requirements

- Python 3.x
- No external dependencies

### How to Use

#### Original Version

1. Download the script from the GitHub repository.
2. Run the script using Python 3.x.
3. Provide the file path to the file that you want to analyze (can be any file, such as an ELF or a PCAP).
4. The script will search for embedded ZIP files and save them as separate `.zip` files in the `archivos_extraidos_zip` folder.

#### Updated Version

1. Download the script from the GitHub repository.
2. Run the script using Python 3.x.
3. When prompted, choose the file format to search for (e.g., ZIP, PDF, PNG, etc.), or input a custom hexadecimal signature and file extension.
4. The script will search for files embedded within the provided file, extract them, and save them in a folder named `archivos_extraidos_[extension]`, where `[extension]` is the file type you selected.

### Example Usage

```bash
python extract_files.py
```

Follow the prompts to select or input the file signature you wish to search for.

---

## Español

### Descripción

Esta herramienta permite extraer archivos incrustados dentro de otros archivos mediante la búsqueda de firmas hexadecimales específicas. Puedes extraer archivos de varios tipos (ZIP, PDF, PNG, JPG, GIF, RAR) o incluso especificar una firma personalizada para diferentes tipos de archivos.

### Características

- **Versión Original**:
    - Extrae únicamente archivos ZIP incrustados dentro de otros archivos utilizando la firma del archivo ZIP (`PK\x03\x04`).
- **Versión Actualizada**:
    - Soporta formatos de archivos ZIP, PDF, PNG, JPG, GIF y RAR, además de permitir firmas hexadecimales personalizadas para una mayor flexibilidad.
    - Permite al usuario ingresar su propia firma para buscar cualquier tipo de archivo.

### Requisitos

- Python 3.x
- No hay dependencias externas

### Cómo Usar

#### Versión Original

1. Descarga el script desde el repositorio de GitHub.
2. Ejecuta el script utilizando Python 3.x.
3. Proporciona la ruta del archivo que deseas analizar (puede ser cualquier archivo, como un ELF o un PCAP).
4. El script buscará archivos ZIP incrustados y los guardará como archivos `.zip` separados en la carpeta `archivos_extraidos_zip`.

#### Versión Actualizada

1. Descarga el script desde el repositorio de GitHub.
2. Ejecuta el script utilizando Python 3.x.
3. Cuando se te solicite, elige el formato de archivo que deseas buscar (por ejemplo, ZIP, PDF, PNG, etc.) o ingresa una firma hexadecimal personalizada y la extensión del archivo.
4. El script buscará archivos incrustados dentro del archivo proporcionado, los extraerá y los guardará en una carpeta llamada `archivos_extraidos_[extensión]`, donde `[extensión]` es el tipo de archivo seleccionado.

### Ejemplo de Uso

```bash
python extract_files.py
```

Sigue las indicaciones para seleccionar o ingresar la firma del archivo que deseas buscar.

---

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
