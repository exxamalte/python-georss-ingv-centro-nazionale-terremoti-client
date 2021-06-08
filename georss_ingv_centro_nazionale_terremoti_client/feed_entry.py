"""INGV Centro Nazionale Terremoti (Earthquakes) feed entry."""
from typing import Optional, Tuple

from georss_client import FeedEntry

from .consts import (
    IMAGE_URL_PATTERN,
    REGEXP_ATTR_EVENT_ID,
    REGEXP_ATTR_MAGNITUDE,
    REGEXP_ATTR_REGION,
)


class IngvCentroNazionaleTerremotiFeedEntry(FeedEntry):
    """INGV Centro Nazionale Terremoti feed entry."""

    def __init__(self, home_coordinates: Tuple[float, float], rss_entry, attribution):
        """Initialise this service."""
        super().__init__(home_coordinates, rss_entry)
        self._attribution = attribution

    @property
    def attribution(self) -> str:
        """Return the attribution of this entry."""
        return self._attribution

    @property
    def magnitude(self) -> Optional[float]:
        """Return the magnitude of this entry."""
        magnitude = self._search_in_title(REGEXP_ATTR_MAGNITUDE)
        if magnitude:
            magnitude = float(magnitude)
        return magnitude

    @property
    def region(self) -> Optional[float]:
        """Return the region of this entry."""
        return self._search_in_title(REGEXP_ATTR_REGION)

    @property
    def event_id(self) -> Optional[int]:
        """Return the event id of this entry."""
        event_id = self._search_in_external_id(REGEXP_ATTR_EVENT_ID)
        if event_id:
            return int(event_id)
        return None

    @property
    def image_url(self) -> Optional[str]:
        """Return the image url of this entry."""
        if self.event_id and self.magnitude >= 3:
            return IMAGE_URL_PATTERN.format(self.event_id)
        return None
