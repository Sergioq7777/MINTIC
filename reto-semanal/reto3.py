

def cambiar_contraseña():
    print("cambiando contraseña".center(30,"*"))
def Ingresar_coordenadas_actuales():
    print("Ingresar coordenadas actuales".center(30,"*"))
def Ubicar_zona_wifi_cercana():
    print("Ubicar zona wifi más cercana".center(30,"*"))
def Guardar_archivo_ubicacion_cercana():
    print("Guardar archivo con ubicación cercana".center(30,"*"))
def Actualizar_registros_zonas_wifi_archivo():
    print("Actualizar registros de zonas wifi desde archivo".center(30,"*"))

#(Reto Semanal 2)-RE01
def menu_inicial():
    """
    RE01:
    """
    
    list_num = [1,2,3,4,5,6,7]
    list_options = [
        "Cambiar contraseña", "Ingresar coordenadas actuales", 
        "Ubicar zona wifi más cercana", "Guardar archivo con ubicación cercana",
        "Actualizar registros de zonas wifi desde archivo", "Elegir opción de menú favorita",
        "Cerrar sesión"
        ]
    #First step show the options in a list
   
    def print_menu(lis1, lis2):
        print("MENU DE INICIO".center(30,"*"))
        i =1
        j=1
        for i,j in zip(lis1,lis2):
            print(i,j)
    

    print_menu(list_num, list_options)
    




    acumulador = 1
    while acumulador <= 3:
        #Option to select the option
        option = int(input('Elija una opción del menu: '))
        if option in range(1,8):
            if option == 6:
                    change = int(input('Elija un favorito de la opcion 1 al 5: '))
                    if change > 5 :
                            print("Error")
                            break
                    else:
                        res = capchat_adivina()
                        if res == True:
                            a = list_options[change]
                            del list_options[change]
                            list_options.insert(0,a)


                            print_menu(list_num, list_options)
                            o = int(input('Elija una opción del menu: '))
                            print(f"o= {o}")
                            menu_option(o)
                            break
                        else:
                            print("Error")
                            break
            elif option == 7:
                print("Hasta pronto")
                print("Sesión cerrada".center(30,"-"))
                exit()
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
                                        Me separaron de mi hermano siamés, 
                                        antes era un ocho y ahora soy un...”
                                        : """)
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
    



def menu_option(option):

    print(f"Usted ha elegido la opción {option}")

    if option==1:
        cambiar_contraseña()
    elif option==2:
        Ingresar_coordenadas_actuales()
    elif option==3:
        Ubicar_zona_wifi_cercana()
    elif option==4:
        Guardar_archivo_ubicacion_cercana()
    elif option==5:
        Actualizar_registros_zonas_wifi_archivo()
    else:
        print("Error")
        print("No existe esa opción")
        menu_inicial()


#(Reto Semanal 1)-RE02,RE03,RE04
def login(user, passw):
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

    u = int(user) 
    # Convierte Str en Int y se imprime desde la posicion -1
    p = int(passw[::-1])
    

    # Convierte Str en Int y arranca de la posicion 3 hasta la 1 en forma inversa
    ultimos_tres = int(user[2::1])
    # Convierte Str en Int y arranca de la posicion 5 hasta la 1
    ultimo = int(user[4::1])

    if ultimo == 0:
        ultimo = int(user[3::2])
  
    
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





#(Reto Semanal 1)-RE01
def sing_up():
    """
    *Se imprime la bienvenida
    *Se genera dos input: 
    1) input usuario = string de un numero
    2) input password = string de el numero usuario en reversa
    """

    print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
    print("*".center(70,"*"))
    usuario=str(input("Ingrese Nombre de Usuario: "))
    if len(usuario) == 5:
        password=str(input("Ingrese contraseña: "))
        login(usuario,password)
    else:
        print("Error")
        print("Porfavor digite usuario y clave de 5 digitos")
        #Usa una funcion recursiva y se vuelve a llamar asi mismo
        sing_up()
    
    



sing_up()