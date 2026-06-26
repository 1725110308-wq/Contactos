import web
render=web.template.render('views')
class Ver_contactos():
    def GET(self):
        return render.ver_contactos()