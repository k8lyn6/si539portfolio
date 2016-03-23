import webapp2, os, logging, jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class PageHandler(webapp2.RequestHandler):
	def get(self):
		#find path of URL
		path = self.request.path
		#deals with the first run when URL path does not have html file
		if path == '/':
			path = '/about'
		# 	title = 'ABOUT'
		# #all other instances, splits string to find title of page
		# else:
		# 	title = path[1:]
		# 	title = title.upper()
		#logs path name and title to troubleshoot
		logging.info(path)
		# logging.info(title)
		#loads and renders file depending on path variable
		template = JINJA_ENVIRONMENT.get_template('templates' + path + '.html')
		self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', PageHandler),
    ('/.*', PageHandler)
], debug=True)
