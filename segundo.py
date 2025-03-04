import numpy as np

class Estudiante:
    def __init__(self, codigo, nombre, promedio, carrera, ingreso):
        self.codigo = codigo
        self.nombre = nombre
        self.promedio = promedio
        self.carrera = carrera
        self.ingreso = ingreso

estudiantes = [
    Estudiante('1001', 'Juan Perez', 4.2, 'SIS', 1985),
    Estudiante('1002', 'Ana Gomez', 3.8, 'SIS', 1992),
    Estudiante('1003', 'Luis Martinez', 4.5, 'ELE', 1988),
    Estudiante('1004', 'Maria Rojas', 3.0, 'SIS', 1987),
    Estudiante('1005', 'Carlos Ruiz', 4.1, 'SIS', 1995),
    Estudiante('1006', 'Laura Diaz', 4.0, 'ELE', 1990),
    Estudiante('1007', 'Pedro Castro', 3.1, 'IND', 1993),
    Estudiante('1008', 'Sofia Lopez', 2.7, 'SIS', 1989),
    Estudiante('1009', 'Miguel Torres', 3.6, 'ELE', 1991),
    Estudiante('1010', 'Elena Vargas', 4.4, 'IND', 1986),
    Estudiante('1011', 'Jorge Nunez', 3.5, 'SIS', 1994),
    Estudiante('1012', 'Carmen Soto', 3.1, 'ELE', 1984),
    Estudiante('1013', 'Ricardo Mora', 3.4, 'IND', 1996),
    Estudiante('1014', 'Patricia Rios', 4.7, 'SIS', 1983),
    Estudiante('1015', 'Fernando Castro', 3.0, 'ELE', 1997),
]

def filtrar_cra_y_prom(carrera, estudiantes):
    promedios = np.array([est.promedio for est in estudiantes])
    carreras = np.array([est.carrera for est in estudiantes])
    
    indices_filtrados = np.where((carreras == carrera) & (promedios >= 4))[0]
    
    filtrados = [estudiantes[i] for i in indices_filtrados]
    
    for est in filtrados:
        print(est.codigo, est.nombre)
    
    print(len(filtrados))
    return filtrados

carrera = 'SIS'
primer_punto = filtrar_cra_y_prom(carrera, estudiantes)

def filtar_ingreso_y_cond(ingreso, estudiantes):
    ingresos = np.array([est.ingreso for est in estudiantes])
    promedios = np.array([est.promedio for est in estudiantes])
    
    indices_filtrados = np.where((ingresos < ingreso) & (promedios < 3.2))[0]
    
    filtrados = [estudiantes[i] for i in indices_filtrados]
    
    for est in filtrados:
        print(est.codigo, est.nombre)
    return filtrados

ingreso = 1990
segundo_punto = filtar_ingreso_y_cond(ingreso, estudiantes)