from google.appengine.ext import ndb


class Altitude(ndb.Model):
  """A record of the altitude at a moment."""
  moment = ndb.DateTimeProperty()
  floors_ascended = ndb.IntegerProperty()
  gps_raw_altitude = ndb.FloatProperty()
  floors_descended = ndb.IntegerProperty()
  gps_altitude_from_location = ndb.FloatProperty()
  pressure = ndb.FloatProperty()
  adjusted_pressure = ndb.FloatProperty()
