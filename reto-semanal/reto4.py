
import numpy as np

usuario = ""
password = ""
dic_menu = {
    "1":"cambiar_contrasena", 
    "2":"Ingresar_coordenadas_actuales",
    "3":"Ubicar_zona_wifi_cercana",
    "4":"Guardar_archivo_ubicacion_cercana",
    "5":"Actualizar_registros_zonas_wifi_archivo",
    "6":"Elegir_opcion_menu_favorita",
    "7":"Cerrar_Sesion"
    }
ing_coordenadas = []
lista_trabajo=[]
lista_casa=[]
lista_parque = []
mt_coord = np.array(0)


def main():
    if sing_up():
        login(usuario, password)




    #(Reto Semanal 1)-RE01
def sing_up():
    """
    *Se imprime la bienvenida
    *Se genera dos input: 
    1) input usuario = string de un numero
    2) input password = string de el numero usuario en reversa
    """

    #se pone global aqui para poder modificar las variables que estan afuera
    global usuario 
    global password

    print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
    print("*".center(70,"*"))
    usuario=str(input("Ingrese Nombre de Usuario: "))
    if len(usuario) == 5:
        password=str(input("Ingrese contraseña: "))
        return usuario,password
        
    else:
        print("Error")
        print("Porfavor digite usuario y clave de 5 digitos")
        #Usa una funcion recursiva y se vuelve a llamar asi mismo
        sing_up()



#(Reto Semanal 1)-RE02,RE03,RE04
def login(usr, psw):
    """
    RE02:
    Este login recive el input usuario y password y verifica
    si los dos datos de 6 digitos son iguales y redirecciona al menu inicial.
    Si no imprime **Error**

    RE03:
    *El captcha sera el resultado de la suma de dos terminos:
    
    terminos:
    1) Ultimos 3 digitos del usuario
    2) Penultimo numero del usuario

    RE04:
    Mostrar en pantalla Sesion iniciada
    """

    u = usr
    # Convierte Str en Int y se imprime desde la posicion -1
    p = psw[::-1]
    # Convierte Str en Int y arranca de la posicion 3 hasta la 1 en forma inversa
    ultimos_tres = int(usr[2::1])
    # Convierte Str en Int y arranca de la posicion 5 hasta la 1
    ultimo = int(usr[4::1])

    if ultimo == 0:
        ultimo = int(usr[3::2])

    
    res = int(ultimo + ultimos_tres)
    
    
    if u == p:
        print("Captcha".center(30,"*"))
        print("".center(30,"*"))
        respuesta_usuario = int(input(f"""
        {ultimos_tres}+{ultimo}:{res}
        type the answer:"""))
        if res == respuesta_usuario:
            print("Sesión iniciada".center(30,"-"))
            menu_inicial()
        else:
            print("Error")
    else:
        print("Error")



#(Reto Semanal 2)-RE01
def menu_inicial():
    """
    RE01:
    """
    mostrar_menu()

    acumulador = 1
    while acumulador <= 3:
        #Option to select the option
        option = int(input('Elija una opción del menu: '))
        print(f"Usted ha elegido la opción {option}")
        if option in range(1,8):
            if option == 6:
                Elegir_opcion_menu_favorita()
            elif option == 7:
                Cerrar_Sesion()
            else:
                menu_option(option)
                acumulador = 4
        else:
            #Usa una funcion recursiva y se vuelve a llamar asi mismo
            print("Error")
            if acumulador ==3:
                print("Sesion terminada")
                exit()
            acumulador +=1



def capchat_adivina():
    q_uno = ("""Para confirmar por favor responda:
                                        Si me giras pierdo tres unidades
                                        por eso debes colocarme siempre 
                                        de pie”: """)
    q_dos = ("""Para confirmar por favor responda:
                                        Si estoy a la derecha algo valgo,
                                        pero a la izquierda soy nada: """)
    question_one = int(input(q_uno))
    if question_one == 9:
        question_two = int(input(q_dos))
        if question_two == 0:
            return True
        else:
            print("Error")
            menu_inicial()
    else:
        print("Error")



def mostrar_menu():
    for p in dic_menu:
        print(f"{p} {dic_menu[p]}")


def menu_option(option):
    valor = dic_menu.get(str(option))

    if valor=="cambiar_contrasena":
        cambiar_contrasena(password)
    elif valor=="Ingresar_coordenadas_actuales":
        Ingresar_coordenadas_actuales()
    elif valor=="Ubicar_zona_wifi_cercana":
        Ubicar_zona_wifi_cercana()
    elif valor=="Guardar_archivo_ubicacion_cercana":
        Guardar_archivo_ubicacion_cercana()
    elif valor=="Actualizar_registros_zonas_wifi_archivo":
        Actualizar_registros_zonas_wifi_archivo()
    else:
        print("Error")
        print("No existe esa opción")
        menu_inicial()



def cambiar_contrasena(password):
    print("cambiando contraseña".center(30,"*"))

    pass_uno = input("Introduce contraseña actual: ")
    if pass_uno == password:
        pass_dos = input("Introduce nueva contraseña: ")
        if pass_dos != password:
            pass_tres = input("Confirma la nueva contraseña: ")
            if pass_dos == pass_tres:
                password = pass_dos
                print(f"contraseña cambiada con exito {password}")
                menu_inicial()
            else:
                print("Error")
        else:
            print("Error")
            print("No se puede usar la misma contraseña\n")
            menu_inicial()
    else:
        print("Error")




