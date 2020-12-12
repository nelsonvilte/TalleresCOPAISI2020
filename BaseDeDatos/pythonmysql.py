import pymysql

#configuracion de la conexion
datosConexion={
    'host':'localhost',
    'user':'passuser',
    'password':'password',
    'database':'universidad'
}

try:
    conexion = pymysql.connect(**datosConexion)
    print('Conexion Exitosa')
    cursor = conexion.cursor()
except Exception:
    print("Conexion")
    raise

#Asegurar el cierre de la conexion despues de usarla
def cerrarConexion():
    cursor.close()
    conexion.close()
    print("Conexion Cerrada")



def mostrarTodo():
    sql = "SELECT * FROM alumnos;"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    #print(resultados)
    for fila in resultados:
        print("ID: ", fila[0])
        print("Nombre: ",fila[1])
        print("______")



def mostrarUno(id):
    sql = "SELECT * FROM Alumnos WHERE id_alumno='%s';"%(id)
    cursor.execute(sql)
    resultados = cursor.fetchall()

    if (len(resultados) == 0):
        print("No se encontro el ID "+str(id))
    else:
        print(resultados)

def insertar(nombre, apellido, lu, fechaNac):
    sql = "INSERT INTO alumnos(nombre,apellido,lu,fechaNacimiento) VALUES ('%s','%s','%s','%s');"%(nombre, apellido,lu,fechaNac)        
    cursor.execute(sql)
    conexion.commit()
    

#mostrarUno(2)

insertar('Federico','Ramos','218456','200-04-09')

cerrarConexion()