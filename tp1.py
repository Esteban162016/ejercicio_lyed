### Hacer un programa que permita registrar los datos de un presupuesto para un cliente de mi empresa
### El operador debe ingresar fecha de presupuesto, que debe ser valida
### También nombre del cliente
### Los presupuestos deben ser enumerados desde el 1
### Se pueden ingresar varios presupuestos con una ejecucion del programa, se termina el programa cuando no se ingresa fecha o cliente alguno
### Cada presupuesto consta de un maximo de tres Items 
### Cada intems se componen de detalle de texto, una cantidad y un precio unitario
### Cualquier elemento vacio del items da como terminado ese presupuesto
### Al finalizar el programa se debe mostrar los presupuestos ingresados
### Cada presupuesto debera estar encabezado por la fecha y el nombre del cliente, un pie con la cantidad de las unidades y el precio total

presupuestos = []
numero_presupuesto = 1
from datetime import date

while True:

    print('*'*40)
    print('Presupuesto N°: ', numero_presupuesto)
    print('*'*40)

    cliente = input('Ingrese nombre de cliente: ')
    if not cliente:
        break    
    
    while True:
        try:
            dia = int(input('Ingrese día: '))
        except:
            print('Día Inválido')
            continue
        try:
            mes = int(input('Ingrese mes: '))
        except:
            print('Mes invalido')
            continue
        try:
            anio = int(input('Ingrese año: '))
        except:
            print('Año invalido')
            continue
        try:
            fecha_ingresada = date(anio, mes, dia)
            break
        except ValueError:
            print('Fecha Invalida')
            continue
    items = []
    contador_item = 0 
    cant_total = 0
    precio_total_item = 0
    precio_total_pres = 0 
    while contador_item <=3:
        
        detalle = input('ingrese detalle: ')
        if not detalle:
            break
        try:
            cantidad = int(input('Ingrese cantidad: '))
            valor = float(input('Ingrese el valor unitario:  '))
        except ValueError:
            print('dato invalido')
            continue
        item = {  
        'detalle ': detalle,
        'cantidad': cantidad,
        'valor unitario': valor,
        }
        cant_total = cant_total + cantidad
        precio_total_item = cantidad * valor
        precio_total_pres = precio_total_item + precio_total_pres
        
        items.append(item)
        contador_item += 1
        if contador_item == 3:
            break

    
    presupuesto = numero_presupuesto,  fecha_ingresada, cliente, items, cant_total, precio_total_pres
    presupuestos.append(presupuesto)
    numero_presupuesto += 1

print('='*40)
print('    Presupuestos ingresados: ', numero_presupuesto - 1)
print('='*40)
for presupuesto in presupuestos:
    print('Presupuesto N°', presupuesto[0])
    print('Fecha:', presupuesto[1])
    print('Cliente:', presupuesto[2])
    print('items:', presupuesto[3]) 
    print('-' * 35)
    print('Cantidad de unidades:', presupuesto[4])   
    print('-' * 35)
    print('Precio Total = $', presupuesto[5])
    print('-' * 40)
    print('-' * 40)
print('='*40)
