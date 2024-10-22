# %% 1. Cabecera
"""
Autor: Rubén Cereceda
Clase: Diseño de Interfaces
"""
# %% 2. Importar Módulos
from abc import ABC, abstractmethod

# %% 3. Clases

class Empleado(ABC):
    def __init__(self, nombre, telefono, edad, id_empleado):
        self.nombre = nombre
        self.telefono = telefono
        self.edad = edad
        self.id_empleado = id_empleado
         
    @abstractmethod
    def pago(self):
        """Calcula el pago del empleado"""
        pass

    @abstractmethod
    def informacion(self):
        """Devuelve la información del empleado"""
        pass

class EmpleadoAsalariado(Empleado):
    def __init__(self, nombre, telefono, edad, id_empleado, sueldo):
        super().__init__(nombre, telefono, edad, id_empleado)
        self.sueldo = sueldo
        
    def pago(self):
        return self.sueldo
    
    def informacion(self):
        return (f"ID: {self.id_empleado}, Nombre: {self.nombre}, Edad: {self.edad}, "
                f"Teléfono: {self.telefono}, Tipo: Asalariado, Sueldo: {self.sueldo}€")

class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, telefono, edad, id_empleado, precio_hora, numero_horas):
        super().__init__(nombre, telefono, edad, id_empleado)
        self.precio_hora = precio_hora
        self.numero_horas = numero_horas
        
    def pago(self):
        return self.precio_hora * self.numero_horas
    
    def informacion(self):
        return (f"ID: {self.id_empleado}, Nombre: {self.nombre}, Edad: {self.edad}, "
                f"Teléfono: {self.telefono}, Tipo: Temporal, Precio por hora: {self.precio_hora}€, "
                f"Número de horas: {self.numero_horas}")

class Empresa:
    def __init__(self, nombre, ubicacion, telefono):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.telefono = telefono
        self.empleados = []
        
    def agregar_empleado_asalariado(self, nombre, telefono, edad, id_empleado, sueldo):
        empleado = EmpleadoAsalariado(nombre, telefono, edad, id_empleado, sueldo)
        self.empleados.append(empleado)
        
    def agregar_empleado_temporal(self, nombre, telefono, edad, id_empleado, precio_hora, numero_horas):
        empleado = EmpleadoTemporal(nombre, telefono, edad, id_empleado, precio_hora, numero_horas)
        self.empleados.append(empleado)
        
    def calcular_coste_total(self):
        return sum(empleado.pago() for empleado in self.empleados)
        
    def listar_empleados(self):
        if not self.empleados:
            print("No hay empleados en la empresa.")
            return
        for empleado in self.empleados:
            print(empleado.informacion())

# %% 4. Funciones generales

def crear_empresa():
    print("\nPara crear la empresa necesitamos varios datos.")
    
    nombre = input("\nDime cuál será el nombre de la empresa: ")
    ubicacion = input("Dime la ubicación de la empresa: ")
    
    while True:
        telefono = input("Dime el teléfono de la empresa: ")
        if len(telefono) == 9 and telefono.isdigit():
            print("Teléfono registrado correctamente.")
            break
        else:
            print("El número de teléfono debe tener 9 dígitos numéricos. Inténtalo de nuevo.")
    
    empresa = Empresa(nombre, ubicacion, telefono)
    
    print("\nEmpresa creada exitosamente:")
    print(f"Nombre: {empresa.nombre}")
    print(f"Ubicación: {empresa.ubicacion}")
    print(f"Teléfono: {empresa.telefono}")
    
    return empresa  # Retornamos la instancia por si se desea usar luego

def agregar_empleado(empresa):
    print("\nSelecciona el tipo de empleado a agregar:")
    print("1. Asalariado")
    print("2. Temporal")
    tipo = input("Introduce el número correspondiente: ")
    
    nombre_empleado = input("Dime cuál será el nombre del empleado: ")
    
    while True:
        telefono_empleado = input("Dime cuál es el teléfono del empleado: ")
        if len(telefono_empleado) == 9 and telefono_empleado.isdigit():
            print("Teléfono registrado correctamente.")
            break 
        else:
            print("El teléfono debe tener exactamente 9 dígitos numéricos. Inténtalo de nuevo.")
    
    edad_empleado = input("Introduce la edad del empleado: ")
    id_empleado = input("Introduce el ID del empleado: ")
    
    if tipo == '1':
        while True:
            sueldo = input("Introduce el sueldo mensual del empleado: ")
            try:
                sueldo = float(sueldo)
                break
            except ValueError:
                print("Por favor, introduce un número válido para el sueldo.")
        empresa.agregar_empleado_asalariado(nombre_empleado, telefono_empleado, edad_empleado, id_empleado, sueldo)
    elif tipo == '2':
        while True:
            precio_hora = input("Introduce el precio por hora: ")
            try:
                precio_hora = float(precio_hora)
                break
            except ValueError:
                print("Por favor, introduce un número válido para el precio por hora.")
        while True:
            numero_horas = input("Introduce el número de horas trabajadas: ")
            try:
                numero_horas = float(numero_horas)
                break
            except ValueError:
                print("Por favor, introduce un número válido para el número de horas.")
        empresa.agregar_empleado_temporal(nombre_empleado, telefono_empleado, edad_empleado, id_empleado, precio_hora, numero_horas)
    else:
        print("Tipo de empleado no válido.")
        return
    
    print(f"Empleado {nombre_empleado} agregado exitosamente.")
    print(f"Número total de empleados: {len(empresa.empleados)}")