import web
import sqlite3
render = web.template.render('views', base='layout')
class Insertar_contacto():
    def insertarContacto(self,contacto:dict)->bool:
        try:
            conexion = sqlite3.connect("sql/agenda.sqlite")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()

            nombre = contacto["nombre"]
            primer_apellido = contacto["primer_apellido"]
            segundo_apellido = contacto["segundo_apellido"]
            email = contacto["email"]
            telefono = contacto["telefono"]

            query = """INSERT INTO contacto(nombre, primer_apellido, segundo_apellido,
                        email, telefono)
                      VALUES(?,?,?,?,?)"""
            datos = (
                nombre,
                primer_apellido,
                segundo_apellido,
                email,
                telefono,
            )
            cursor.execute(query, datos)
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.Error as error:
            print(f"Error 1: {error.args}")
            return False
        except Exception as errror:
            print(f"Error 2: {errror.args}")
            return False

    def POST(self):
        formulario=web.input()
        contacto = {
            #"id_contacto":formulario['id_contacto'],
            "nombre":formulario['nombre'],
            "primer_apellido":formulario['primer_apellido'],
            "segundo_apellido":formulario['segundo_apellido'],
            "email":formulario['email'],
            "telefono":formulario['telefono']
        }
        resultado=self.insertarContacto(contacto)
        web.ctx.status = '303 See Other'
        web.header('Location', '/lista_contactos')
        return ''

    def GET(self):
        nombre=""
        primer_apellido=""
        segundo_apellido=""
        email=""
        telefono=""
        return render.insertar_contacto(nombre,primer_apellido,segundo_apellido,email,telefono)