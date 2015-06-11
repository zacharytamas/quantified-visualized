import json
import logging

from dateutil.parser import parse
from google.appengine.api import urlfetch

from models.reporter_report import ReporterReport
from reporter_parsers import (
  BatteryLifeParser,
  AltitudeParser,
  ConnectivityParser
)
from utils.dates import aware_to_utc


class ReporterImporter(object):
  """An Importer for Reporter.app data."""

  MIDDLEWARES = [
    BatteryLifeParser,
    AltitudeParser,
    ConnectivityParser
  ]

  def log(self, s):
    logging.info("I/%s : %s" % (self.__class__.__name__, s))

  def __init__(self, uri):
    self.log("Instantiated")
    self.data = self.getData(uri)
    self.log("Data retrieved successfully")
    self.process()

  def getData(self, uri):
    """Return the Reporter data at a URI. Can be a filepath or a URL."""
    if uri.startswith("http"):
      result = urlfetch.fetch(uri)

      if result.status_code == 200:
        return json.loads(result.content)
      else:  # TODO handle other cases
        pass
    else:  # TODO Implement file.
      pass

  def seenThis(self, report):
    return ReporterReport.get_by_id(report['uniqueIdentifier']) is not None

  def process(self, data=None):
    """Process data into Visualizer objects."""
    if data is None:
      data = self.data

    for report in data:

      if self.seenThis(report):
        self.log("Skipping report, we've seen this before.")
        continue

      moment = self._getDate(report['date'])

      for middleware in self.MIDDLEWARES:
        self.log("Applying %s middleware" % middleware.__name__)
        middleware().onReport(moment, report)

      self.markSeen(moment, report)

  def markSeen(self, moment, report):
    return ReporterReport(id=report.get('uniqueIdentifier'),
                          moment=moment).put()

  def _getDate(self, date_string):
    return aware_to_utc(parse(date_string))
