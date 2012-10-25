#!/usr/bin/env python
import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("template/index.html")

settings={
	"static_path":os.path.join(os.path.dirname(__file__),"static"),
}
app=tornado.web.Application([
	(r"/",MainHandler),
],**settings)

if __name__=="__main__":
	app.listen(8080)
	tornado.ioloop.IOLoop.instance().start()
