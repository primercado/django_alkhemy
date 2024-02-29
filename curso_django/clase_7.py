# Enumeración para los tipos de instrumentos
from enum import Enum

class TipoInstrumento(Enum):
    VIENTO = "Viento"
    CUERDAS = "Cuerdas"
    PERCUSION = "Percusión"

# Clase Instrumento
class Instrumento:
    def __init__(self, id_alfanumerico, precio, tipo):
        self.id_alfanumerico = id_alfanumerico
        self.precio = precio
        self.tipo = tipo

    def __str__(self):
        return f"ID: {self.id_alfanumerico}, Precio: {self.precio}, Tipo: {self.tipo.value}"

# Clase Sucursal
class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []

    def agregarInstrumento(self, instrumento):
        self.instrumentos.append(instrumento)

# Clase Fabrica
class Fabrica:
    def __init__(self):
        self.sucursales = []

    def agregarSucursal(self, sucursal):
        self.sucursales.append(sucursal)

    def listarInstrumentos(self):
        for sucursal in self.sucursales:
            print(f"Instrumentos en sucursal {sucursal.nombre}:")
            for instrumento in sucursal.instrumentos:
                print(instrumento)

    def instrumentosPorTipo(self, tipo):
        instrumentos_tipo = []
        for sucursal in self.sucursales:
            for instrumento in sucursal.instrumentos:
                if instrumento.tipo == tipo:
                    instrumentos_tipo.append(instrumento)
        return instrumentos_tipo

    def borrarInstrumento(self, id_alfanumerico):
        for sucursal in self.sucursales:
            sucursal.instrumentos = [instrumento for instrumento in sucursal.instrumentos if instrumento.id_alfanumerico != id_alfanumerico]

    def porcInstrumentosPorTipo(self, nombre_sucursal):
        for sucursal in self.sucursales:
            if sucursal.nombre == nombre_sucursal:
                total = len(sucursal.instrumentos)
                if total == 0:
                    return {tipo: 0 for tipo in TipoInstrumento}
                conteo = {tipo: 0 for tipo in TipoInstrumento}
                for instrumento in sucursal.instrumentos:
                    conteo[instrumento.tipo] += 1
                porcentajes = {tipo: (count / total) * 100 for tipo, count in conteo.items()}
                return porcentajes
        return None

# Ejemplo de uso
fabrica = Fabrica()

# Crear sucursales
sucursal1 = Sucursal("Sucursal Central")
sucursal2 = Sucursal("Sucursal Norte")

# Agregar sucursales a la fábrica
fabrica.agregarSucursal(sucursal1)
fabrica.agregarSucursal(sucursal2)

# Agregar instrumentos
sucursal1.agregarInstrumento(Instrumento("ID001", 1000, TipoInstrumento.VIENTO))
sucursal1.agregarInstrumento(Instrumento("ID002", 1500, TipoInstrumento.CUERDAS))
sucursal2.agregarInstrumento(Instrumento("ID003", 750, TipoInstrumento.PERCUSION))

# Listar instrumentos
fabrica.listarInstrumentos()

# Obtener instrumentos por tipo
instrumentos_cuerdas = fabrica.instrumentosPorTipo(TipoInstrumento.CUERDAS)
for instr in instrumentos_cuerdas:
    print(instr)

# Borrar un instrumento
fabrica.borrarInstrumento("ID002")

# Porcentaje de instrumentos por tipo en una sucursal
porcentajes = fabrica.porcInstrumentosPorTipo("Sucursal Central")
print(porcentajes)
