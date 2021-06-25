
def Elegir_opcion_menu_favorita():
    return "hola"

def cambiar_contrasena():
    return "hola"

def Ingresar_coordenadas_actuales():
    return "hola"
def Ubicar_zona_wifi_cercana():
    return "hola"
def Guardar_archivo_ubicacion_cercana():
    return "hola"
def Actualizar_registros_zonas_wifi_archivo():
    return "hola"

def Cerrar_Sesion():
    return "sesion cerrada"

dic_menu = {
    "1":{"cambiar_contraseña":cambiar_contrasena()}, 
    "2":{"Ingresar_coordenadas_actuales":Ingresar_coordenadas_actuales()},
    "3":{"Ubicar_zona_wifi_cercana":Ubicar_zona_wifi_cercana()},
    "4":{"Guardar_archivo_ubicacion_cercana":Guardar_archivo_ubicacion_cercana()},
    "5":{"Actualizar_registros_zonas_wifi_archivo":Actualizar_registros_zonas_wifi_archivo()},
    "6":{"Elegir_opcion_menu_favorita":Elegir_opcion_menu_favorita()},
    "7":{"Cerrar_Sesion":Cerrar_Sesion()}
    }

def executa(opt):    
    for i, j in dic_menu.items():
        if opt == i:
            return j
    return "theres is no such key"


def mostrar_menu():
    for p in dic_menu:
        for c in dic_menu[p]:
            #print(f"{p} {c}:{dic_menu[p][c]}")
            print(f"{p} {c}")


#n = str(input("type a option"))
#print(executa(n))
mostrar_menu()