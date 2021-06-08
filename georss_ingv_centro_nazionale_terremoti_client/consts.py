"""INGV Centro Nazionale Terremoti (Earthquakes) consts."""
from georss_client import CUSTOM_ATTRIBUTE

IMAGE_URL_PATTERN = (
    "http://shakemap.rm.ingv.it/shake4/data/{}/current/products/intensity.jpg"
)

REGEXP_ATTR_MAGNITUDE = r"Magnitude\(M.{{0,3}}\) (?P<{}>[^ ]+) ".format(
    CUSTOM_ATTRIBUTE
)
REGEXP_ATTR_REGION = r"Magnitude\(M.{{0,3}}\) [^ ]+[ ]+-[ ]+(?P<{}>.+)$".format(
    CUSTOM_ATTRIBUTE
)
REGEXP_ATTR_EVENT_ID = r"eventId=(?P<{}>\d+)$".format(CUSTOM_ATTRIBUTE)

URL = "http://cnt.rm.ingv.it/feed/atom/all_week"
