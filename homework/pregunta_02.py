"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_02():
        
    import pandas as pd

    data = pd.read_csv("files/input/tbl0.tsv", sep="\t",header=0)
    return data.count(axis=1)[0]

    # """
    # ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    # Rta/
    # 4

    # """
