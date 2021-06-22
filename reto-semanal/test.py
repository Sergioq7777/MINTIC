"""
num = int(str(12345)[1::])
print(num)
"""
"""
def pen_ultimo(serial):
    for i in serial:
        num = int(i)
        pen = num-1

    return pen    

def ultimos_tres(serial):
    for i in serial:
        tres = int(i[-3:])
    print(tres)
    return tres


#(Reto Semanal 1)-RE03
def captcha(num_usr):
    
    *El captcha sera el resultado de la suma de dos terminos:

    terminos:
    1) Ultimos 3 digitos del usuario
    2) Penultimo numero del usuario


    termino_uno = Ticnec.ultimos_tres(num_usr)
    termino_dos = Ticnec.pen_ultimo(num_usr)

    suma_terminos = termino_uno + termino_dos
    print(f'{termino_uno}+{termino_dos}={suma_terminos}')
    
    return suma_terminos
"""    

        
    def contador():
        conta = 1
        while conta <= 3:
            ask = int(input("Type option: "))
            if ask == 6:
                print("correcto")
                conta = 4
            else:
                print("Respuesta incorrecta")
                if conta == 3:
                    print("comunicate con el admin")
                conta +=1

    

contador()