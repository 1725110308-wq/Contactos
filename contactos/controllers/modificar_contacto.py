import web
render=web.template.render('views', base='layout')
class Modificar_contacto():
    def GET(self):
        return render.modificar_contacto()