def FilePassword():
    # Abre el archivo "password" en modo escritura y escribe contraseñas de ejemplo
    with open("password", "w") as f:
        f.write("Karonte353453@!#@#@#\n 124324434\n 46t34563454")

    # Abre el archivo "password.txt" en modo lectura para validar cada línea
    with open("password.txt", "r") as f:
          for password in f:
               # Define los símbolos especiales permitidos para la validación
               simbolos = "@#$%^&*()_+"
               # Comprueba si existe al menos una letra en la contraseña
               letras = any(letra.isalpha() for letra in password)
               # Comprueba si existe al menos una letra mayúscula en la contraseña
               mayusculas = any(letra.strip().isupper() for letra in password)
               # Comprueba si existe al menos una letra minúscula en la contraseña
               minusculas = any(letra.strip().islower() for letra in password)
               # Comprueba si existe al menos un carácter alfanumérico (letra o número)
               numeros = any (numero.isdigit() for numero in password)
               # Comprueba si existe al menos un símbolo especial en la contraseña
               caracteres_especiales = any(caracter in simbolos  for caracter in password)
               # Comprueba si la longitud de la contraseña es al menos 8 caracteres
               tamano = len(password) >= 8
               if letras and mayusculas and minusculas and numeros and caracteres_especiales and tamano:
                    # Si cumple todas las condiciones, indica que es válida
                    print(f'es valida')
                
               else:
                    # Si no cumple alguna condición, indica que no es válida
                    print(f'pass no valido')
          

# Llama a la función para ejecutar la validación de contraseñas
FilePassword()
