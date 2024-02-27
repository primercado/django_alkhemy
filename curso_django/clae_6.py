# Constantes 
TIPO_COMISION = "Por Comisión"
TIPO_SUELDO_FIJO = "Salario Fijo"

# Constantes
ANTIGUEDAD_MENOS_DE_DOS = "Menos de 2 años"
ANTIGUEDAD_ENTRE_DOS_Y_CINCO = "Entre 2 y 5 años"
ANTIGUEDAD_MAS_DE_CINCO = "Más de 5 años"

class Empleado:
    def __init__(self, dni, nombre, apellido, anio_ingreso, tipo_contratacion):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anio_ingreso = anio_ingreso
        self.tipo_contratacion = tipo_contratacion

    def mostrar_salario(self):
        pass

class PorComision(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, tipo_contratacion,
                 salario_minimo, clientes_captados, importe_por_cliente):
        super().__init__(dni, nombre, apellido, anio_ingreso, tipo_contratacion)
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        self.importe_por_cliente = importe_por_cliente

    def mostrar_salario(self):
        salario_por_comision = self.clientes_captados * self.importe_por_cliente
        return max(self.salario_minimo, salario_por_comision)

class SueldoFijo(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, tipo_contratacion,
                 sueldo_basico, porcentaje_adicional, cat_antiguedad):
        super().__init__(dni, nombre, apellido, anio_ingreso, tipo_contratacion)
        self.sueldo_basico = sueldo_basico
        self.porcentaje_adicional = porcentaje_adicional
        self.cat_antiguedad = cat_antiguedad

    def mostrar_salario(self):
        porcentaje = 0
        if self.cat_antiguedad == ANTIGUEDAD_MENOS_DE_DOS:
            porcentaje = 0.05
        elif self.cat_antiguedad == ANTIGUEDAD_ENTRE_DOS_Y_CINCO:
            porcentaje = 0.10
        elif self.cat_antiguedad == ANTIGUEDAD_MAS_DE_CINCO:
            porcentaje = 0.20
        bonificacion = self.sueldo_basico * porcentaje
        return self.sueldo_basico + bonificacion# Constantes de Tipo de Contratación
TIPO_COMISION = "Por Comisión"
TIPO_SUELDO_FIJO = "Salario Fijo"

# Constantes de Categorías de Antigüedad
ANTIGUEDAD_MENOS_DE_DOS = "Menos de 2 años"
ANTIGUEDAD_ENTRE_DOS_Y_CINCO = "Entre 2 y 5 años"
ANTIGUEDAD_MAS_DE_CINCO = "Más de 5 años"

class Empleado:
    def __init__(self, dni, nombre, apellido, anio_ingreso, tipo_contratacion):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anio_ingreso = anio_ingreso
        self.tipo_contratacion = tipo_contratacion

    def mostrar_salario(self):
        pass

class PorComision(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, tipo_contratacion,
                 salario_minimo, clientes_captados, importe_por_cliente):
        super().__init__(dni, nombre, apellido, anio_ingreso, tipo_contratacion)
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        self.importe_por_cliente = importe_por_cliente

    def mostrar_salario(self):
        salario_por_comision = self.clientes_captados * self.importe_por_cliente
        return max(self.salario_minimo, salario_por_comision)

class SueldoFijo(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, tipo_contratacion,
                 sueldo_basico, porcentaje_adicional, cat_antiguedad):
        super().__init__(dni, nombre, apellido, anio_ingreso, tipo_contratacion)
        self.sueldo_basico = sueldo_basico
        self.porcentaje_adicional = porcentaje_adicional
        self.cat_antiguedad = cat_antiguedad

    def mostrar_salario(self):
        porcentaje = 0
        if self.cat_antiguedad == ANTIGUEDAD_MENOS_DE_DOS:
            porcentaje = 0.05
        elif self.cat_antiguedad == ANTIGUEDAD_ENTRE_DOS_Y_CINCO:
            porcentaje = 0.10
        elif self.cat_antiguedad == ANTIGUEDAD_MAS_DE_CINCO:
            porcentaje = 0.20
        bonificacion = self.sueldo_basico * porcentaje
        return self.sueldo_basico + bonificacion
    
    
    
# Ejemplo
empleado_comision = PorComision("12345678", "Juan", "Pérez", 2018, TIPO_COMISION, 500, 30, 20)
empleado_sueldo_fijo = SueldoFijo("87654321", "Ana", "López", 2015, TIPO_SUELDO_FIJO, 1000, 0.20, ANTIGUEDAD_MAS_DE_CINCO)

print("Salario Empleado Comisión:", empleado_comision.mostrar_salario())
print("Salario Empleado Sueldo Fijo:", empleado_sueldo_fijo.mostrar_salario())