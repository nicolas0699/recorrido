from algoritmos import *
from mapas import mapa
import webbrowser
from PIL import Image


while True:
    print('--------------------------------Visita de Iglesias y museos--------------------------------------------')
    print('1. Mirar información de iglesias y museos en el mapa.')
    print('')
    print('2. Dime la ruta que debo seguir.')
    print('')
    print('3. Salir.')
    print('')
    num = int(input('Escriba el número de la acción que desea realizar: '))
    if num == 1:
        while True:
            mapa()
            # Cambia la dirección en donde se encuentra el .html
            direccion = '~/Universidad/Grafos/proyecto/' + 'mapa_candelaria.html'
            webbrowser.open_new_tab(direccion)
            break
    elif num == 2:
        while True:
            print('-------------------------*-----------------------------------')
            print('1. Visitar museos')
            print('')
            print('2. Visitar iglesias')
            print('')
            print('3. Para elegir nuevamente mi acción')
            print('')
            num = int(input('¿Que lugares deseas visitar?'))
            if num == 3:
                break
            while True:
                if num == 1:
                    print('-------------------------------------*---------------------------')
                    print('1. Museo del oro')
                    print('')
                    print('2. Museo de la Independencia')
                    print('')
                    print('3. Museo de trajes')
                    print('')
                    print('4. Museo arte colonial')
                    print('')
                    print('5. Museo Arqueológico')
                    print('')
                    print('6. Museo Santa Clara')
                    print('')
                    print('7. Casa Natal de Rufino José Cuervo')
                    print('')
                    print('8. Museo militar')
                    print('')
                    print('9. Museo Casa de Moneda')
                    print('')
                    print('10. Museo Casa de Poesía Silva')
                    print('')
                    print('11. Para volver a elegir que lugares visitar')
                    print('')
                    num = int(input('¿Cual es tu punto de partida?'))
                    print('')
                    if num == 11:
                        break
                    pesos_museos = [[0, 8, 9, 9, 12, 12, 11, 10, 9, 7], [8, 0, 3, 3, 6, 4, 6, 5, 4, 10],
                                    [9, 3, 0, 1, 3, 3, 3, 2, 4, 10], [9, 3, 1, 0, 3, 4, 3, 2, 3, 10],
                                    [12, 6, 3, 3, 0, 5, 6, 5, 7, 13], [12, 4, 3, 4, 5, 0, 7, 7, 8, 14],
                                    [11, 6, 3, 3, 6, 7, 0, 1, 2, 7], [10, 5, 2, 2, 5, 7, 1, 0, 2, 8],
                                    [9, 4, 4, 3, 7, 8, 2, 2, 0, 6], [7, 10, 10, 10, 13, 14, 7, 8, 6, 0]]
                    vertices, aristas, pesos = vecino_mas_cercano(pesos_museos, num)

                    aristas, pesos = cerrar(aristas, pesos, pesos_museos)
                    if pesos[aristas[0]] < pesos[aristas[1]]:
                        aristas = ordenar(aristas)
                    else:
                        aristas = ordenar(aristas, 1)
                    aristas, pesos = procedimiento_intercambio(aristas, pesos_museos)
                    print('------------------------------*-----------------------------')
                    print('1. Si.')
                    print('')
                    print('2. No.')
                    num = int(input('¿Quieres volver a tu punto de partida?'))
                    if num == 2:
                        aristas = imprimir_camino_museos(pesos, aristas)
                        grafo(vertices, aristas)
                        img = Image.open('./grafo_generado.png')
                        img.show()
                        break
                    elif num == 1:
                        aristas = imprimir_museos(pesos, aristas)
                        grafo(vertices, aristas)
                        img = Image.open('./grafo_generado.png')
                        img.show()
                        break
                elif num == 2:
                    print('-------------------------------------*---------------------------')
                    print('1. Catedral primada de Colombia')
                    print('')
                    print('2. Santuario Nuestra Señora de El Carmen')
                    print('')
                    print('3. Iglesia de San Ignacio de Layola')
                    print('')
                    print('4. Iglesia de Nuestra Señora de la Candelaria')
                    print('')
                    print('5. Ermita de San Miguel del Príncipe')
                    print('')
                    print('6. Iglesia de Nuestra Señora de Egipto')
                    print('')
                    print('7. Parroquia de Nuestra Señora de las Aguas')
                    print('')
                    print('8. Iglesia La Bordadita')
                    print('')
                    print('9. Iglesia de la Orden Tercera')
                    print('')
                    print('10. Iglesia de la Veracruz')
                    print('')
                    print('11. Iglesia de San Francisco')
                    print('')
                    print('12. Para volver a elegir que lugares visitar')
                    print('')
                    num = int(input('¿Cual es tu punto de partida?'))
                    print('')
                    if num == 12:
                        break
                    pesos_iglesias =[[0, 5, 1, 4, 10, 18, 15, 4, 9, 9, 7],
                                     [5, 0, 4, 6, 11, 15, 17, 9, 14, 14, 12],
                                     [1, 4, 0, 6, 11, 18, 19, 6, 10, 9, 7],
                                     [4, 6, 1, 0, 5, 15, 12, 6, 11, 11, 9],
                                     [10, 11, 11, 5, 0, 15, 9, 6, 11, 11, 9],
                                     [18, 15, 18, 15, 15, 0, 22, 18, 23, 23, 21],
                                     [15, 17, 19, 12, 9, 22, 0, 11, 10, 10, 11],
                                     [4, 9, 6, 6, 6, 18, 11, 0, 5, 5, 3],
                                     [9, 14, 10, 11, 11, 23, 10, 5, 0, 1, 2],
                                     [9, 14, 9, 11, 11, 23, 10, 5, 1, 0, 2],
                                     [7, 12, 7, 9, 9, 21, 11, 3, 3, 3, 0]]

                    vertices, aristas, pesos = vecino_mas_cercano(pesos_iglesias, num)

                    aristas, pesos = cerrar(aristas, pesos, pesos_iglesias)
                    if pesos[aristas[0]] < pesos[aristas[1]]:
                        aristas = ordenar(aristas)
                    else:
                        aristas = ordenar(aristas, 1)
                    x = aristas
                    aristas, pesos = procedimiento_intercambio(aristas, pesos_iglesias)
                    print(aristas)
                    print('------------------------------*-----------------------------')
                    print('1. Si.')
                    print('')
                    print('2. No.')
                    num = int(input('¿Quieres volver a tu punto de partida?'))
                    if num == 2:
                        aristas = imprimir_camino_iglesias(pesos, aristas)
                        grafo(vertices, aristas)
                        img = Image.open('./grafo_generado.png')
                        img.show()
                        break
                    elif num == 1:
                        aristas = imprimir_iglesias(pesos, aristas)
                        grafo(vertices, aristas)
                        img = Image.open('./grafo_generado.png')
                        img.show()
                        break
    elif num == 3:
        break




