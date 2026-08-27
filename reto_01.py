""" Imagina que trabajas en un hotel y necesitas llevar un registro sencillo de incidencias.

Crea un programa que permita:

Añadir una incidencia.
Ver todas las incidencias pendientes.
Marcar una incidencia como resuelta.
Ver cuántas incidencias quedan pendientes.

Cada incidencia tendrá:

descripción
habitación
estado (pendiente / resuelta)
--- GESTOR DE INCIDENCIAS ---

1. Añadir incidencia
2. Ver incidencias
3. Resolver incidencia
4. Ver incidencias resueltas
5. Salir

Elige una opción:
"""

#Gestor incidencia hotel


#Crear una incidencia a modo diccionario y que se añada a una lista

#Eliminar de la lista la incidencia realizada y pasarla a una lista nueva
#salir 

list_incidencias = []
list_resueltas =[]
incidencia = {}
salir = False
#Pedir que quiere hacer el usuario y que escoja una opción


#función para crear un diccionario de una incidencia
def add_incidencia(description, num_hab, estado = False):
    incidencia = {"Descripción": description, "Habitación": num_hab, "Estado":estado}
    return incidencia


#Recorrer lista incidencias para mostrarlas
def mostrar_incidencias(lista):
    for incidencias in list_incidencias:
        print(incidencias)

#resolver una incidencia, quitarla de la lista y ponerla en otra pidiendo el número de habitación
def resolver_incidencia (num_habitacion):
    for incidencia in list_incidencias:
        if num_habitacion == incidencia["Habitación"]:
            incidencia["Estado"]= True
            list_resueltas.append(incidencia)
            list_incidencias.remove(incidencia)
            print("Incidencia resuelta")
            break
    else:
        print("No hay incidencias en esa habitación")


while not salir:
    opcion= int(input("""¡Buenas!
        ¿Que quieres hacer?
        1. Añadir incidencia
        2. Ver incidencias
        3. Resolver una incidencia
        4. Ver incidencias resueltas
        5. Salir
        """))

    if opcion == 1:
        descripcion = input("Describe la Avería: ")
        habitacion = input("Dime número de habitación: ")
        incidencia = add_incidencia(descripcion, habitacion)
        list_incidencias.append(incidencia)
    elif opcion == 2:
        mostrar_incidencias(list_incidencias)

    elif opcion == 3:
        room = int(input("¿Qué numero de habitación has arreglado"))
        resolver_incidencia(room)

    elif opcion == 4:
        mostrar_incidencias(list_resueltas)

    elif opcion == 5:
        salir =True

    else:
        print("Esa opción no existe")