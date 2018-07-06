import webapp2

class HeloWorld(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', HeloWorld)
], debug=True)
