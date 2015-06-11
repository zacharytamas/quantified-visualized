#!/usr/bin/env python

import webapp2

from utils.reporter_importer import ReporterImporter


class MainHandler(webapp2.RequestHandler):
  def get(self):
    URI = "https://raw.githubusercontent.com/zacharytamas/quantified-data/master/reporter/2015-06-10.json"

    importer = ReporterImporter(URI)
    self.response.write(importer.data)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
