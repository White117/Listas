#Metodos utilizados 
#mostrar_lista
#buscar_valor
#eliminar_valor



def eliminar_valor(lista):
    if len(lista) == 0:
        print("La lista está vacía.")
    else:
        valor_eliminar = input("Ingrese el valor que desea eliminar: ")
        if valor_eliminar in lista:
            lista.remove(valor_eliminar)
            print(f"El valor '{valor_eliminar}' ha sido eliminado de la lista.")
        else:
            print(f"El valor '{valor_eliminar}' no se encuentra en la lista.")

def ingresar_valores():
    valores = input("Ingrese los valores separados por comas: ")
    lista = valores.split(",")
    return lista

def mostrar_lista(lista):
    if len(lista) == 0:
        print("La lista está vacía.")
    else:
        print("Elementos de la lista:")
        print(", ".join(lista))

def buscar_valor(lista):
    if len(lista) == 0:
        print("La lista está vacía.")
    else:
        valor_buscar = input("Ingrese el valor que desea buscar: ")
        if valor_buscar in lista:
            print(f"El valor '{valor_buscar}' se encuentra en la lista.")
        else:
            print(f"El valor '{valor_buscar}' no se encuentra en la lista.")



# Uso de los métodos
mi_lista = ingresar_valores()
print()
mostrar_lista(mi_lista)
print()
buscar_valor(mi_lista)
print()
eliminar_valor(mi_lista)
print()
mostrar_lista(mi_lista)