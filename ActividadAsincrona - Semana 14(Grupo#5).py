
print("\t\t*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
print("\t\t*~ Bienvenido/a al programa *~")
print("\t\t*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
print("Indicaciones:\nEn este programa debera seleccionar un departamento perteneciente a El Salvador y\nobtendra los distintos municipios pertenecientes a ese departamento\n")

#Conjuntos de Departamentos y Municipios
Departamentos = ["Ahuachapán","Cabañas","Chalatenango","Cuscatlán","Morazán","La Libertad","La Paz","La Unión","San Miguel","San Salvador","San Vicente","Santa Ana","Sonsonate","Usulután"]
Municipios =[["Apaneca","Atiquizaya","Concepción de Ataco","El Refugio","Guaymango","Jujutla","San Francisco Menéndez","San Lorenzo","San Pedro Puxtla","Tacuba","Turín"],
            ["Cinquera","Dolores / Villa Dolores","Guacotecti","Ilobasco","Jutiapa","San Isidro","Sensuntepeque","Tejutepeque","Victoria"],
            ["Agua Caliente","Arcatao","Azacualpa","Chalatenango","Citalá","Comalapa","Concepción Quezaltepeque","Dulce Nombre de María","El Carrizal","El Paraíso","La Laguna","La Palma","La Reina","Las Vueltas","Nombre de Jesús","Nueva Concepción","Nueva Trinidad","Ojos de Agua","Potonico","San Antonio de la Cruz","San Antonio Los Ranchos","San Fernando","San Francisco Lempa","San Francisco Morazán","San Ignacio","San Isidro Labrador","San José Cancasque / Cancasque","San José Las Flores / Las Flores","San Luis del Carmen","San Miguel de Mercedes","San Rafael","Santa Rita","Tejutla"],
            ["Candelaria","Cojutepeque","El Carmen","El Rosario","Monte San Juan","Oratorio de Concepción","San Bartolomé Perulapía","San Cristóbal","San José Guayabal","San Pedro Perulapán","San Rafael Cedros","San Ramón","Santa Cruz Analquito","Santa Cruz Michapa","Suchitoto","Tenancingo"],
            ["Arambala","Cacaopera","Chilanga","Corinto","Delicias de Concepción","El Divisadero","El Rosario","Gualococti","Guatajiagua","Joateca","Jocoaitique","Jocoro","Lolotiquillo","Meanguera","Osicala","Perquín","San Carlos","San Fernando","San Francisco Gotera","San Isidro","San Simón","Sensembra","Sociedad","Torola","Yamabal","Yoloaiquín"],
            ["Antiguo Cuscatlán","Chiltiupán","Ciudad Arce","Colón","Comasagua","Huizúcar","Jayaque","Jicalapa","La Libertad","Santa Tecla","Nuevo Cuscatlán","San Juan Opico","Quezaltepeque","Sacacoyo","San José Villanueva","San Matías","San Pablo Tacachico","Talnique","Tamanique","Teotepeque","Tepecoyo","Zaragoza"],
            ["Cuyultitán","El Rosario / Rosario de La Paz","Jerusalén","Mercedes La Ceiba","Olocuilta","Paraíso de Osorio","San Antonio Masahuat","San Emigdio","San Francisco Chinameca","San Juan Nonualco","San Juan Talpa","San Juan Tepezontes","San Luis La Herradura","San Luis Talpa","San Miguel Tepezontes","San Pedro Masahuat","San Pedro Nonualco","San Rafael Obrajuelo","Santa María Ostuma","Santiago Nonualco","Tapalhuaca","Zacatecoluca"],
            ["Anamorós","Bolívar","Concepción de Oriente","Conchagua","El Carmen","El Sauce","Intipucá","La Unión","Lilisque","Meanguera del Golfo","Nueva Esparta","Pasaquina","Polorós","San Alejo","San José","Santa Rosa de Lima","Yayantique","Yucuaiquín"],
            ["Carolina","Chapeltique","Chinameca","Chirilagua","Ciudad Barrios","Comacarán","El Tránsito","Lolotique","Moncagua","Nueva Guadalupe","Nuevo Edén de San Juan","Quelepa","San Antonio del Mosco","San Gerardo","San Jorge","San Luis de la Reina","San Miguel","San Rafael Oriente","Sesori","Uluazapa"],
            ["Aguilares","Apopa","Ayutuxtepeque","Delgado","Cuscatancingo","El Paisnal","Guazapa","Ilopango","Mejicanos","Nejapa","Panchimalco","Rosario de Mora","San Marcos","San Martín","San Salvador","Santiago Texacuangos","Santo Tomás","Soyapango","Tonacatepeque"],
            ["Apastepeque","Guadalupe","San Cayetano Istepeque","San Esteban Catarina","San Ildefonso","San Lorenzo","San Sebastián","San Vicente","Santa Clara","Santo Domingo","Tecoluca","Tepetitán","Verapaz"],
            ["Candelaria de la Frontera","Chalchuapa","Coatepeque","El Congo","El Porvenir","Masahuat","Metapán","San Antonio Pajonal","San Sebastián Salitrillo","Santa Ana","Santa Rosa Guachipilín","Santiago de la Frontera","Texistepeque"],
            ["Acajutla","Armenia","Caluco","Cuisnahuat","Izalco","Juayúa","Nahuizalco","Nahulingo","Salcoatitán","San Antonio del Monte","San Julián","Santa Catarina Masahuat","Santa Isabel Ishuatán","Santo Domingo de Guzmán","Sonsonate","Sonzacate"],
            ["Alegría","Berlín","California","Concepción Batres","El Triunfo","Ereguayquín","Estanzuelas","Jiquilisco","Jucuapa","Jucuarán","Mercedes Umaña","Nueva Granada","Ozatlán","Puerto El Triunfo","San Agustín","San Buenaventura","San Dionisio","San Francisco Javier","Santa Elena","Santa María","Santiago de María","Tecapán","Usulután"]]

#Funcion StartProgram
def StartProgram():
    Start = True
    Reinicio = False
    while Departamentos:
        z = 0

        #Reinicio de programa
        if Reinicio == True:
            Start = input("\nDesea consultar otro departamento -> ").lower()
            if Start == "si".lower():
                Start = True

            elif Start == "no".lower():
                break

            else:
                print("\n\t~~~ Opción no válida ~~~")

        #Programa
        while Start == True:
            while z < 4 and Start == True:
                print("\n\tDepartamentos de El Salvador:")

                #Lista y selección de departamentos
                x = 0
                for i in range(len(Departamentos)):
                    print(f"\t{x+1}- {Departamentos[x]}")
                    x += 1

                Select = input("\nSelecione 1 departamento -> ").lower()

                #Resultados de la elección del departamento
                if Select == "1" or Select  == Departamentos[0].lower() or Select == "Ahuachapan".lower():
                    print(f"\n\tDepartamento: {Departamentos[0]}")
                    print("\n\tMunicipios:")
                    y = 0
                    for i in range(len(Municipios[0])):
                        print(f"\t{y + 1}- {Municipios[0][y]}")
                        y +=  1
                    Reinicio = True
                    Start = False

                elif Select == "2"or Select  == Departamentos[1].lower():
                    print(f"\n\tDepartamento: {Departamentos[1]}")
                    print("\n\tMunicipios:")
                    y = 0
                    for i in range(len(Municipios[1])):
                        print(f"\t{y + 1}- {Municipios[1][y]}")
                        y +=  1
                    Reinicio = True
                    Start = False

                elif Select == "3"or Select  == Departamentos[2].lower():
                    print(f"\n\tDepartamento: {Departamentos[2]}")
                    print("\n\tMunicipios:")
                    y = 0
                    for i in range(len(Municipios[2])):
                        print(f"\t{y + 1}- {Municipios[2][y]}")
                        y +=  1
                    Reinicio = True
                    Start = False

                elif Select == "4"or Select  == Departamentos[3].lower() or Select == "Cuscatlan".lower():
                    print(f"\n\tDepartamento: {Departamentos[3]}")
                    print("\n\tMunicipios:")
                    y = 0
                    for i in range(len(Municipios[3])):
                        print(f"\t{y + 1}- {Municipios[3][y]}")
                        y +=  1
                    Reinicio = True
                    Start = False

                elif Select == "5"or Select  == Departamentos[4].lower() or Select == "Morazan".lower():
                    print(f"\n\tDepartamento: {Departamentos[4]}")
                    print("\n\tMunicipios:")
                    y = 0
                    for i in range(len(Municipios[4])):
                        print(f"\t{y + 1}- {Municipios[4][y]}")
                        y +=  1
                    Reinicio = True
                    Start = False

                elif Select == "6"or Select  == Departamentos[5].lower() or Select == "Libertad".lower():
                    print(f"\n\tDepartamento: {Departamentos[5]}")
                    print("\n\tMunicipios:")
                    y = 0
                    for i in range(len(Municipios[5])):
                        print(f"\t{y + 1}- {Municipios[5][y]}")
                        y +=  1
                    Reinicio = True
                    Start = False

                elif Select == "7"or Select  == Departamentos[6].lower():
                    print(f"\n\tDepartamento: {Departamentos[6]}")
                    print("\n\tMunicipios:")
                    y = 0
                    for i in range(len(Municipios[6])):
                        print(f"\t{y + 1}- {Municipios[6][y]}")
                        y +=  1
                    Reinicio = True
                    Start = False

                elif Select == "8"or Select  == Departamentos[7].lower() or Select == "La Union".lower() or Select == "Union".lower() or Select == "Unión".lower():
                    print(f"\n\tDepartamento: {Departamentos[7]}")
                    print("\n\tMunicipios:")
                    y = 0
                    for i in range(len(Municipios[7])):
                        print(f"\t{y + 1}- {Municipios[7][y]}")
                        y +=  1
                    Reinicio = True
                    Start = False

                elif Select == "9"or Select  == Departamentos[8].lower():
                    print(f"\n\tDepartamento: {Departamentos[8]}")
                    print("\n\tMunicipios:")
                    y = 0
                    for i in range(len(Municipios[8])):
                        print(f"\t{y + 1}- {Municipios[8][y]}")
                        y +=  1
                    Reinicio = True
                    Start = False

                elif Select == "10" or Select  == Departamentos[9].lower():
                    print(f"\n\tDepartamento: {Departamentos[9]}")
                    print("\n\tMunicipios:")
                    y = 0
                    for i in range(len(Municipios[9])):
                        print(f"\t{y + 1}- {Municipios[9][y]}")
                        y +=  1
                    Reinicio = True
                    Start = False

                elif Select == "11" or Select  == Departamentos[10].lower():
                    print(f"\n\tDepartamento: {Departamentos[10]}")
                    print("\n\tMunicipios:")
                    y = 0
                    for i in range(len(Municipios[10])):
                        print(f"\t{y + 1}- {Municipios[10][y]}")
                        y +=  1
                    Reinicio = True
                    Start = False

                elif Select == "12" or Select  == Departamentos[11].lower():
                    print(f"\n\tDepartamento: {Departamentos[11]}")
                    print("\n\tMunicipios:")
                    y = 0
                    for i in range(len(Municipios[11])):
                        print(f"\t{y + 1}- {Municipios[11][y]}")
                        y +=  1
                    Reinicio = True
                    Start = False

                elif Select == "13" or Select  == Departamentos[12].lower():
                    print(f"\n\tDepartamento: {Departamentos[12]}")
                    print("\n\tMunicipios:")
                    y = 0
                    for i in range(len(Municipios[12])):
                        print(f"\t{y + 1}- {Municipios[12][y]}")
                        y +=  1
                    Reinicio = True
                    Start = False

                elif Select == "14" or Select  == Departamentos[13].lower() or Select == "Usulutan".lower():
                    print(f"\n\tDepartamento: {Departamentos[13]}")
                    print("\n\tMunicipios:")
                    y = 0
                    for i in range(len(Municipios[13])):
                        print(f"\t{y + 1}- {Municipios[13][y]}")
                        y +=  1
                    Reinicio = True
                    Start = False

                #Contador de intentos fallidos
                else:
                    z += 1
                    if z == 4:
                        print("\n\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")                        
                        print("\t~~ Demasados intentos fallidos ~~")
                        print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                        Reinicio = True
                        Start = False

                    else:
                        print("\n\t~~~ Opción no válida ~~~")

#Inicio o fin del programa
while Departamentos:
    Start = input("Desea iniciar el programa -> ").lower()
    if Start == "si".lower():
        StartProgram()
        break

    elif Start == "no".lower():
        break

    else:
        print("~~~ Opción no válida ~~~")

print("\nFin del programa")