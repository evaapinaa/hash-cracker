import hashlib
import string
import time

palabras = []

def pantalla():
    banner = r"""
           ___ ____      ___               _             
  /\/\    /   \ ___|    / __\ __ __ _  ___| | _____ _ __ 
 /    \  / /\ /___ \   / / | '__/ _` |/ __| |/ / _ \ '__|
/ /\/\ \/ /_// ___) | / /__| | | (_| | (__|   <  __/ |   
\/    \/___,' |____/  \____/_|  \__,_|\___|_|\_\___|_|    
                                                                                           
    """

    print("="*60)
    print(banner)
    print("="*60)
    

# Cargar diccionario con contraseñas más comunes
def cargarDiccionario(archivo="rockyou.txt"):
    try:
        with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
            palabras = [linea.strip() for linea in f if linea.strip()]
        print(f"Diccionario cargado: {len(palabras)} palabras")
        return palabras
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}")
        return []
    except Exception as e:
        print(f"Error al cargar el diccionario: {e}")
        return []

# Generar hash MD5
def generarHashMD5(palabra):
    return hashlib.md5(palabra.encode()).hexdigest()

# Función recursiva para generar todas las posibles combinaciones
def generarCombinaciones(letras, longitud, actual=""):
    if len(actual) == longitud:
        yield actual
        return
    
    for letra in letras:
        yield from generarCombinaciones(letras, longitud, actual + letra)
    
# Probar todas las combinaciones posibles
def fuerzaBruta(longitud, hashObjetivo):
    letras = string.printable.strip()
    longitud = int(longitud)
    tiempoInicio = time.time()
    
    for i in range(1, longitud + 1):
        
        for combinacion in generarCombinaciones(letras, i):
            hashCombinacion = generarHashMD5(combinacion)
            
            print(f"Probando: {combinacion}")
            
            if hashCombinacion == hashObjetivo:
                print("----Hash encontrado!!----")
                print(f"Palabra: {combinacion}")
                print(f"Hash: {hashCombinacion}")
                print(f"Tiempo: {time.time() - tiempoInicio}\n")
                return combinacion
    
    print("No se ha encontrado\n")          
    return None

# Hacer hash de cada palabra, y las comparas
def ataqueDiccionario(hashObjetivo):
    palabras = cargarDiccionario()
    tiempoInicio = time.time()
    for palabra in palabras:
        hashPalabra = generarHashMD5(palabra)
        
        if hashPalabra == hashObjetivo:
            print("----Hash encontrado!!----")
            print(f"Palabra: {palabra}")
            print(f"Hash: {hashPalabra}")
            print(f"Tiempo: {time.time() - tiempoInicio}\n")
            return palabra
    
    print("No se ha encontrado en el diccionario\n")
    return None



if __name__ == "__main__":

    pantalla()
    
    while True:

        print("1 - Ataque de Diccionario")
        print("2 - Fuerza Bruta")
        print("3 - Salir del programa")
        opcion = input("Seleccione la opción que desee: ")
        
        if opcion == "1":
            hashToCrack = input("\nIntroduce el hash a crackear: ")
            ataqueDiccionario(hashToCrack)
        
        elif opcion == "2":
            longitud = input("\nIntroduce la longitud máxima que desee probar: ")
            hashToCrack = input("\nIntroduce el hash a crackear: ")
            fuerzaBruta(longitud, hashToCrack)
    
        elif opcion == "3":
            print("\nAdiós")
            break
        
        else:
            print("\nEsa tecla no es válida, jeje\n")
        
    