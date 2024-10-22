# main.py

from Gestion_ERP import crear_empresa, agregar_empleado, Empresa

def mostrar_menu():
    print("\nOpciones:")
    print("1. Agregar un empleado")
    print("2. Calcular el coste total de los empleados")
    print("3. Listar información de los empleados")
    print("4. Salir")

def main():
    empresa = crear_empresa()
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            agregar_empleado(empresa)
        elif opcion == '2':
            coste = empresa.calcular_coste_total()
            print(f"\nEl coste total de todos los empleados es: {coste}€")
        elif opcion == '3':
            print("\nLista de empleados:")
            empresa.listar_empleados()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
