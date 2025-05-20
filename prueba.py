
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
        contador_item += 1
        items.append(item)
        if contador_item == 3 :
             break

for item in items:
    print(item)
print('total de unidades: ', cant_total)
print('total del presupuesto = ',precio_total_pres)
