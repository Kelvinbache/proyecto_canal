import os 


os.chdir("canal")

print("direccion actual: " + os.getcwd())

lista = os.listdir()

print(lista)