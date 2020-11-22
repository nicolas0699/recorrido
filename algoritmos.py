import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import copy


def vecino_mas_cercano(matriz_pesos, inicial):
    """
    Función que toma los pesos de un grafo completo y arroja un ciclo hamiltoniano

    :param matriz_pesos: Matriz de pesos del grafo completo
    :param inicial: Punto donde comienz a formar el ciclo hamiltoniano
    :return: vertices, aristas y pesos del ciclo hamiltoniano
    """
    # Inicializa las variables necesarias para poder encontrar el ciclo hamiltoniano

    vertices = []
    aristas = []
    ini = copy.deepcopy(inicial)  # Crea una copia en profundidad del vertice inicial
    pesos = {}
    aux_pesos = {}
    count = 1

    # Crea una copia en profundidad para no cambiar los datos de la variable original
    x = copy.deepcopy(matriz_pesos)
    aux = x[ini - 1]

    # Se incluye el vertice inicial a los vertices
    vertices.append(ini)

    # Este while permite recorrer todos los vertices
    while count != len(x):
        if len(vertices) == 1:
            # Inicializa el grafo con 3 vertices y dos aristas
            while len(vertices) != 3:
                if 0 in aux:
                    # Modifica el cero de la fila para que sea muy grande
                    index = aux.index(0)
                    aux[index] = np.inf
                else:
                    # Enceuntra el minimo, lo añade a vertices y añade las aristas del inicial con el vertice minimo
                    index = aux.index(min(aux))
                    vertices.append(index + 1)
                    aristas.append((inicial, index + 1))
                    # Añadimos las aristas con pesos
                    pesos[(inicial, index + 1)] = aux[index]
                    aux_pesos[(inicial, index + 1)] = aux[index]
                    aux[index] = np.inf
                    count += 1
        else:
            # Continua añadiendo aristas pero de una en una, tomando siempre la menor
            for key, value in aux_pesos.items():
                if value == min(aux_pesos.values()):
                    ini = key[1]
                    break
            aux = x[ini - 1]
            if 0 in aux:
                index = aux.index(0)
                aux[index] = np.inf
            else:
                index = aux.index(min(aux))
                if index + 1 in vertices or [inicial, index + 1] in aristas or [index + 1, inicial] in aristas:
                    # Si el vertice ya está o la arista ya se encuentra se omite este valor
                    aux[index] = np.inf
                    pass
                else:
                    # añado la arista y el peso a el diccionario de pesos
                    pesos[(ini, index + 1)] = aux[index]
                    for key, value in aux_pesos.items():
                        if value == min(aux_pesos.values()):
                            # Sobre escribe el valor de la llave a infinito para no seleccionarla otra vez
                            aux_pesos[key] = np.inf
                            break
                    vertices.append(index + 1)
                    aristas.append((ini, index + 1))
                    aux_pesos[(ini, index + 1)] = aux[index]
                    aux[index] = np.inf
                    count += 1
    return vertices, aristas, pesos


def cerrar(aristas, pesos, matriz_pesos):
    """
    Cierra el camino hamiltoniano conectando los vertices donde su grado sea distinto de dos

    :param matriz_pesos: Matriz de pesos del grafo completo
    :param aristas: Lista de aristas del camino hamiltoniano
    :param pesos: Diccionario de pesos del camino hamiltoniano
    :return: vertices, aristas y pesos del ciclo hamiltoniano
    """
    # Diccionario para contar los grados de cada vértice
    grados = dict.fromkeys([i for i in range(1, len(aristas) + 2)], 0)  # Importante para al final cerrar el ciclo

    # Coloca los números de las aristas en la lista
    x = [j for i in aristas for j in i]
    for i in x:
        grados[i] += 1

    # sobre escribe x para tener las aristas que tienen grado diferente de 2
    x = [key for key, value in grados.items() if value == 1]

    # Se añade a el diccionario pesos la arista y el peso que faltaba
    pesos[(x[0], x[1])] = matriz_pesos[x[0] - 1][x[1] - 1]

    aristas.append((x[0], x[1]))

    return aristas, pesos


def grafo(vertices, aristas):
    """
    Crea el grafico del ciclo hamiltoniano
    :param vertices: Lista de vertices del grafo
    :param aristas: Aristas del grafo
    """
    g = nx.Graph()
    g.add_nodes_from(vertices)
    g.add_edges_from(aristas)
    nx.draw(g, with_labels=True, node_color='green', edge_color='purple')
    plt.savefig('grafo_generado.png')
    plt.close()


