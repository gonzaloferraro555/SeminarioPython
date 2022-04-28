import os
import csv
ruta =os.path.realpath(".")
ruta_completa = os.path.join(ruta,"Netflix","netflix_titles.csv")
#la ruta siempre hasta el archivo, y el nombre con ".tipo".
print(ruta_completa)
archivo_netflix = open(ruta_completa,errors='ignore')
archivo_netflix_2021 = open("netflix_2021.csv","w")
writer = csv.writer(archivo_netflix_2021)
csv_reader = csv.reader(archivo_netflix, delimiter = ',')
for elem in (csv_reader):
    if "2021" in elem[6]:
        writer.writerow(elem)
archivo_netflix.close()
archivo_netflix_2021.close()










