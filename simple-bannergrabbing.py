# ============================================================================
# SCRIPT DE BANNER GRABBING - Detecta banners y vulnerabilidades en puertos
# ============================================================================
# Este script realiza un escaneo de red para:
# 1. Conectarse a múltiples hosts en un rango especificado
# 2. Intentar acceso a puertos comunes
# 3. Obtener el "banner" (información del servidor) de cada conexión exitosa
# 4. Comparar banners contra una base de datos de vulnerabilidades conocidas
# ============================================================================

import socket, sys  # socket: para conexiones TCP/IP, sys: para argumentos de línea de comandos

# Validación: verificar que se pasó el argumento necesario
if len(sys.argv) < 2:
    print("Uso: python simple-bannergrabbing.py <porcion_de_red>")
    print("Ejemplo: python simple-bannergrabbing.py 192.168.1")
    sys.exit(1)

# Crear un socket TCP/IP
# AF_INET = usar IPv4
# SOCK_STREAM = usar protocolo TCP
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# BUCLE 1: Iterar sobre los hosts (10 y 11)
# Esto permite escanear múltiples máquinas en la red
# Ejemplo: si sys.argv[1] es "192.168.1", escanea:
#   - 192.168.1.10
#   - 192.168.1.11
for host in range(10, 12):
    
    # Abrir archivo con lista de puertos a escanear
    ports = open('ports.txt', 'r')
    
    # Abrir archivo con banners conocidos como vulnerables
    vulnbanners = open('vulnbanners.txt', 'r')
    
    # BUCLE 2: Iterar sobre cada puerto en la lista
    for port in ports:
        try:
            # Construir la dirección IP: concatenar argumento + octeto actual
            target_host = str(sys.argv[1]) + '.' + str(host)
            target_port = int(port.strip())
            
            # Intentar conectar al host en el puerto especificado
            socket.connect((target_host, target_port))
            
            # Si la conexión es exitosa, imprimir información
            print('Connecting to ' + target_host + ' on port ' + port.strip())
            
            # Recibir datos del servidor (máximo 1024 bytes)
            # Esto es el "banner" - información que el servidor envía al conectar
            banner = socket.recv(1024)
            
            # BUCLE 3: Comparar el banner recibido contra vulnerabilidades conocidas
            for vulnbanner in vulnbanners:
                # Si el banner coincide con alguno de los banners vulnerables registrados
                if banner.strip() in vulnbanner.strip():
                    # Alerta: vulnerable detectada
                    print('we have a match! ' + banner.strip() + ' is vulnerable to ' + vulnbanner.strip())
        
        except:
            # Si no hay conexión (puerto cerrado o no accesible), imprimir aviso
            print('Port ' + port.strip() + ' is closed on ' + str(sys.argv[1]) + '.' + str(host))
            pass