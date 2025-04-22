# # Ejercicio 2: Intersección de Listas
# # Escribir una función que reciba dos listas y devuelva una nueva lista con los elementos
# #  comunes entre ambas (sin repetir).

# def listas(lista_1,lista_2):
  
    
#     return lista_1,lista_2

# print(listas(["perro, foca, caballo"], ["ballena, foca, tiburon"]))


# # def listas(lista_1,lista_2):
# #     lista_1="perro, foca, caballo"
# #     lista_2="ballena, foca, tiburon"
# #     resultado=lista_1 + " " + lista_2
# #     return lista_1,lista_2

# # print(listas(["perro, foca, caballo"], ["ballena, foca, tiburon"]))




empleados={
    "carolina":44,
    "cristian":32,
    "julian":15
}

edades ={}

def clasificar (diccionario):
    for clave,valor in diccionario.items():
        if valor<13:
            edades.update("niños",valor)
            print(edades)
        elif valor>60:
            edades.update("Mayor",valor)
            print(edades)
        else:
            edades.updates("Adulto",valor)
            print(edades)