import numpy as np

def buscar_menor(coordena, wifis):
    distanciaMenor = (coordena[0]-coordena[1] +(wifis[0,0] - wifis[0,1]))
    posicionMenor = 0
    index = 0
    for i in wifis:
        
        operacion = (coordena[0]-coordena[1] + (i[0] - i[1]))
        if operacion < distanciaMenor:
            distanciaMenor = operacion
            posicionMenor = index
        index +=1

    return posicionMenor



wifis = [
    
    [25,15],
    [54,45],
    [32,23],
    [12,24]
]
npWifis = np.array(wifis)

coordena = [10,20]
resultado = buscar_menor(coordena,npWifis)
print(resultado)