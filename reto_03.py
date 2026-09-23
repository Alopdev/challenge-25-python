""" Para el reto 3: Gestor de entrenamientos.

Objetivo: crear un programa donde puedas registrar entrenamientos, consultar el historial, calcular estadísticas y buscar entrenamientos por tipo.

Pero vamos a hacerlo como los anteriores: te doy los requisitos, no la solución.

Añadir entrenamiento: fecha, tipo (Bici, Carrera, Natación, Gimnasio), duración y distancia.
Ver todos los entrenamientos.
Calcular tiempo total entrenado.
Calcular distancia total por tipo de entrenamiento.
Buscar entrenamientos por tipo.
Salir.

Dificultad: un pequeño salto respecto al reto 2, sobre todo por trabajar mejor con datos relacionados entre sí."""
type_train = ["Bici", "Carrera", "Natacion", "Gimnasio"]
#funciones para simplificar función añadir entrenamiento
def date_train():
    print("Introduce la fecha del entrenamiento (DD/MM/YYYY)")
    dia =int(input("Introduce el día: "))
    mes = int(input("Introduce el mes: "))
    anio= int(input("Introduce el año: "))
    fecha = f"{dia:02d}/{mes:02d}/{anio}"
    if (0 < dia and dia < 32) and (0 < mes and mes < 13):
        return fecha
    else:
        print("Has puesto mal el mes o el día")
        return(date_train())
    

def tipo_entrenamiento():
    tipo = input("Tipo de entrenamiento: Bici, Carrera, Natacion o Gimnasio ")
    if tipo.title() in type_train:
        return tipo.title()
    else:
        print("Ese estrenamiento no existe ")
        return(tipo_entrenamiento())




#función para añdir el entrenamiento
"""def add_train():
    fecha =input("Introduce la fecha del entrenamiento DD/MM/YYYY: ")"""
    




#función para calcular tiempo total entrenado
#función para calcular distancia total por tipo de entrenamiento
#función mostrar entrenamientos por tipo
#Bucle app con la opción de salir