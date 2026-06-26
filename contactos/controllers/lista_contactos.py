import web
import sqlite3
render=web.template.render('views')
class ListaContactos():
    def conectar(self):
        try:
            conexion=sqlite3.connect("sql/agenda.sqlite")
            conexion.row_factory=sqlite3.row
            return conexion
        except Exception as error:
            print(f"error 100:{error.args}")
        return None
    def ListaContactos(self):
        try:
            conexion=self.conectar()
            cursor=conexion.cursor()
            sql="SELECT * FROM contacto"
            cursor.execute(sql)
            contactos=cursor.fetchall()
            return contactos
        except Exception as error:
            print(f"error 101:{error.args}")
        return None
    def GET(self):
        print(self.ListaContactos)
        return render.lista_contactos()