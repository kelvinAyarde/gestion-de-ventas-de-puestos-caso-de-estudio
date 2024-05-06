
def formato_error(resultado):
    # Verifica si el resultado es una cadena (str)
    if isinstance(resultado, str):
        # Si es una cadena, asume que contiene un mensaje de error y lo asigna directamente a la variable mensaje_error
        mensaje_error = resultado
    else:
        # Si no es una cadena, asume que es una excepción u objeto de error y accede al segundo elemento de sus argumentos (args[1]).
        # Esto se hace bajo la suposición de que el segundo elemento de los argumentos es el mensaje de error en la mayoría de los objetos de excepción.
        mensaje_error = resultado.args[1]
    # Devuelve el mensaje de error obtenido
    return mensaje_error
