import web
urls = (
    '/','controllers.index.Index',
    '/','controllers.borrar_contacto.Borrar_contacto',
    '/','controllers.insertar_contacto.Insertar_contacto',
    '/lista_contactos','controllers.lista_contactos.ListaContactos',
    '/','controllers.modificar_contacto.Modificar_contacto',
    '/ver_contacto/(.*)','controllers.ver_contactos.Ver_contactos',
)
app = web.application(urls,globals())
if __name__=='__main__':
    app.run()
    #select * from contacto where id_contacto=1