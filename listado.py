poblacion = open("/home/esteban/Escritorio/Logica y Estructura de datos/poblacion/poblacion_identificada_provincia_agosto_2024.csv", "r")
poblacion.readline()  # leo la linea 1 para ignorarla
lista_poblacion = poblacion.readlines()  # leo el resto del archivo("")
poblacion.close() # cierro el archivo
total_habitantes = 0  # inicializo el total de habitantes
provincias = set()

for linea in lista_poblacion: # iterando cada elemento de la lista
    datos = linea.split(",")  # separar la línea por comas
    cantidad_habitantes = int(datos[6]) # obtener la cantidad de habitantes de cada renglón
    total_habitantes = total_habitantes + cantidad_habitantes  # sumar la cantidad de habitantes al total
    
    #provincia = datos[1].strip()
    #provincias.add(provincia) 
    
    provincias.add(datos[1].strip())# es lo mismo que hacer lo anterior

provincias = sorted(provincias)   
 
cantidad = 0
for p in provincias:
    print(p)
    cantidad += 1
print('cantidad de provincias: ', cantidad)
print(f"Total de habitantes: {total_habitantes:,}")
