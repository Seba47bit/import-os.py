import os
import platform

def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

campus = ["zona core", "campus uno", "campus matriz", "sector outsourcing"]

def mostrar_menu():
    print("¿Qué quiere hacer?")
    print("1. Ver los dispositivos.")
    print("2. Ver los campus.")
    print("3. Añadir dispositivo.")
    print("4. Añadir campus.")
    print("5. Borrar dispositivo.")
    print("6. Borrar campus.")
    return input("Elija una opción: ")

def mostrar_campus():
    limpiar_pantalla()
    print("Listado de Campus:")
    for i, item in enumerate(campus, 1):
        print(f"{i}. {item}")

def ver_dispositivos():
    limpiar_pantalla()
    mostrar_campus()
    try:
        seleccion = int(input("\nElija un campus: ")) - 1
        if 0 <= seleccion < len(campus):
            archivo = campus[seleccion] + ".txt"
            if os.path.exists(archivo):
                with open(archivo, "r") as file:
                    print(f"\nDispositivos en {campus[seleccion]}:\n")
                    print(file.read())
            else:
                print("\nNo se encontraron dispositivos registrados en este campus.")
        else:
            print("Selección inválida.")
    except ValueError:
        print("Por favor, introduzca un número válido.")
        
def agregar_dispositivo():
    limpiar_pantalla()
    mostrar_campus()
    try:
        seleccion = int(input("\nElija un campus donde agregar el dispositivo: ")) - 1
        if 0 <= seleccion < len(campus):
            archivo = campus[seleccion] + ".txt"
            servicios = []
            
            tipo_dispositivo = input("\nElija un dispositivo:\n1. Router\n2. Switch\n3. Switch multicapa\nOpción: ")
            
            nombre_dispositivo = input("Ingrese el nombre del dispositivo: ")
            
            while True:
                confirmar = input(f"¿Confirma el nombre '{nombre_dispositivo}'?\n1. Si\n2. No\nOpción: ")
                if confirmar == "1":
                    break
                else:
                    nombre_dispositivo = input("Ingrese nuevamente el nombre del dispositivo: ")
            
            jerarquia = input("Elija una jerarquía:\n1. Núcleo\n2. Distribución\n3. Acceso\nOpción: ")

            if tipo_dispositivo == "1":
                print("Seleccione servicios para el Router:\n1. Enrutamiento\n2. Salir")
            elif tipo_dispositivo == "2" or tipo_dispositivo == "3":
                print("Seleccione servicios:\n1. Datos\n2. VLAN\n3. Trunking\n4. Enrutamiento (Solo Switch multicapa)\n5. Salir")

            while True:
                servicio = input("Elija una opción de servicio: ")
                if servicio == "5":
                    break
                if servicio == "1":
                    servicios.append("Datos")
                elif servicio == "2":
                    servicios.append("VLAN")
                elif servicio == "3":
                    servicios.append("Trunking")
                elif servicio == "4" and tipo_dispositivo == "3":
                    servicios.append("Enrutamiento")
                elif servicio == "4" and tipo_dispositivo != "3":
                    print("Opción no válida para el tipo de dispositivo.")
            
            with open(archivo, "a") as file:
                file.write(f"Dispositivo: {nombre_dispositivo}\n")
                file.write(f"Jerarquía: {jerarquia}\n")
                file.write(f"Servicios: {', '.join(servicios)}\n")
                file.write("-" * 30 + "\n")
            print(f"Dispositivo '{nombre_dispositivo}' agregado a {campus[seleccion]}.\n")
        else:
            print("Selección inválida.")
    except ValueError:
        print("Por favor, introduzca un número válido.")

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            ver_dispositivos()
        elif opcion == "2":
            mostrar_campus()
        elif opcion == "3":
            agregar_dispositivo()
        elif opcion == "4":
            print("Funcionalidad no implementada aún.")  
        elif opcion == "5":
            print("Funcionalidad no implementada aún.")  
        elif opcion == "6":
            print("Funcionalidad no implementada aún.")  
        elif opcion == "salir":
            break
        else:
            print("Opción no válida.")
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
