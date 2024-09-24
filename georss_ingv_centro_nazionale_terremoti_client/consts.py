"""INGV Centro Nazionale Terremoti (Earthquakes) consts."""

from georss_client import CUSTOM_ATTRIBUTE

IMAGE_URL_PATTERN = (
    "http://shakemap.rm.ingv.it/shake4/data/{}/current/products/intensity.jpg"
)

REGEXP_ATTR_MAGNITUDE = rf"Magnitude\(M.{{0,3}}\) (?P<{CUSTOM_ATTRIBUTE}>[^ ]+) "
REGEXP_ATTR_REGION = (
    rf"Magnitude\(M.{{0,3}}\) [^ ]+[ ]+-[ ]+(?P<{CUSTOM_ATTRIBUTE}>.+)$"
)
REGEXP_ATTR_EVENT_ID = rf"eventId=(?P<{CUSTOM_ATTRIBUTE}>\d+)$"

URL = "http://cnt.rm.ingv.it/feed/atom/all_week"
