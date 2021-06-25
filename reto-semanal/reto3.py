
usuario = ""
password = ""
dic_menu = {
    "1":"cambiar_contraseña", 
    "2":"Ingresar_coordenadas_actuales",
    "3":"Ubicar_zona_wifi_cercana",
    "4":"Guardar_archivo_ubicacion_cercana",
    "5":"Actualizar_registros_zonas_wifi_archivo",
    "6":"Elegir_opcion_menu_favorita",
    "7":"Cerrar_Sesion"
    }

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



def mostrar_menu():
    for p in dic_menu:
        print(f"{p} {dic_menu[p]}")


def menu_option(option):
    valor = dic_menu.get(str(option))

    if valor=="cambiar_contraseña":
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
                return password
            else:
                print("Error")
        else:
            print("Error")
            print("No se puede usar la misma contraseña\n")
            menu_inicial()
    else:
        print("Error")




def Ingresar_coordenadas_actuales():
    print("Ingresar coordenadas actuales".center(30,"*"))
def Ubicar_zona_wifi_cercana():
    print("Ubicar zona wifi más cercana".center(30,"*"))
def Guardar_archivo_ubicacion_cercana():
    print("Guardar archivo con ubicación cercana".center(30,"*"))
def Actualizar_registros_zonas_wifi_archivo():
    print("Actualizar registros de zonas wifi desde archivo".center(30,"*"))

    
    
    
#corregir
def Elegir_opcion_menu_favorita():
    global dic_menu
    change = int(input('Elija un favorito de la opcion 1 al 5: '))
    val = dic_menu.get(str(change))
    if change > 5 :
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
    print("Sesión cerrada".center(30,"-"))
    exit()








main()