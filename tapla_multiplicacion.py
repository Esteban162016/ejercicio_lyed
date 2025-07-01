def tabla_multiplicar (numero):
    '''Multiplica cada numero ingresado del 1 al 10 y los retorna en una lista'''
    resultados = []
    for iterador in range (1,11):
        resultados.append(iterador*numero)
    return resultados   #### este resultado es local, esta dentro de la funcion

### PROGRAMA PRINCIPAL
print('Por favor Guada, ingresa que numero queres la tabla')
desde = int(input('Valor desde: ' ))
hasta = int(input('Valor hasta: ' ))
for valor in range(desde,hasta+1):
    print('\nLa tabla del', valor, 'es: ')
    resultados_global = tabla_multiplicar(valor)
    for contador, respuesta in enumerate(resultados_global): ### enumerate sirve para contar las vueltas del for
        print(valor, 'x', contador+1, '=', respuesta )




