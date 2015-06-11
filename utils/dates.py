import pytz


def aware_to_utc(date):
  """Accepts an aware Datetime and returns a naive one in UTC."""
  return date.astimezone(pytz.utc).replace(tzinfo=None)
