from google.appengine.ext import ndb


class ReporterReport(ndb.Model):
  """A record of a Reporter Report that we processed."""
  moment = ndb.DateTimeProperty()
  processed_date = ndb.DateTimeProperty(auto_now_add=True)
