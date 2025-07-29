import os 
import shutil

#Que vamos a hacer:
# Vamos a crear un programa que permita al usuario gestionar archivos y directorios de manera sencilla
# El programa tendrá un menú interactivo que permitirá al usuario elegir entre varias opciones
# Las opciones incluirán crear, mover, renombrar y eliminar archivos, así como crear directorios
# Utilizaremos funciones para organizar el código y hacerlo más legible y mantenible

def createFile(ruta, contenido):
    rutas = os.path.join(os.getcwd(), ruta)

    with open(rutas, "w") as f:
        f.write(contenido)
    print("el archivo se creo exictosamente:", ruta)   

def createCaper(ruta):
    if not os.path.exists(ruta):
        os.mkdir(ruta)
        print("se creo exictosamente:", ruta)
    else:
        print("este archivo ya exite")   

def moverCT(ruta_actual, nueva_ruta):
    if os.path.exists(ruta_actual):
        shutil.move(ruta_actual, nueva_ruta)
        print("se cambio de ruta")
    else:
        print("este ruta no existe: ", ruta_actual)          

def eliminar(ruta):
    if os.path.exists(ruta):
       os.remove(ruta)
       print("el archivo se elimino exitosamente: ", ruta)
    else:
       print("el archivo no exite: ", ruta)     

def renombrar(nombre_actual, nuevo_nombre):
    if os.path.exists(nombre_actual):
       os.rename(nombre_actual, nuevo_nombre)
       print("El nombre del archivo se cambio con exicto: ", nuevo_nombre)
    else:
       print("Este archivo no exicte: ", nombre_actual)     


# Bucle 
while True:
    print("1 create file")
    print("2 create carpeta")
    print("3 mover")
    print("4 eliminar")
    print("5 renombrar")
    print("0 salir")
    select = int(input("Que quieres hacer: "))
   
    if select == 1:
       ruta = input("ruta del archivo: ")
       contenido = input("Pon el contenido del archivo: ")
       createFile(ruta, contenido)
     
    elif select == 2:
         ruta = input("ruta del archivo: ")
         createCaper(ruta)
    
    elif select == 3:
         ruta_actual = input("Dime la ruta actual del archivo: ")
         nueva_ruta = input("Dime la nueva ruta del archivo: ")
         moverCT(ruta_actual, nueva_ruta)

    elif select == 4:
        ruta = input("ruta del archivo: ")
        eliminar(ruta)

    elif select == 5:
         nombre_actual = input("Dime la ruta actual del archivo: ")
         nuevo_nombre = input("Dime la nueva ruta del archivo: ")
         renombrar(nombre_actual, nuevo_nombre)

    elif select == 0:
        print("Salir del programa")
        break