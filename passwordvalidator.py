import re
def Password():
   password = input("ingrese una password valida:").strip()
   print(f"Probando con: '{password}' (Longitud: {len(password)})")
   reg = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#%])[A-Za-z\d@$#%]{6,20}$'
   patron = re.fullmatch(reg, password)
   if patron:
      print(f'pass valida')
   else:
      print(f'pass no valida')

Password()         