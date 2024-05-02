"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
def lectura_csv ():
    with open("data.csv", "r") as file:
        contenido = file.readlines()
    lista = [line.replace("\n", "") for line in contenido]
    lista = [line.replace("\t", "_") for line in lista]
    texto = [line.split("_") for line in lista]
    return texto
# texto=lectura_csv()
# print(texto)

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    listas=lectura_csv()     
    suma=0
    suma= sum([suma + int(line[1]) for line in listas])
    return suma
#texto=pregunta_01()
#print(texto)

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    listas=lectura_csv()
    letras= [(line[0],1) for line in listas]
    letras_keys=[]
    letras_keys=sorted(list(set(tupla[0] for tupla in letras)))
    cant_registros_letra = [ tuple([tupla[0],sum([int(tuplas[1]) for tuplas in letras if tuplas[0]==tupla[0]]) ]) for tupla in letras_keys]
    return cant_registros_letra
# texto=pregunta_02()
# print(texto)

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    listas=lectura_csv()
    letras= [(line[0] , line[1]) for line in listas]
    letras_keys=[]
    letras_keys=sorted(list(set(tupla[0] for tupla in letras)))
    sum_registros_letra = [ tuple([tupla[0],sum([int(tuplas[1]) for tuplas in letras if tuplas[0]==tupla[0]]) ]) for tupla in letras_keys]
    return sum_registros_letra
#texto=pregunta_03()
#print(texto)


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    listas=lectura_csv()
    meses= [(str(line[2].split('-')[1]),1) for line in listas]
    mes_keys=[]
    mes_keys=sorted(list(set(tupla[0] for tupla in meses)))
    cant_registros_mes = [(tupla,sum([tuplas[1] for tuplas in meses if tuplas[0]==tupla])) for tupla in mes_keys]
    return cant_registros_mes
# texto=pregunta_04()
# print(texto)

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    listas=lectura_csv()
    letras= [(line[0], int(line[1]), int(line [1])) for line in listas]
    letras_keys=[]
    letras_keys=sorted(list(set(tupla[0] for tupla in letras)))
    cant_registros_mes = [((tupla,max([tuplas[1] for tuplas in letras if tuplas[0]==tupla]), min([tuplas[1] for tuplas in letras if tuplas[0]==tupla]))) for tupla in letras_keys]
    return cant_registros_mes
# texto=pregunta_05()
# print(texto)

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    listas = lectura_csv()
    letras = [line[4].split(',')for line in listas]
    nuevas_letras = []
    [[nuevas_letras.append(grupos) for grupos in filas ]for filas in letras]
    letras = ([(diccio.split(':')[0] , int (diccio.split(':')[1]))  for diccio in nuevas_letras])
    letras_keys=[]
    [letras_keys.append(clave[0]) for clave in letras if clave[0] not in letras_keys]
    letras_keys=sorted(letras_keys)
    cant_registros_mes = [((tupla,min ([tuplas[1] for tuplas in letras if tuplas[0]==tupla]), max ([tuplas[1] for tuplas in letras if tuplas[0]==tupla]))) for tupla in letras_keys]
    return cant_registros_mes

#texto=pregunta_06()
#print(texto)

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    listas = lectura_csv()
    letras_keys=[]
    [letras_keys.append(clave) for clave in [line[1] for line in listas] if clave not in letras_keys]
    letras_keys=sorted(letras_keys)
    letras_tupla = [((int(tupla),[tuplas[0] for tuplas in listas if tuplas[1]==tupla])) for tupla in letras_keys]
    return letras_tupla
    
#texto=pregunta_07()
#print(texto)


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    tuplas=pregunta_07()
    letras_tupla = [(int(tupla[0]),sorted(list(set(tupla[1])))) for tupla in tuplas]
    return letras_tupla
    
#texto=pregunta_08()
#print(texto)

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    listas = lectura_csv()
    letras = [line[4].split(',') for line in listas]
    nuevas_letras = []
    [[nuevas_letras.append(grupos) for grupos in filas ]for filas in letras]
    tupla = [(nuevas.split(':')[0], 1) for nuevas in nuevas_letras]
    tupla = sorted( tupla )
    diccionario = {}
    for i in tupla:
        diccionario [i[0]]=sum([j[1] for j in tupla if i[0]==j[0]])
    return diccionario

#texto=pregunta_09()
#print(texto)

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    listas = lectura_csv()
    lista_tupla = [( line[0],len (line[3].split(',')),len (line[4].split(','))) for line in listas]
    return lista_tupla

#texto=pregunta_10()
#print(texto)

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    listas = lectura_csv()
    lista = [(fila[1], fila[3].split(',')) for fila in listas]
    diccionario={}
    for i in lista:
        for x in i[1]:
            if x in diccionario:
                diccionario[x] += int(i[0])
            else:
                diccionario[x] = int(i[0])
    return dict(sorted(diccionario.items()))

# texto=pregunta_11()
# print(texto)

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    data = lectura_csv()
    dic = {}
    for row in data:
        for letter in row[4].split(","):
            _, value = letter.split(":")
            if row[0] in dic:
                dic[row[0]] += int(value)
            else:
                dic[row[0]] = int(value)
    
    return dict(sorted(dic.items()))
