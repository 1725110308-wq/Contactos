import web
urls = (
    '/','controllers.index.Index',
    '/borrar_contacto/(.*)','controllers.borrar_contacto.Borrar_contacto',
    '/lista_contactos','controllers.lista_contactos.ListaContactos',
    '/modificar_contacto/(.*)','controllers.modificar_contacto.Modificar_contacto',
    '/ver_contacto/(.*)','controllers.ver_contactos.Ver_contactos',
    '/insertar_contacto/(.*)','controllers.insertar_contacto.Insertar_contacto'
)
app = web.application(urls,globals())
if __name__=='__main__':
    web.config.debug = True
    app.run()
    #select * from contacto where id_contacto=1