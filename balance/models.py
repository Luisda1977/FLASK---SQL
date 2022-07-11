import sqlite3


class DBManager:
    def __init__(self, ruta):
        self.ruta=ruta

    def consultaSQL(self, consulta):
        # 1. conectar con la BD (base de datos)
        conexion = sqlite3.connect(self.ruta)

        # 2. abrir un cursor
        cursor = conexion.cursor()

        # 3. ejecutar consulta SQL
        cursor.execute(consulta)

        # 4. tratar los datos
        #  4.1 obtengo los nombres de columna
        #    (("nom_col",....), (), ()...)
        #  4.2 pido todos los datos (registros)
        #  4.3 recorrer los resultados
        #    4.3.1 crear un diccionario
        #       - recorro la lista de los nombres de columna
        #       - para cada columna: nombre + valor
        #    4.3.2 guardar en la lista de movimientos  
        # [{"nom_col1": "val_col1",....}]    

        self.movimientos = []
        nombres_columnas = []

        for desc_columna in cursor.description:
            nombres_columnas.append(desc_columna[0])
        # nombres_columnas = ["nom_col1", "nom_col2"...]
        # nombres_columnas = ["id", "fecha", "conepto", "tipo", "cantidad"]

        datos = cursor.fetchall()
        for dato in datos:
            movimiento  = {}
            indice = 0
            for nombre in nombres_columnas:
                movimiento[nombre] = dato[indice]
                indice += 1
            self.movimientos.append(movimiento)

        conexion.close()

        return self.movimientos