def Ingresar_coordenadas_actuales():
    #6.689, -72.873


    global ing_coordenadas
    global mt_coord
    

    def rango_latitud(lat):
        if lat > 6.600 and lat < 6.700:
            return True
        else:
            return False
    def rango_longitud(lon):
        if lon < -72.800 and  lon > -72.900:
            return True
        else:
            return False


    def validator_ll(latitud):
        if latitud != 0 and rango_latitud(latitud) == True:
            longitud=float(input("Ingresa longitud: "))
        else:    
            print("Error coordenada")
            exit()
        return latitud,longitud
    

    def actualizar_coordenada(latitud):
        if latitud != 0 and rango_latitud(latitud) == True:
            longitud=float(input("Ingresa longitud: "))
        else:    
            print("Error actualización")
            exit()
        return latitud, longitud
    

    #Coordenada mas al norte
    def coordenada_x_mas_alta():
        #almacena toda la matriz
        npCoord = np.array(mt_coord)

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
            
        return f'coordenada [latitud,longitud] {posMayor+1}: {mt_coord[posMayor]}'


    #Coordenada mas al sur
    def coordenada_x_mas_baja():
        #almacena toda la matriz
        npCoord = np.array(mt_coord)

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
            
        return f'coordenada [latitud,longitud] {posMayor+1}: {mt_coord[posMayor]}'


    #Coordenada mas al oriente
    def coordenada_y_mas_baja():
        n = -1
        #almacena toda la matriz
        npCoord = np.array(mt_coord)

        #almacena eje x o latitudes
        latitudes = npCoord[:,0] * n

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
        posMayor * n
            
        return f'coordenada [latitud,longitud] {posMayor+1}: {mt_coord[posMayor]}'

    #Coordenada mas al occidente
    def coordenada_y_mas_alta():
        n = -1
        #almacena toda la matriz
        npCoord = np.array(mt_coord)

        #almacena eje y o longitudes
        longitudes = npCoord[:,1] * n

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
        posMayor * n
        return f'coordenada [latitud,longitud] {posMayor+1}: {mt_coord[posMayor]}'

        
    if ing_coordenadas:

        opt = int(input(f"""
        Coordenada mas al norte:
        {coordenada_x_mas_alta()}
        Coordenada mas al sur:
        {coordenada_x_mas_baja()}
        Coordenada mas al oriente:
        {coordenada_y_mas_baja()}
        Coordenada mas al occidente:
        {coordenada_y_mas_alta()}
        Presione 1,2 o 3 para actualizar la respectiva coordenadas
        presione 0 para regresar al menu:

        """))

        if opt > 3:
            print("Error actualización")
            exit()
        else: 
            global lista_casa
            global lista_parque
            global lista_trabajo
 
            if opt == 0:
                menu_inicial()
            elif opt == 1:
                print("Coordenadas Trabajo".center(30,"-"))
                trabajo_latitud=float(input("Ingresa latitud: "))
                lista_trabajo = actualizar_coordenada(trabajo_latitud)
                
            elif opt == 2:
                print("Coordenadas Casa".center(30,"-"))
                casa_latitud=float(input("Ingresa latitud: "))
                lista_casa = actualizar_coordenada(casa_latitud)
                
            elif opt == 3:
                print("Coordenadas Parque".center(30,"-"))
                parque_latitud=float(input("Ingresa latitud: "))
                lista_parque = actualizar_coordenada(parque_latitud)

    else: 
        print("Coordenadas Trabajo".center(30,"-"))
        trabajo_latitud=float(input("Ingresa latitud: "))
        lista_trabajo = validator_ll(trabajo_latitud)    

        print("Coordenadas Casa".center(30,"-"))
        casa_latitud=float(input("Ingresa latitud: "))
        lista_casa = validator_ll(casa_latitud)
                
        print("Coordenadas Parque".center(30,"-"))
        parque_latitud=float(input("Ingresa latitud: "))
        lista_parque = validator_ll(parque_latitud)
    
    ing_coordenadas = lista_trabajo,lista_casa,lista_parque
    
    mt_coord = np.array(ing_coordenadas)
    print(mt_coord)
    menu_inicial()


    



        
    

def Ubicar_zona_wifi_cercana():
    if ing_coordenadas:
        question = int(input("Choose option"))
        if question == 80:
            print("Error ubicación")
    else:
        print("Error sin registro de coordenadas")



def Guardar_archivo_ubicacion_cercana():
    if Ubicar_zona_wifi_cercana() == True:
        print("Guardar archivo con ubicación cercana".center(30,"*"))
    else:
        print("Error sin registro de coordenadas")


def Actualizar_registros_zonas_wifi_archivo():
    print("Actualizar registros de zonas wifi desde archivo".center(30,"*"))

    
    

def Elegir_opcion_menu_favorita():
    global dic_menu
    change = int(input('Elija un favorito de la opcion 1 al 5: '))
    val = dic_menu.get(str(change))
    if change > 5 or change < 0:
        print("Error")
    else:
        res = capchat_adivina()
        if res == True:
            dic_menu = {**dic_menu,"1":val}
            dic_menu = {**dic_menu,str(change):"cambiar_contraseña"}
            menu_inicial()
        else:
            print("Error")

def Cerrar_Sesion():
    print("Hasta pronto")
    exit()








main()