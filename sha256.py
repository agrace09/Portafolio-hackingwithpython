import hashlib, random,string


def Random_Password():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    long = input('ingrese la longitud de su password:')
    longitud_defecto = 8
    try:
        Password = ''.join(random.choice(caracteres) for _ in range(int(long)))
        return Password
    except ValueError:
         Password = ''.join(random.choice(caracteres) for _ in range(longitud_defecto))
         return Password
print(f"su pass es : {Random_Password()}")
         


