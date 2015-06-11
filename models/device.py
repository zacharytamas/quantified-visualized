from google.appengine.ext import ndb


class Device(ndb.model):
  name = ndb.StringProperty()
