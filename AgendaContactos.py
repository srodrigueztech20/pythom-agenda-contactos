
def mostrar_menu():
    print("\nAgenda de Contactos:")
    print("1.- Agregar Nuevo Contacto")
    print("2.- Eliminar contacto existente")
    print("3.- Buscar Contacto")
    print("4.- Lista de Contactos")
    print("5.- Salir")
    print("\n")
    
# ----------- Funcion Agregar -----------------
    
def agregar_contacto(agenda):
    nombre = input("Introduzca el nombre completo: ").capitalize()
    telefono = input("Introduzca el teléfono del contacto: ")
    email = input("Introduzca el mail del contacto: ")
    
    agenda[nombre] = {"telefono":telefono, "email": email}
    
    print(f"Se ha agregado el contacto {nombre} exitosamente!")
 
 # ----------- Funcion Eliminar -----------------
    
def eliminar_contacto(agenda):
    nombre = input("Introduzca el nombre de la agenda que desea eliminar: ").capitalize()
    
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto {nombre} ha sido eliminado!!!")
    else:
        print(f"No se ha encontrado el contacto {nombre}") 
    
    
# -------------  Funcion Buscar -----------------
    
def buscar_contacto(agenda):
    nombre = input("Ingrese el contacto que desea buscar: ").capitalize()
    
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"No se ha encontrado el contacto {nombre} en la agenda") 
        
# ---------------  Funcion Listar --------------------
    
def listar_contactos(agenda):
    if agenda:
        print("\nLista de Contactos: ")

        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info['telefono']}")
            print(f"Email: {info['email']}")
            print("-" * 20)
    else:
        print("La agenda esta vacía!!!")       
        
        
# ----------- Funcion Central / Agenda -----------------
    
def agenda_contactos():
    agenda = {}
    
    while True:
        mostrar_menu()
        opcion = input("Elija una Opcion: ")
        
        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            break
        else:
            print("Elija una opcion valida (1 a 5)")
            
agenda_contactos()
