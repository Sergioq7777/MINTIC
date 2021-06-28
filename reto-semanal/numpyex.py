import numpy as np

matriz = [
    [21,56], 
    [34,35], 
    [47,48]
]
matriz_np = np.array(matriz)


def coordenada_x_mas_alta():
        res = np.amax(matriz, axis=0)
        res2 = np.amax(res, axis=0)
        return res2


def coordenada_x_alta():
    #almacena toda la matriz
    npCoord = np.array(matriz)

    #almacena eje x o latitudes
    latitudes = npCoord[:,0]

    #posicion mayor empieza desde cero
    posMayor = 0
    #latMayor en la posicion 0 de latitudes 
    latMayor = latitudes[posMayor]


    j = 0
    for i in latitudes:
        if i > latMayor:
            latMayor = i
            posMayor = j
        j += 1
    return matriz_np[posMayor]

def coordenada_y_alta():
    #almacena toda la matriz
    npCoord = np.array(matriz)

    #almacena eje y o longitudes
    longitudes = npCoord[:,1]

    #posicion mayor empieza desde cero
    posMayor = 0
    #latMayor en la posicion 0 de latitudes 
    latMayor = longitudes[posMayor]


    j = 0
    for i in longitudes:
        if i > latMayor:
            latMayor = i
            posMayor = j
        j += 1
    return matriz_np[posMayor]


def coordenada_x_baja():
    #almacena toda la matriz
    npCoord = np.array(matriz)

    #almacena eje x o latitudes
    latitudes = npCoord[:,0]

    #posicion mayor empieza desde cero
    posMayor = 0
    #latMayor en la posicion 0 de latitudes 
    latMayor = latitudes[posMayor]


    j = 0
    for i in latitudes:
        if i < latMayor:
            latMayor = i
            posMayor = j
        j += 1
    return matriz_np[posMayor]

def coordenada_y_baja():
    #almacena toda la matriz
    npCoord = np.array(matriz)

    #almacena eje y o longitudes
    longitudes = npCoord[:,1]

    #posicion mayor empieza desde cero
    posMayor = 0
    #latMayor en la posicion 0 de latitudes 
    latMayor = longitudes[posMayor]


    j = 0
    for i in longitudes:
        if i < latMayor:
            latMayor = i
            posMayor = j
        j += 1
    return matriz_np[posMayor]





def buscar_menor():
    distanciaMenor = 0
    posicionMenor = 0


    j = 0
    for i in matriz:
        operacion = (i[0] - i[1])
        if operacion < distanciaMenor:
            distanciaMenor = operacion
            posicionMenor = j
        j +=1

    return matriz_np[posicionMenor]




print(coordenada_x_alta())
print(coordenada_y_alta())
print(coordenada_x_baja())
print(coordenada_y_baja())



#print(matriz_np)
#print(matriz)

#Imprimir la columna

#print(matriz_np[:,0])
#print(matriz_np[:,1])
#print(matriz_np[:,2])

#Imprimir Filas
#print(matriz_np[0][0])
#print(matriz_np[0][1])
#print(matriz_np[0][2])


#Imprimir en especifico
#print(matriz_np[1][1])
#print(matriz_np[1][3])



