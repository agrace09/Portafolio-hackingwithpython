import random  # Importa el módulo random para generar números aleatorios
import string  # Importa el módulo string para acceder a constantes de cadenas (aunque no se usa en este código)

def Generador(password):  # Define una función llamada Generador que toma un parámetro 'password'
    lista_pass = []  # Inicializa una lista vacía para almacenar las contraseñas generadas
    for i in password:  # Itera sobre cada carácter en la cadena 'password' (aunque 'i' no se usa dentro del bucle)
      caracteres_posibles = '@#$%'  # Define una cadena con caracteres especiales para reemplazar
      list_cadena = list(password)  # Convierte la cadena 'password' en una lista de caracteres
      indice_a_cambiar = random.randint(0, len(list_cadena) -1)  # Genera un índice aleatorio dentro del rango de la lista
      list_cadena[indice_a_cambiar] = random.choice(caracteres_posibles)  # Reemplaza el carácter en el índice aleatorio con un carácter especial aleatorio
      resultado = ''.join(list_cadena)  # Une la lista de caracteres de vuelta en una cadena
      lista_pass.append(resultado)  # Agrega la cadena modificada a la lista de contraseñas
    print(lista_pass)  # Imprime la lista de contraseñas generadas (fuera del bucle, por lo que se ejecuta una vez al final de la función)     

Generador('camilo')  # Llama a la función Generador con la cadena 'camilo' como argumento