def procedimiento_intercambio(aristas, matriz_pesos):
    """
    Realiza intercambios desde la arista anteriormente inicial si los hay con
    alguna otra arista posible dentro del grafo
    :param pesos: Diccionario de pesos del grafo hamiltoniano
    :param matriz_pesos: Matriz de pesos del grafo completo
    :return: vertices, aristas, pesos
    """
    aristas = aristas
    for i in range(5):
        pesos = {}
        for i in aristas:
            pesos[i] = matriz_pesos[i[0] - 1][i[1] - 1]
        move = 1
        arista = 3
        print(aristas)
        while move == 1:
            count = 1
            move = 0
            while count != len(aristas):
                if arista >= len(aristas):
                    break
                # Tomo las aristas que inicializan para ver si es posible cambiar
                if pesos[aristas[0]] < pesos[aristas[1]]:
                    arista1 = aristas[0]
                    arista2 = aristas[arista]
                else:
                    # arista += 1
                    arista1 = aristas[1]
                    arista2 = aristas[arista]

                peso1 = pesos[arista1]
                peso2 = pesos[arista2]
                print("La arista {0} tiene un peso de {1} y la arista {2} tiene un peso de {3}".format(arista1, peso1,
                                                                                                       arista2, peso2))
                # Se busca la nueva arista con los pesos nuevos
                nueva_arista1 = (arista1[0], arista2[0])
                nueva_arista2 = (arista1[1], arista2[1])
                nuevo_peso1 = matriz_pesos[arista1[0] - 1][arista2[0] - 1]
                nuevo_peso2 = matriz_pesos[arista1[1] - 1][arista2[1] - 1]
                print("La nueva arista {0} tiene un peso de {1} y la nueva arista {2} tiene un peso de {3}".format(
                    nueva_arista1, nuevo_peso1, nueva_arista2, nuevo_peso2))
                if peso1 + peso2 < nuevo_peso1 + nuevo_peso2:
                    print('Peso aristas viejas: {0}\nPeso aristas nuevas: {1}'.format(peso1 + peso2,
                                                                                      nuevo_peso1 + nuevo_peso2))
                    count += 1
                    arista += 1
                    pass
                else:
                    if (nueva_arista1[0], nueva_arista1[1]) in aristas or (
                            nueva_arista1[1], nueva_arista1[0]) in aristas or (
                            nueva_arista2[0], nueva_arista2[1]) in aristas or (
                            nueva_arista2[1], nueva_arista2[0]) in aristas:
                        print('La arista ya se enceuntra en el grafo')
                        count += 1
                        arista += 1
                        pass
                    elif nueva_arista1[0] == nueva_arista1[1] or nueva_arista2[0] == nueva_arista2[1]:
                        print('no se puede ejecutar un bucle')
                        count += 1
                        arista += 1
                        pass
                    else:
                        print('Peso aristas viejas: {0}\nPeso aristas nuevas: {1}'.format(peso1 + peso2,
                                                                                          nuevo_peso1 + nuevo_peso2))
                        index1 = aristas.index(arista1)
                        del aristas[index1]
                        aristas.insert(index1, nueva_arista1)
                        index2 = aristas.index(arista2)
                        del aristas[index2]
                        aristas.insert(index2, nueva_arista2)
                        del pesos[arista1]
                        del pesos[arista2]
                        pesos[nueva_arista1] = nuevo_peso1
                        pesos[nueva_arista2] = nuevo_peso2
                        print('Se ejecuto el cambio')
                        break
            if pesos[aristas[0]] < pesos[aristas[1]]:
                aristas = ordenar(aristas)
            else:
                aristas = ordenar(aristas, 1)
    return aristas, pesos


def ordenar(aristas, tipo=0):
    x = aristas[2:]
    y = aristas[:2]
    comparar = y[tipo]
    for i in range(len(x)):
        for j in x:
            if comparar[1] == j[0]:
                x.remove(j)
                y.append(j)
                comparar = j
                break
            elif comparar[1] == j[1]:
                x.remove(j)
                y.append((j[1], j[0]))
                comparar = (j[1], j[0])
                break
    return y


