import re

def bionic_reading(text):
    # Separar el texto en palabras
    words = text.split()

    # Lista de palabras ignoradas
    ignored_words = ['el', 'la', 'los', 'las', 'de', 'del', 'y', 'a', 'ante', 'bajo', 'con', 'contra', 'desde', 'en', 'entre', 'hacia', 'hasta', 'para', 'por', 'según', 'sin', 'sobre', 'tras', 'que', 'se', 'su', 'sus', 'o', 'u', 'un', 'una', 'unos', 'unas']

    # Lista de palabras importantes
    important_words = []
    for word in words:
        if word.lower() not in ignored_words:
            important_words.append(word)

    # Resaltar las letras más importantes de cada palabra
    formatted_words = []
    for word in important_words:
        formatted_word = ''
        if len(word) <= 3:
            formatted_word = '<b>' + word[0] + '</b>' + word[1:]
        else:
            formatted_word = '<b>' + word[0] + '</b>'
            for i in range(1, len(word)-1):
                if i % 2 == 0:
                    formatted_word += '<b>' + word[i] + '</b>'
                else:
                    formatted_word += word[i]
            formatted_word += '<b>' + word[-1] + '</b>'
        formatted_words.append(formatted_word)

    # Unir las palabras formateadas en el texto final
    formatted_text = ''
    for i in range(len(words)):
        if words[i].lower() in ignored_words:
            formatted_text += words[i] + ' '
        else:
            formatted_text += formatted_words.pop(0) + ' '

    # Dividir el texto en líneas de máximo 3 palabras
    lines = []
    line = ''
    for word in formatted_text.split():
        if len(line.split()) < 3:
            line += word + ' '
        else:
            lines.append(line.strip())
            line = word + ' '
    if line:
        lines.append(line.strip())

    # Unir las líneas en el texto final
    final_text = ''
    for line in lines:
        final_text += line + '<br>'

    return final_text

# Pedir al usuario que introduzca un texto
#text = input('Introduce un texto: ')
fichero = open("prebionic.txt", "r")
text = fichero.read()

# Convertir el texto a formato bionic reading y guardarlo en un archivo
with open('texto_bionic_reading.html', 'w') as f:
    f.write('<html><body><head><style> body { font-family: "Roboto"; text-align: center; column-count: 4; column-width: 300px;} </style></head>' + bionic_reading(text) + '</body></html>')

print('El archivo "texto_bionic_reading.html" se ha guardado correctamente.')

