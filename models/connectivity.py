from google.appengine.ext import ndb


class Connectivity(ndb.Model):
  """A record of my connectivity at a moment."""
  moment = ndb.DateTimeProperty()
  connected = ndb.BooleanProperty()
  on_wifi = ndb.BooleanProperty()
  on_cellular = ndb.BooleanProperty()
