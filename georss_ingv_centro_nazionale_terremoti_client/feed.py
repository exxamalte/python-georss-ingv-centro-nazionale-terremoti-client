"""INGV Centro Nazionale Terremoti (Earthquakes) feed."""

from __future__ import annotations

from georss_client import ATTR_ATTRIBUTION, GeoRssFeed

from .consts import URL
from .feed_entry import IngvCentroNazionaleTerremotiFeedEntry


class IngvCentroNazionaleTerremotiFeed(GeoRssFeed):
    """INGV Centro Nazionale Terremoti feed."""

    def __init__(
        self,
        home_coordinates: tuple[float, float],
        filter_radius: float | None = None,
        filter_minimum_magnitude: float | None = None,
    ):
        """Initialise this service."""
        super().__init__(home_coordinates, URL, filter_radius=filter_radius)
        self._filter_minimum_magnitude = filter_minimum_magnitude

    def __repr__(self):
        """Return string representation of this feed."""
        return f"<{self.__class__.__name__}(home={self._home_coordinates}, url={self._url}, radius={self._filter_radius}, magnitude={self._filter_minimum_magnitude})>"

    def _new_entry(self, home_coordinates, rss_entry, global_data):
        """Generate a new entry."""
        attribution = (
            None
            if not global_data and ATTR_ATTRIBUTION not in global_data
            else global_data[ATTR_ATTRIBUTION]
        )
        return IngvCentroNazionaleTerremotiFeedEntry(
            home_coordinates, rss_entry, attribution
        )

    def _filter_entries(self, entries):
        """Filter the provided entries."""
        entries = super()._filter_entries(entries)
        if self._filter_minimum_magnitude:
            # Return only entries that have an actual magnitude value, and
            # the value is equal or above the defined threshold.
            return list(
                filter(
                    lambda entry: entry.magnitude
                    and entry.magnitude >= self._filter_minimum_magnitude,
                    entries,
                )
            )
        return entries
