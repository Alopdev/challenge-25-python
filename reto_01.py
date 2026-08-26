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

#Pedir que quiere hacer el usuario y que escoja una opción
opcion= input("""¡Buenas!
    ¿Que quieres hacer?
    1. Añadir incidencia
    2. Ver incidencias
    3. Resolver una incidencia
    4. Ver incidencias resueltas
    5. Salir
    """)

#función para crear un diccionario de una incidencia
def add_incidencia(description, num_hab, estado):
    incidencia ={"Descripción": description, "Habitación": num_hab, "Estado":estado}
    #return print(incidencia)


#Recorrer lista incidencias para mostrarlas
def mostrar_incidencias(lista):
    for incidencias in lista:
        print(incidencias)

#resolver una incidencia, quitarla de la lista y ponerla en otra pidiendo el número de habitación
def resolver_incidencia (num):
    for incidencia in list_incidencias:
        if 

