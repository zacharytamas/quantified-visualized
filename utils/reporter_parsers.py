import logging

from models.battery_life import BatteryLife
from models.altitude import Altitude
from models.connectivity import Connectivity


class ReporterParser(object):
  def log(self, s):
    logging.info("I/%s : %s" % (self.__class__.__name__, s))


class BatteryLifeParser(ReporterParser):

  def onReport(self, moment, report):
    # Battery data comes as a float such as 0.87 for 87%. Let's store
    # it as an Integer.
    battery_percent = report.get('battery') * 100
    BatteryLife(moment=moment,
                value=int(battery_percent)
                ).put()
    self.log('Stored data for BatteryLife: %d%% at %s' % (
             battery_percent, str(moment)))


class AltitudeParser(ReporterParser):

  def onReport(self, moment, report):
    data = report.get('altitude')

    Altitude(id=data.get('uniqueIdentifier'),
             moment=moment,
             floors_ascended=data.get('floorsAscended'),
             gps_raw_altitude=data.get('gpsRawAltitude'),
             floors_descended=data.get('floorsDescended'),
             gps_altitude_from_location=data.get('gpsAltitudeFromLocation'),
             pressure=data.get('pressure'),
             adjusted_pressure=data.get('adjustedPressure')
             ).put()
    self.log("Stored data for Altitude from " + str(moment))


class ConnectivityParser(ReporterParser):

  def onReport(self, moment, report):
    data = report.get('connection')
    Connectivity(id=report.get('uniqueIdentifier'),
                 moment=moment,
                 on_wifi=(data == 1),
                 on_cellular=(data == 0),
                 connected=(data != 2)).put()
    self.log("Stored Conectivity data")
