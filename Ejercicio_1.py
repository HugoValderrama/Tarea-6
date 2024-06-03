lista = []

while True:
    palabra = input("Ingrese palabra a agregar a la lista (Presione Enter para finalizar): ")

    if palabra == "":
        break

    lista.append(palabra)
    print("")
    print("Contenido actual de la lista: ", lista)

vocales = "aeiouAEIOU"
for palabra in lista:
    num_vocales = 0
    num_consonantes = 0
    lista_vocales = []
    lista_consonantes = []

    for letra in palabra:
        if letra.isalpha():
            if letra in vocales:
                num_vocales += 1
                lista_vocales.append(letra)
            else:
                num_consonantes += 1
                lista_consonantes.append(letra)

    str_vocales = ''.join(lista_vocales)
    str_consonantes = ''.join(lista_consonantes)

    print("")
    print("Palabra:", palabra)
    print("Vocales ",num_vocales, " : ", str_vocales)
    print("Consonantes ", num_consonantes, " : ", str_consonantes)
    print("-" * 30)