import tornado.ioloop
import tornado.web

# cookie.niqu.me
class MainHandler(tornado.web.RequestHandler):
    def options(self):
        self.set_header('Access-Control-Allow-Origin', '*')

    def get(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Content-Type', 'application/json')
        self.set_cookie('food', 'rice', '.test.com')
        self.write('{"name": "John"}')

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
