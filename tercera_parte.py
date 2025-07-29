import shutil 
import os

# #asi podemos crear archivos
# with open("canal_2/segunda_parte/demofile.txt", "w") as f:
#   f.write("Woops! I have deleted the content!")

# #asi podemos mover estos archivos
# shutil.move("canal_2/segunda_parte/demofile.txt", "./demofile.txt")

# #ahora cambiar el nombre al archivo 
os.rename("./demofile.txt", "canal_2/segunda_parte/demofile_new.txt")