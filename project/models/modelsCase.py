from bd import Conection
import bcrypt
class User():
    def __init__(self):
        print('model user')
        self.conn=Conection()
        self.cursor=self.conn.getCursor()
    def getUserAll(self):
        data=self.cursor.execute('select * from USUARIOS').fetchall()
        return data
    def getUser(self,id):
        sentence=f"SELECT * FROM USUARIOS WHERE USUARIO='{id}'"
        data=self.cursor.execute(sentence).fetchone()
        return data
    def insertUser(self,dataTuple):
        inserSentence="INSERT INTO USUARIOS(USUARIO,PASSWORD,EMAIL,FULLNAME,TIPOUSUARIO) VALUES(?,?,?,?,?)"
        self.cursor.execute(inserSentence,dataTuple)
        self.conn.con.commit()
        print('data insertada')

class TipoDeCambio:
    def __init__(self):
        print('model user')
        self.conn=Conection()
        self.cursor=self.conn.getCursor()
    def insertData(self,data):
        insertSentence="INSERT INTO NOMBRE_TABLA(PA1,PA2,P3) VALUES(?,?,?)"
        self.cursor.execute(insertSentence,data)


class Cliente:
    pass

class Vendedor:
    pass

class Producto:
    pass

class Categoria:
    pass

class Venta:
    pass
# models.venta
