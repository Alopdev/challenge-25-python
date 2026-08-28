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


#Declaración de Variables y listas 
list_incidencias = []
list_resueltas =[]
incidencia = {}
salir = False
id = 0



#función para crear un diccionario de una incidencia
def add_incidencia(id, description, num_hab, estado = False):
    incidencia = {"ID" : id, "Descripción": description, "Habitación": num_hab, "Estado":estado}
    return incidencia


#Mostrar listado de incidencias y arreglos
def mostrar_listado(lista):
    for incidencias in lista:
        print(incidencias)


#resolver incidencia y generando lista averías resueltas
def resolver_incidencia (num_habitacion, identificador):
    for incidencia in list_incidencias:
        if num_habitacion == incidencia["Habitación"] and identificador == incidencia["ID"]:
            incidencia["Estado"]= True
            list_resueltas.append(incidencia)
            list_incidencias.remove(incidencia)
            print("Incidencia resuelta")
            break
    else:
        print("No hay incidencias en esa habitación")

print("¡Bienvenido/a a tu aplicación de incidencias!")
#Pedir que quiere hacer el usuario y que escoja una opción. No se sale hasta que el usuario lo escoja
while not salir:#Hasta que esto no sea true el usuario sigue en la aplicacion
    opcion= int(input("""
        ¿Que quieres hacer ahora?
        1. Añadir incidencia
        2. Ver incidencias
        3. Resolver una incidencia
        4. Ver incidencias resueltas
        5. Salir
        """))

    if opcion == 1:
        id +=1#Le doy un ID a cada incidencia para diferenciarlo por si hay dos averías misma habitación
        descripcion = input("Describe la Avería: ")
        habitacion = int(input("Dime número de habitación: "))
        incidencia = add_incidencia(id, descripcion, habitacion)
        list_incidencias.append(incidencia)

    elif opcion == 2:
        mostrar_listado(list_incidencias)

    elif opcion == 3:#Podría pedir únicamente el id pero queda como más seguro
        room = int(input("¿Qué numero de habitación has arreglado? "))
        identificador = int(input("¿Que ID de avería tiene?"))
        resolver_incidencia(room, identificador)

    elif opcion == 4:
        mostrar_listado(list_resueltas)

    elif opcion == 5:
        #Al cambia de valor Salir, el programa sale del bucle
        salir =True
        print("Hasta pronto")

    else:
        print("Esa opción no existe")