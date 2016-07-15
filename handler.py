#coding:utf-8
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
    	mode = 1
        self.render("test.html", mode=mode)

class QueryHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("query.html")

class AjaxHandler(tornado.web.RequestHandler):
	def post(self):
		if(self.get_argument("message")=="1"):
			chosen="right"
		elif(self.get_argument("message")=="0"):
			chosen="Please choose one"
		else:
			chosen="wrong"
		self.write(chosen)
   
