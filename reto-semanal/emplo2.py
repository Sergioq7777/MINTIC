import numpy as np

wifis = [
    
    [6.629,72.873],
    [6.699,72.866],
    [6.669,72.899]
]
npWifis = np.array(wifis)


def buscar_menor(wifis):
    distanciaMenor = (wifis[0,0] - wifis[0,1])
    print(f'distanciaMenor: {wifis[0,0]}-{wifis[0,1]} = {distanciaMenor}')
    posicionMenor = 0


    j = 0
    for i in wifis:
        operacion = (i[0] - i[1])
        print(f'operacion:{i[0]}-{i[1]} = {operacion}')
        if operacion < distanciaMenor:
            distanciaMenor = operacion
            posicionMenor = j
        j +=1

    return npWifis[posicionMenor]







print(buscar_menor(npWifis))