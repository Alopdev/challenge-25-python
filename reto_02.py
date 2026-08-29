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

cat = define_categoría()   
print(cat)

def add_gastos(descripcion, categoría, cantidad):
    descripcion = input("Concepto de gasto: ")
    categoría = define_categoría()
    cantidad = int(input("Cantidad: "))
    gasto = {"Decripción: ": descripcion, "Categoría: ": categoría, "Cantidad": cantidad}