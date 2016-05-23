import cherrypy
import os, os.path


class CardServer(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

    @cherrypy.expose
    def hello(self):
        return 'hello'


if __name__ == '__main__':
    cherrypy.config.update('server.conf')
    webapp = CardServer()
    cherrypy.quickstart(webapp, '/', 'app.conf')
