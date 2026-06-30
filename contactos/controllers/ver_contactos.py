import web
render = web.template.render('views', base='layout')
class Ver_contactos():
    def GET(self, id_contacto):
        print(f"id contacto: {id_contacto}")
        return render.ver_contacto()