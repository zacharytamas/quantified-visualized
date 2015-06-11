from google.appengine.ext import ndb


class BatteryLife(ndb.Model):
  """The current battery status of a device."""
  moment = ndb.DateTimeProperty()
  value = ndb.IntegerProperty()
