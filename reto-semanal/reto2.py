class Ticnec:

    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password

        
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

    def cerrar_sesión():
        print("cerrar sesión".center(30,"*"))
    
    def menu_inicial():
        option = int(input('''
        1. Cambiar contraseña
        2. Ingresar coordenadas actuales
        3. Ubicar zona wifi más cercana
        4. Guardar archivo con ubicación cercana
        5. Actualizar registros de zonas wifi desde archivo
        6. Elegir opción de menú favorita
        7. Cerrar sesión

        Elija una opción: 
        '''))
        if option > 0 and option < 8:
            Ticnec.menu_option(option)
        else:
            #Usa una funcion recursiva y se vuelve a llamar asi mismo
            Ticnec.menu_inicial()

    def menu_option(option):
        if option==1:
            Ticnec.cambiar_contraseña()
        elif option==2:
            Ticnec.Ingresar_coordenadas_actuales()
        elif option==3:
            Ticnec.Ubicar_zona_wifi_cercana()
        elif option==4:
            Ticnec.Guardar_archivo_ubicacion_cercana()
        elif option==5:
            Ticnec.Actualizar_registros_zonas_wifi_archivo()
        elif option==6:
            Ticnec.cerrar_sesión()
        else:
            print("No existe esa opción")

    
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
        ultimos_tres = int(user[3::1])
        # Convierte Str en Int y arranca de la posicion 5 hasta la 1
        ultimo = int(user[5::1])


        res = int(ultimo + ultimos_tres)
        
       
        if u == p:
            print("Captcha".center(30,"*"))
            print("".center(30,"*"))
            respuesta_usuario = int(input(f"""
            {ultimos_tres}+{ultimo}:{res}
            type the answer:"""))
            if res == respuesta_usuario:
                print("Sesión iniciada".center(30,"*"))
                Ticnec.menu_inicial()
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
    
        print("Bienvenido al sistema de ubicación para zonas públicas WIFI".center(70,"*"))
        print("*".center(70,"*"))
        usuario=str(input("Ingrese nombre de usuario : "))
        if len(usuario) == 6:
            password=str(input("Ingrese password: "))
            usuario1 = Ticnec.login(usuario,password)
        else:
            print("Porfavor digite usuario y clave de 6 digitos")
            #Usa una funcion recursiva y se vuelve a llamar asi mismo
            Ticnec.sing_up()
        
        


if __name__ == '__main__':
    Ticnec.sing_up()