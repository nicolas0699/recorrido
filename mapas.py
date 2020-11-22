import folium
import branca


def mapa():
    # Inicializa el mapa en la candelaria
    mapa = folium.Map(location=(4.5963989, -74.0797888), zoom_start=16)
    # Coordenadas para iglesias
    primada = (4.5972806, -74.0769709)
    carmen = (4.5945271, -74.0770678)
    loyola = (4.5968792, -74.0777072)
    candelaria = (4.5965493, -74.0748279)
    ermita = (4.5972111, -74.0721242)
    egipto = (4.5937161, -74.0714746)
    aguas = (4.602256, -74.0691681)
    bordadita = (4.59988, -74.0753887)
    tercera = (4.6026623, -74.075385)
    veracruz = (4.60246, -74.0751886)
    francisco = (4.602442, -74.0755424)

    # Coordenadas para museos
    oro = (4.6016886, -74.074074)
    julio = (4.598312, -74.0773027)
    trajes = (4.5970035, -74.0773898)
    colonial = (4.5967309, -74.0773572)
    arqueologico = (4.5948836, -74.0784287)
    clara = (4.5969528, -74.0794693)
    rufino = (4.5960285, -74.0760094)
    militar = (4.596206, -74.0761537)
    moneda = (4.596955, -74.0757118)
    poesia = (4.5985978, -74.0728427)

    # La información de los marcadores la añadiremos usando branca, sirve para escribir en html las etiquetas
    # # etiquetas de las iglesias
    html = """
            <p>
                <b>1. Catedral primada de Colombia</b>
                <p>
                    La Catedral Basílica Metropolitana de Bogotá y Primada de Colombia, oficialmente Sacro 
                    Santo Templo Catedral Basílica Metropolitana y Primada de la Inmaculada Concepción de María y 
                    San Pedro. Se construyó entre 1807 y 1823. Por su significado histórico, valor 
                    arquitectónico y cultural fue declarada Monumento Nacional.
                </p>
            </p>
            """
    iframe1 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
            <p>
                <b>2. Santuario Nuestra Señora de El Carmen:</b>
                <p>
                    El Santuario Nacional Nuestra Señora del Carmen es un templo católico dedicado a 
                    la Virgen María bajo la advocación del Carmen. Se destaca su pintura interpolada marrón y
                     crema, colores emblemáticos de los Carmelitanos. Su construcción inició en 1926 y fue consagrada 
                     en el año 1938.
                </p>
            </p>"""
    iframe2 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
            <p>
                <b>3. Iglesia de San Ignacio de Layola</b>
                <p>
                    La primera piedra se puso en noviembre de 1610 y la construcción se finalizó en 1691. En 1635 
                    la iglesia fue consagrada a San Ignacio de Loyola, el fundador de la Compañía de Jesús.
                </p>
            </p>
            """
    iframe3 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
            <p>
                <b>4. Iglesia de Nuestra Señora de la Candelaria</b>
                <p>
                    Su construcción se inició el 1686 y fue finalizado en 1703. El templo alberga importantes 
                    obras de arte religioso de origen colonial. Por su significado histórico, valor arquitectónico y 
                    cultural, el templo y el antiguo convento fueron declarados Monumento Nacional. 
                </p>    
            </p>
            """
    iframe4 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
            <p>
                <b>5. Ermita de San Miguel del Príncipe</b>
                <p>
                    Desde su construcción en 1969, la Ermita de San Miguel del Príncipe a imagen de la antigua Capilla
                    del Humilladero, fue la primera iglesia que tuvo Bogotá. Se dice fue el primer asentamiento 
                    español en la capital.
                </p>
            </p>
            """
    iframe5 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
           <p>
                <b>6. Iglesia de Nuestra Señora de Egipto:</b>
                <p>La Iglesia de Nuestra Señora del Destierro y Huida a Egipto es un templo católico ubicado en el
                 barrio Egipto nombrado por la iglesia que conlleva ese nombre, fue construida entre 1656 y 1775
                </p>
           </p>
           """
    iframe6 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
            <p>
                <b>7. Parroquia de Nuestra Señora de las Aguas</b>
                <p>
                    El templo hacía parte del antiguo convento de las Aguas, el cual a lo largo de su historia se ha 
                    desempeñado también como hospital, orfanato y actualmente es la sede de Artesanías de Colombia, 
                    fue construida entre 1657 y 1694. Por su significado histórico, valor arquitectónico y cultural,
                    el templo y el antiguo convento fueron declarados Monumento Nacional.
                </p>
            </p>
            """
    iframe7 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
            <p>
                <b>8. Iglesia La Bordadita</b>
                <p>
                    La Capilla se construyó en el siglo XVII al mismo tiempo que el Colegio Mayor del Rosario.
                     Conocida como La Bordadita por el cuadro que se ubica en el centro del retablo del 
                     altar principal de Nuestra Señora del Rosario, el cual fue bordado por la reina Margarita de 
                     Austria en la segunda mitad del siglo XVII.
                </p>
            </p>
            """
    iframe8 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
            <p>
                <b>9. Iglesia de la Orden Tercera</b>
                <p>
                    La iglesia de La Tercera o iglesia de los Estigmas tiene una construcción data que del 
                    siglo XVIII. Perteneció a la Orden Tercera Seglar o de Penitencia, que sigue los paradigmas 
                    de San Francisco de Asís. La iglesia se construyó entre 1761 y 1780, La torre, por su 
                    parte, se erigió en 1857. 
                </p>
            </p>
            """
    iframe9 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
            <p>
                <b>10. Iglesia de la Veracruz</b>
                <p>
                    Se encuentra en la antigua Calle Del Arco. La capilla original se construyó en el siglo XVI, 
                    poco después de la fundación de la ciudad. Según la placa instalada en la fachada norte se inauguró
                    en 1549, pero otras fuentes citan el año de 1575 como la fecha de sus inicios.
                </p>
            </p>
            """
    iframe10 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
            <p>
                <b>11. Iglesia de San Francisco</b>
                <p>
                    Se localiza en el barrio Veracruz, en la Avenida Jiménez con la carrera Séptima.
                    Se construyó entre 1557 y 1566; Actualmente es la iglesia más antigua que se conserva 
                    en Bogotá. Este edificio es el que tiene una artesa o armadura mudéjar , una de las
                    mejores de la nueva granada, el retablo es el más representativo del virreinato de la Nueva 
                    Granada.
                </p>
            </p>
            """
    iframe11 = branca.element.IFrame(html=html, width=300, height=200)

    # # etiqueta de los museos
    html = """
            <p>
                <b>1. Museo del oro</b>
                <p>
                    El Museo del Oro del Banco de la República en Bogotá, preserva una extraordinaria colección de
                    orfebrería prehispánica, la más grande del mundo. Sus objetos arqueológicos de metal, cerámica, 
                    piedra, concha, madera y textil dan testimonio de la vida y el pensamiento de las sociedades 
                    indígenas que habitaron el territorio hoy colombiano antes del contacto con Europa.
                </p>
            </p>
            """
    iframe12 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
            <p>
                <b>2. Museo de la Independencia</b>
                <p>
                    El Museo de la Independencia - Casa del Florero, antes llamado Museo del 20 de julio. 
                    En él se produjo uno de los acontecimientos históricos más destacados, conocido como el Grito de 
                    Independencia, el 20 de julio de 1810.
                </p>
            </p>
            """
    iframe13 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
            <p>
                <b>3. Museo de trajes</b>
                <p>
                    El Museo de Trajes es una dependencia de la Universidad de América. Fundado en 1975 por la 
                    antropóloga Edith Jiménez de Muñoz. El Museo es un espacio de encuentro alrededor del tema del
                    Traje y de diálogo entre el pasado, presente y futuro del traje en Colombia.
                </p>
            </p>
            """
    iframe14 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
            <p>
                <b>4. Museo arte colonial</b>
                <p>
                    Fue construido en 1610. Se encuentra ubicado en el Centro Histórico de Bogotá. Cuenta con una 
                    amplia colección de pintura, escultura, mobiliario y artes decorativas de los siglos XVI, XVII y
                    XVIII.
                </p>
            </p>
            """
    iframe15 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
            <p>
                <b>5. Museo Arqueológico</b>
                <p>
                    El MUSA alberga la colección más grande y diversa de piezas cerámicas precolombinas en Colombia. 
                    Hoy en día cuenta con trece mil objetos que representan las principales culturas que habitaron el 
                    territorio nacional: Tairona, Muisca, Guane, Quimbaya, Calima, Nariño, Sinú, Tumaco, San Agustín, 
                    entre otras.
                </p>
            </p>
            """
    iframe16 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
            <p>
                <b>6. Museo Santa Clara</b>
                <p>
                    Fue construido en 1647. Cuenta con una amplia colección de pinturas y esculturas de los siglos XVII,
                     XVIII, XIX y XX. El edificio se considera una de las muestras más representativas de la 
                     arquitectura y el ornato barrocos de los siglos XVII y XVIII en Bogotá.
                </p>
            </p>
            """
    iframe17 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
            <p>
                <b>7. Casa Natal de Rufino José Cuervo</b>
                <p>
                    Construida en el siglo XVIII, en 1970 el entonces gobernador de Cundinamarca estableció la casa como 
                    sede del Instituto Caro y Cuervo, que la restauró entre 1970 y 1974. En 1974 el presidente Misael 
                    Pastrana le dio el carácter de casa museo literario y el 22 de julio de ese mismo año fue declarada 
                    patrimonio arquitectónico y cultural.
                </p>
            </p>
            """
    iframe18 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
            <p>
                <b>8. Museo militar</b>
                <p>
                    Contiene una importante colección de esculturas, documentos históricos, condecoraciones,
                    uniformes militares, armas, vehículos y maquetas que muestran la historia y
                    evolución técnica de las Fuerzas Militares de Colombia. El edificio actual donde funciona el 
                    Museo fue construido entre 1911 y 1913.
                </p>
            </p>
            """
    iframe19 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
            <p>
                <b>9. Museo Casa de Moneda</b>
                <p>
                    El Museo Casa de la Moneda, acoge la Colección Numismática del Banco de la República desde 1996.
                </p>
            </p>"""
    iframe20 = branca.element.IFrame(html=html, width=300, height=200)
    html = """
            <p>
                <b>10. Museo Casa de Poesía Silva</b>
                <p>
                    Fue fundada el 24 de mayo de 1986 por Belisario Betancur, es la casa en la que 
                    habitó los últimos 5 años de su vida el poeta colombiano José Asunción Silva. Cuenta con una
                    biblioteca y un fonoteca especializadas en poesía, un auditorio y una librería. La casa fue
                    declarada Monumento Nacional en 1995.
                </p>
            </p>
            """
    iframe21 = branca.element.IFrame(html=html, width=300, height=200)

    # creamos marcadores y añadimos la información del popup usando folium.Popup
    # # Marcadores para iglesias
    marcador1 = folium.Marker(
        location=primada,
        popup=folium.Popup(iframe1, max_width=500),
        icon=folium.Icon(color="orange")
    )
    marcador2 = folium.Marker(
        location=carmen,
        popup=folium.Popup(iframe2, max_width=500),
        icon=folium.Icon(color="orange")
    )
    marcador3 = folium.Marker(
        location=loyola,
        popup=folium.Popup(iframe3, max_width=500),
        icon=folium.Icon(color="orange")
    )
    marcador4 = folium.Marker(
        location=candelaria,
        popup=folium.Popup(iframe4, max_width=500),
        icon=folium.Icon(color="orange")
    )
    marcador5 = folium.Marker(
        location=ermita,
        popup=folium.Popup(iframe5, max_width=500),
        icon=folium.Icon(color="orange")
    )
    marcador6 = folium.Marker(
        location=egipto,
        popup=folium.Popup(iframe6, max_width=500),
        icon=folium.Icon(color="orange")
    )
    marcador7 = folium.Marker(
        location=aguas,
        popup=folium.Popup(iframe7, max_width=500),
        icon=folium.Icon(color="orange")
    )
    marcador8 = folium.Marker(
        location=bordadita,
        popup=folium.Popup(iframe8, max_width=500),
        icon=folium.Icon(color="orange")
    )
    marcador9 = folium.Marker(
        location=tercera,
        popup=folium.Popup(iframe9, max_width=500),
        icon=folium.Icon(color="orange")
    )
    marcador10 = folium.Marker(
        location=veracruz,
        popup=folium.Popup(iframe10, max_width=500),
        icon=folium.Icon(color="orange")
    )
    marcador11 = folium.Marker(
        location=francisco,
        popup=folium.Popup(iframe11, max_width=500),
        icon=folium.Icon(color="orange")
    )

    # # Marcadores museos
    marcador12 = folium.Marker(
        location=oro,
        popup=folium.Popup(iframe12, max_width=500),
        icon=folium.Icon(color="black")
    )
    marcador13 = folium.Marker(
        location=julio,
        popup=folium.Popup(iframe13, max_width=500),
        icon=folium.Icon(color="black")
    )
    marcador14 = folium.Marker(
        location=trajes,
        popup=folium.Popup(iframe14, max_width=500),
        icon=folium.Icon(color="black")
    )
    marcador15 = folium.Marker(
        location=colonial,
        popup=folium.Popup(iframe15, max_width=500),
        icon=folium.Icon(color="black")
    )
    marcador16 = folium.Marker(
        location=arqueologico,
        popup=folium.Popup(iframe16, max_width=500),
        icon=folium.Icon(color="black")
    )
    marcador17 = folium.Marker(
        location=clara,
        popup=folium.Popup(iframe17, max_width=500),
        icon=folium.Icon(color="black")
    )
    marcador18 = folium.Marker(
        location=rufino,
        popup=folium.Popup(iframe18, max_width=500),
        icon=folium.Icon(color="black")
    )
    marcador19 = folium.Marker(
        location=militar,
        popup=folium.Popup(iframe19, max_width=500),
        icon=folium.Icon(color="black")
    )
    marcador20 = folium.Marker(
        location=moneda,
        popup=folium.Popup(iframe20, max_width=500),
        icon=folium.Icon(color="black")
    )
    marcador21 = folium.Marker(
        location=poesia,
        popup=folium.Popup(iframe21, max_width=500),
        icon=folium.Icon(color="black")
    )

    # Se crea el grupo de iglesias y museos

    iglesias = folium.FeatureGroup(name='Iglesias')
    museos = folium.FeatureGroup(name='Museos')

    # Añadimos los marcadores de iglesias al grupo de iglesias
    marcador1.add_to(iglesias)
    marcador2.add_to(iglesias)
    marcador3.add_to(iglesias)
    marcador4.add_to(iglesias)
    marcador5.add_to(iglesias)
    marcador6.add_to(iglesias)
    marcador7.add_to(iglesias)
    marcador8.add_to(iglesias)
    marcador9.add_to(iglesias)
    marcador10.add_to(iglesias)
    marcador11.add_to(iglesias)

    # Añadimos los marcadores de museos al grupo de museos
    marcador12.add_to(museos)
    marcador13.add_to(museos)
    marcador14.add_to(museos)
    marcador15.add_to(museos)
    marcador16.add_to(museos)
    marcador17.add_to(museos)
    marcador18.add_to(museos)
    marcador19.add_to(museos)
    marcador20.add_to(museos)
    marcador21.add_to(museos)

    # Añadir los grupos al mapa
    iglesias.add_to(mapa)
    museos.add_to(mapa)

    # Añadimos control de capas
    folium.LayerControl().add_to(mapa)

    # Y guardamos el mapa
    mapa.save("mapa_candelaria.html")
