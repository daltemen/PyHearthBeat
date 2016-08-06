import json
import timeit
import datetime
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
 
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    clients = []
    def open(self):
        print ('new connection')
        self.write_message("Hello World")
        WebSocketHandler.clients.append(self)

    def on_message(self, message):
        print ('message received %s' % message)
        print ("el mensaje llego a las:")
        print (datetime.datetime.now().strftime("%H:%M:%S:%f"))

        start = timeit.default_timer()

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
            (r'/websocket', WebSocketHandler)
        ]
 
        tornado.web.Application.__init__(self, handlers)
  
  
if __name__ == '__main__':
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(3000)
    tornado.ioloop.IOLoop.instance().start()
