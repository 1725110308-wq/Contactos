import web
import sqlite3
render = web.template.render('views', base='layout')
class Insertar_contacto():
    def añadirContacto(self)-> bool:
        try:
            onexion = sqlite3.connect("sql/agenda.sqlite")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query="""INSERT INTO contacto(nombre,primer_apellido,segundo_apellido,
                                          email,telefono)
                    values(?,?,?,?,?);
            """
            datos=(nombre,
                   primer_apellido,
                   segundo_apellido,
                   email,
                   telefono
            )
            cursor.execute(query,datos)
            conexion.commit()
            return True
        except sqlite3.error as
    def GET(self):
        return render.insertar_contacto()