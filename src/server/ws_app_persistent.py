from tornado import gen, web
import json
import timeit
import datetime
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import pymongo
from bson.json_util import dumps

#EJEMPLO DE POST Y GET COMUN Y CORRIENTE CON MONGO
# Aqui la idea es hacer los gets para trabajar la
#información guardada
class DataHandler(tornado.web.RequestHandler):
	def check_origin(self, origin):
		return True

	def get(self):
		db = self.application.database
		self.write(dumps(db.prueba.find()))

	def post(self):
		#self.get_argument('anArg')
		pass

#Maneja el Index
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index_p.html")

#EJEMPLO DE PUSH LUEGO DE CAPTURAR UN DATO DE LA 
#BASE DE DATOS EN TIEMPO REAL
class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    clients = []
    def open(self):
    	print ('new connection')
    	self.write_message("Hello World")
    	WebSocketHandler.clients.append(self)

    def on_message(self, message):
    	#Se puede deseralizar el objeto insertarlo
    	#al mongo y  
    	#retornalo al write_message
        print ('message received %s' % message)
        print ("el mensaje llego a las:")
        print (datetime.datetime.now().strftime("%H:%M:%S:%f"))

        start = timeit.default_timer()

        #Declara la conexión a mongo
        db = self.application.database
        #Llama al respectivo query de la coleccion prueba
        query = db.prueba.find()
        #Imprime el query por consola
        print (dumps(query))
        #aqui deberia el message insertarse a la coleccion de 
        #mongo

        #self.write_message(u"Your message was: " + message)
        msg = json.loads(message)
        for c in WebSocketHandler.clients:
            if c != self:
                c.write_message(msg)

        stop = timeit.default_timer()

        print (stop - start)

    def on_close(self):
        print ('connection closed')
        WebSocketHandler.clients.remove(self)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/data', DataHandler),
            (r'/websocket', WebSocketHandler)
        ]
        self.con = pymongo.MongoClient()
        #conexion con la base de datos prueba de Mongo
        self.database = self.con["prueba"]
        tornado.web.Application.__init__(self, handlers, debug=True)

if __name__ == '__main__':
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(3000)
    tornado.ioloop.IOLoop.instance().start()