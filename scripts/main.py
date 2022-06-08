from estructuras.ListaCircularDobleEnlazada import  ListaCircularDE

lista = ListaCircularDE()

if __name__ == "__main__":
    opcion = True
    a = input("Ingrese un numero"+"\n")
    lista.append(a)
    while opcion:
        continuar = input("Desea continuar ingresando numeros? y/n"+"\n")
        if continuar == 'y':
            a = input("Ingrese un numero"+"\n")
            lista.append(a)
        else:
            break
    seleccionado = input("Ingrese un numero"+"\n")
    dato = lista.getDato(seleccionado)
    print("anterior: " + dato.anterior.dato + " actual: "  + dato.dato + " siguiente: " + dato.siguiente.dato )
else:
    print("Nombre del modulo: " + __name__)