def imprimir_camino_iglesias(pesos, aristas):
    arista1 = aristas[0]
    arista2 = aristas[1]
    y = []
    x = []
    if pesos[arista1] < pesos[arista2]:
        del pesos[arista2]
        y.append(arista1)
        x.append(pesos[arista1])
        del pesos[arista1]
    else:
        del pesos[arista1]
        y.append(arista2)
        x.append(pesos[arista2])
        pesos[arista2]
        del pesos[arista2]

    for key, value in pesos.items():
        y.append(key[1])
        x.append(value)

    for i in range(len(y)):
        if i == 0:
            print(
                'Al empezar en la iglesia {0} debes ir a la iglesia {1} en un tiempo de recorrido de {2}min'.format(y[i][i],
                                                                                                                y[i][1],
                                                                                                                x[i]))
        elif i != len(y) - 1:
            print('Luego ir a la iglesia {0} en un tiempo de recorrido de {1}min'.format(y[i], x[i]))
        else:
            print('Y por ultimo debes llegar a {0} en un tiempo de recortrido de {1}min'.format(y[i], x[i]))
            print('Para un tiempo total de recorrido de {0}min'.format(sum(x)))
    pesos[y[0]] = x[0]
    aristas = [key for key in pesos.keys()]
    return aristas


def imprimir_camino_museos(pesos, aristas):
    arista1 = aristas[0]
    arista2 = aristas[1]
    y = []
    x = []
    if pesos[arista1] < pesos[arista2]:
        del pesos[arista2]
        y.append(arista1)
        x.append(pesos[arista1])
        del pesos[arista1]
    else:
        del pesos[arista1]
        y.append(arista2)
        x.append(pesos[arista2])
        pesos[arista2]
        del pesos[arista2]

    for key, value in pesos.items():
        y.append(key[1])
        x.append(value)

    for i in range(len(y)):
        if i == 0:
            print(
                'Al empezar en la museo {0} debes ir a la museo {1} en un tiempo de recorrido de {2}min'.format(y[i][i],
                                                                                                                y[i][1],
                                                                                                                x[i]))
        elif i != len(y) - 1:
            print('Luego ir a la museo {0} en un tiempo de recorrido de {1}min'.format(y[i], x[i]))
        else:
            print('Y por ultimo debes llegar a {0} en un tiempo de recortrido de {1}min'.format(y[i], x[i]))
            print('Para un tiempo total de recorrido de {0}min'.format(sum(x)))
    pesos[y[0]] = x[0]
    aristas = [key for key in pesos.keys()]
    return aristas


def imprimir_iglesias(pesos, aristas):
    arista1 = aristas[0]
    arista2 = aristas[1]
    y = []
    x = []

    if pesos[arista1] < pesos[arista2]:
        y.append(arista1)
        x.append(pesos[arista1])
        del pesos[arista2]
        pesos[arista2] = x[0]
    else:
        y.append(arista2)
        x.append(pesos[arista2])
        del pesos[arista1]
        pesos[arista1] = x[0]

    count = 0
    for key, value in pesos.items():
        if count == 0:
            print('Al empezar en la iglesia {0} debes ir a la iglesia {1} en un tiempo de recorrido de {2}min'.format(key[0], key[1], value))
            count += 1
        elif count != len(pesos) - 1:
            print('Luego ir a la iglesia {0} en un tiempo de recorrido de {1}min'.format(key[1], value))
            count += 1
        else:
            print('Y por ultimo debes llegar a {0} en un tiempo de recortrido de {1}min'.format(key[0], value))
            print('Para un tiempo total de recorrido de {0}min'.format(sum([value for value in pesos.values()])))
            count += 1

    aristas = [key for key in pesos.keys()]
    print(aristas)
    return aristas


def imprimir_museos(pesos, aristas):
    arista1 = aristas[0]
    arista2 = aristas[1]
    y = []
    x = []

    if pesos[arista1] < pesos[arista2]:
        y.append(arista1)
        x.append(pesos[arista1])
        del pesos[arista2]
        pesos[arista2] = x[0]
    else:
        y.append(arista2)
        x.append(pesos[arista2])
        del pesos[arista1]
        pesos[arista2] = x[0]

    count = 0
    print(pesos)
    for key, value in pesos.items():
        if count == 0:
            print('Al empezar en la museo {0} debes ir a la museo {1} en un tiempo de recorrido de {2}min'.format(key[0], key[1], value))
            count += 1
        elif count != len(pesos) - 1:
            print('Luego ir a la museo {0} en un tiempo de recorrido de {1}min'.format(key[1], value))
            count += 1
        else:
            print('Y por ultimo debes llegar a {0} en un tiempo de recortrido de {1}min'.format(key[0], value))
            print('Para un tiempo total de recorrido de {0}min'.format(sum([value for value in pesos.values()])))
            count += 1

    aristas = [key for key in pesos.keys()]

    return aristas