from langdetect import detect_langs

def detect_language(text):
    """
    Función para detectar el idioma predominante en un texto dado.
    :param text: El texto para detectar el idioma.
    :return: El código ISO 639-1 del idioma detectado (e.g., 'en' para inglés, 'es' para español).
    """
    try:
        language_list = detect_langs(text)
        # Obtenemos el idioma con la probabilidad más alta
        dominant_language = language_list[0]
        return dominant_language.lang
    except:
        # En caso de que la detección falle, retornamos None
        return None

if __name__ == "__main__":
    # Ejemplo de uso
    text = input("Ingrese el texto para detectar el idioma: ")
    language_code = detect_language(text)
    if language_code:
        if language_code == 'en':
            print("El texto está en inglés.")
        elif language_code == 'es':
            print("El texto está en español.")
        else:
            print(f"El texto está en un idioma cuyo código es: '{language_code}'.")
    else:
        print("No se pudo detectar el idioma del texto.")
