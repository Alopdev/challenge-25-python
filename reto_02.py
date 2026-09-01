""" Reto 2 — Control de gastos

Crea un programa para llevar tus gastos mensuales.

Debe permitir:

Añadir un gasto: descripción, categoría y cantidad.
Ver todos los gastos.
Calcular cuánto has gastado en total.
Calcular cuánto has gastado por categoría.
Salir.

Nivel: parecido al"""
meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12]
gastos_mes = []
gasto ={} #gasto sería un diccionario que tendría todos los gastos
categorias = ["Ocio", "Hogar", "Banco", "Alimentacion"]

def define_categoría():
    categories = input("Escoge una categoría: Ocio, Hogar, Banco o Alimentación :\n")
    if categories.title() in categorias:
        return categories.title()
    else:
        print("No existe esa categoría")
        define_categoría()


def add_gastos():
    descripcion = input("Concepto de gasto: ")
    categoria = define_categoría()
    cantidad = int(input("Cantidad: "))
    gasto = {"Decripción: ": descripcion, "Categoría: ": categoria, "Cantidad": cantidad}
    return(gasto)

def gasto_mes(gasto):
    mes = int("Introduce el mes en el que se ha producido el gasto (del 1 al 12): ")
    if mes >=1 and mes <=12:
        gasto_mes[mes-1].append(add_gastos)
    else:
        print("No existe ese mes")
        gasto_mes()
gastador = add_gastos()
gasto_mes(gastador)
print(gasto_mes[0])