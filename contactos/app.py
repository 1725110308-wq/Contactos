import web
urls = (
    '/','controllers.index.Index',
    '/borrar_contacto/(.*)','controllers.borrar_contacto.BorrarContacto',
    '/lista_contactos','controllers.lista_contactos.ListaContactos',
    '/modificar_contacto/(.*)','controllers.modificar_contacto.ModificarContacto',
    '/ver_contacto/(.*)','controllers.ver_contactos.VerContactos',
    '/insertar_contacto','controllers.insertar_contacto.InsertarContacto'
)
app = web.application(urls,globals())
if __name__=='__main__':
    web.config.debug = True
    app.run()
    #select * from contacto where id_contacto=1