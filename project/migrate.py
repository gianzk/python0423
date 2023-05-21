import sqlite3
from bd import Conection
#conn=sqlite3.connect('tienda.db')
conn=Conection()
cursor_obj = conn.con.cursor()
cursor_obj.execute("DROP TABLE IF EXISTS USUARIOS")
table = """ CREATE TABLE USUARIOS (
            ID  INTEGER PRIMARY KEY AUTOINCREMENT,
            USUARIO VARCHAR(25) NOT NULL,
            PASSWORD VARCHAR(255),
            EMAIL VARCHAR(255),
            FULLNAME VARCHAR(25) ,
            TIPOUSUARIO VARCHAR(25)
        ); """

cursor_obj.execute(table)
cursor_obj.execute("DROP TABLE IF EXISTS PRODUCTOS")
table = """ CREATE TABLE PRODUCTOS (
            ID  INTEGER PRIMARY KEY AUTOINCREMENT,
            NAMEPRODUCT VARCHAR(255) NOT NULL,
            PRICE VARCHAR(20) NOT NULL, 
            CATEGORIA VARCHAR(25) NOT NULL,
            STCOKACTUAL INT,
            CREACTION_PRODUCT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UPDATE_PRODUCT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ); """
cursor_obj.execute(table)
cursor_obj.execute("DROP TABLE IF EXISTS VENTA")

table=""" CREATE TABLE VENTA (
            ORDERID  INTEGER PRIMARY KEY AUTOINCREMENT,
            PRODUCTID INT, 
            CANTIDAD INT,
            PRICETOTAL VARCHAR(25) NOT NULL,
            CLIENT VARCHAR(25),
            CREACTION_VENTA TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UPDATE_VENTA TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ); """

cursor_obj.execute(table)

# 1.crear un tabla tipo de cambio <id,tipo_dolar(DOUBLE)>


# comentamos las insercciones ya que solo sera parte de la creacion de tablas
""" insert =" INSERT INTO USUARIOS(USUARIO,PASSWORD,EMAIL,FULLNAME,SCORE,TIPOUSUARIO) VALUES('admin','admin','admin@datux.com','admin datux',0,'admin')"

conn.execute(insert)
insert =" INSERT INTO USUARIOS(USUARIO,PASSWORD,EMAIL,FULLNAME,SCORE,TIPOUSUARIO) VALUES('cliente','cliente','email','cliente',0,'cliente')"
conn.execute(insert)


print("Table is Ready")

print("ingrese valores")
nameProduct=input('ingrese el nombre del producto')
price=input('ingrese el PRICE:')
categria=input('ingrese el CATEGORIA:')
stock=int(input('ingrese el STCOKACTUAL:'))

insert="INSERT INTO PRODUCTOS(NAMEPRODUCT,PRICE,CATEGORIA,STCOKACTUAL) VALUES(?,?,?,?);"
data=(nameProduct,price,categria,stock)
conn.execute(insert,data)
"""

conn.con.commit()