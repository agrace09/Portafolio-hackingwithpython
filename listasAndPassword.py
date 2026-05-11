# Importa la librería hashlib para encriptar contraseñas con SHA1
import hashlib
# Importa la librería requests para hacer peticiones HTTP a la API
import requests


def list_pass():
    # Abre el archivo 'userdate.txt' en modo escritura y crea su contenido
    with open('userdate.txt', 'w') as f:
        # Escribe una lista de contraseñas separadas por comas
        f.write('Admin123,12345,root,agrace093494')
    
    # Abre el archivo 'userdate.txt' en modo lectura
    with open('userdate.txt', 'r') as f:
        # Itera sobre cada línea del archivo
        for line in f:
            # Elimina espacios en blanco y divide la línea por comas para obtener cada contraseña
            datos = line.strip().split(',')

            # Itera sobre cada contraseña de la lista
            for password in datos:
                # Elimina espacios en blanco de la contraseña
                password = password.strip()
                # Si la contraseña está vacía, salta a la siguiente iteración
                if not password:
                    continue
                # Encripta la contraseña con SHA1 y la convierte a mayúsculas
                sha1_password = hashlib.sha1(password.encode('utf8')).hexdigest().upper()
                # Divide el hash SHA1 en los primeros 5 caracteres (prefix) y el resto (sufix)
                prefix, sufix = sha1_password[:5], sha1_password[5:]
                # Construye la URL para consultar la API 'Have I Been Pwned' usando el prefix
                url = f"https://api.pwnedpasswords.com/range/{prefix}"
                # Realiza una solicitud GET a la API
                res = requests.get(url)
                # Verifica si la solicitud fue exitosa (código 200)
                if res.status_code != 200:
                    # Si hay error, imprime un mensaje y retorna 0
                    print("error al consultar api")
                    return 0
                else:
                    # Si la solicitud fue exitosa, imprime un mensaje confirmando
                    print('All ok:200')
                # Crea un generador que divide cada línea de la respuesta por ':' para obtener hash y count
                hashes = (line.split(':') for line in res.text.splitlines())
                # Itera sobre cada hash y su cantidad de ocurrencias en la base de datos
                encontrada = False
                for h, count in hashes:
                    # Compara si el suffix del hash coincide con alguno de la API
                    if h == sufix:
                        # Si coincide, imprime que la contraseña ha sido comprometida
                        print(f'tu pass({h}) ha sido comprometida')
                        encontrada = True
                        break   
                if not encontrada:
                        print(f'tu password, no ha sido filtrada')
                        
                   
    # Si ninguna contraseña fue encontrada en las filtraciones, imprime este mensaje
    print("Todo ok, contraseña no encontrada en filtraciones.")
    # Retorna 0 indicando que no hubo coincidencias
    return 0

# Llama la función para ejecutar el programa
list_pass()





