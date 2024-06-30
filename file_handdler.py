def add_score(name, score):
    with open('better_score.txt', 'r') as archivo:
        lineas = archivo.readlines()

    datos = []
    for linea in lineas:
        partes = linea.split(' ')
        datos.append((partes[0], int(partes[1])))

    datos.append((name, int(score)))

    datos_ordenados = sorted(datos, key=lambda x: x[1], reverse=True)

    with open('better_score.txt', 'w') as archivo:
        for clave, valor in datos_ordenados[:5]:
            archivo.write(f'{clave} {valor}\n')


def reed_score():
    with open('better_score.txt', 'r') as archivo:
        lineas = archivo.readlines()
    return lineas

