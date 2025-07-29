import os 
import shutil


def crear_archivo(ruta, contenido):
    rutas = os.path.join(os.getcwd(), ruta)
    print(rutas)

    with open(rutas, "w") as f:
        f.write(contenido)
    print(f"Archivo creado en {ruta}")

def mover_archivo(ruta_origen, ruta_destino):
    shutil.move(ruta_origen, ruta_destino)
    print(f"Archivo movido de {ruta_origen} a {ruta_destino}")

def renombrar_archivo(ruta_actual, nuevo_nombre):
    nuevo_ruta = os.path.join(os.path.dirname(ruta_actual), nuevo_nombre)
    os.rename(ruta_actual, nuevo_ruta)
    print(f"Archivo renombrado a {nuevo_nombre}")

def eliminar_archivo(ruta):
    if os.path.exists(ruta):
        os.remove(ruta)
        print(f"Archivo {ruta} eliminado")
    else:
        print(f"El archivo {ruta} no existe")

def crear_directorio(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)
        print(f"Directorio {ruta} creado")
    else:
        print(f"El directorio {ruta} ya existe")

while True:         

      print("1. Crear un archivo")
      print("2. Mover un archivo")
      print("3. Renombrar un archivo")
      print("4. Eliminar un archivo")
      print("5. crear un directorio")
      print("0. Salir")
      selection = int(input("Que deseas realizar?: "))

      if selection == 1: 
         ruta = input("Ingresa la ruta del archivo a crear: ")
         contenido = input("Ingresa el contenido del archivo: ")
         crear_archivo(ruta, contenido)
    
      elif selection == 2:
           ruta_origen = input("Ingresa la ruta del archivo a mover: ")
           ruta_destino = input("Ingresa la nueva ruta del archivo: ")
           mover_archivo(ruta_origen, ruta_destino)
     
      elif selection == 3:
           ruta_actual = input("Ingresa la ruta del archivo a renombrar: ")
           nuevo_nombre = input("Ingresa el nuevo nombre del archivo: ")
           renombrar_archivo(ruta_actual, nuevo_nombre) 

      elif selection == 4:
           ruta = input("Ingresa la ruta del archivo a eliminar: ")
           eliminar_archivo(ruta)

      elif selection == 5:
            ruta_directorio = input("Ingresa la ruta del directorio a crear: ")
            crear_directorio(ruta_directorio)     

      elif selection == 0:
           print("Saliendo del programa...")
           break
