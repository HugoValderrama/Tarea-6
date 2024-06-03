lista = []

while True:
    print("")
    print("1) Ingresar un elemento a la lista")
    print("2) Modificar un elemento de la lista según el Índice")
    print("3) Eliminar un elemento de la lista según el  Índice")
    print("4) Eliminar el último elemento de la lista")
    print("5) Buscar un elemento de la lista según el dato (devuelve el índice)")
    print("6) Mostrar todos los elementos de la lista")
    print("7) Salir (Finalizar programa)")
    print("")
    opcion = int(input("Ingrese la operación que desea realizar: "))

    if opcion < 1 and opcion > 7:
        print("")
        print("Opción no reconocida. Por favor, intende nuevamente.")

    elif opcion == 1:
        print("")
        indice = input("Ingrese dato deseado a añadir: ")
        lista.append(indice)

    elif opcion == 2:
        print("")
        indice = input("Ingrese índice del elemento a modificar: ")
        if indice.isdigit():
            indice = int(indice)
            if 0 <= indice < len(lista):
                nuevo_dato = input("Ingrese nuevo dato: ")
                lista[indice] = nuevo_dato
            else:
                print("Índice fuera de rango.")
        else:
            print("Índice no válido. Por favor, intente nuevamente.")

    elif opcion == 3:
        print("")
        indice = (input("Ingrese índice del elemento a eliminar deseado: "))
        if indice.isdigit():
            indice = int(indice)
            if 0 <= indice < len(lista):
                lista.pop(indice)
            else:
                print("Índice fuera de rango.")
        else:
            print("Índice no válido. Por favor, intente nuevamente.")

    elif opcion == 4:
        print("")
        if lista:
            lista.pop(-1)
        else:
            print("La lista está vacía.")

    elif opcion == 5:
        buscar = input("Ingrese el dato que desea buscar: ")
        if buscar in lista:
            indice = lista.index(buscar)
            print("El dato buscado se encuentra en el índice", indice)
        else:
            print("El dato no se encuentra en la lista.")

    elif opcion == 6:
        print("")
        print("Los elementos actuales de la lista son: ")
        print(lista)

    elif opcion == 7:
        print("")
        print("Programa finalizado.")