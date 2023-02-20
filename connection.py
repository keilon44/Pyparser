import pyodbc

# Establecer la conexión


def insertquery(name, phone, email, empresa, texto):
    cnxn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=server_name;'
                      'DATABASE=database_name;'
                      'UID=username;'
                      'PWD=password')

    # Crear un cursor
    cursor = cnxn.cursor()

    # Ejecutar una consulta
    cursor.execute("INSERT INTO table_name (name, phone, email, empresa, texto) VALUES (?,?,?,?,?)", (name, phone, email, empresa, texto))

    # Obtener los resultados
    #results = cursor.fetchall()

    # Imprimir los resultados
    #for row in results:
    #  print(row)

    # Cerrar la conexión
    cnxn.close()
