"""INGV Centro Nazionale Terremoti (Earthquakes) feed manager."""
from typing import Tuple

from georss_client.feed_manager import FeedManagerBase

from .feed import IngvCentroNazionaleTerremotiFeed


class IngvCentroNazionaleTerremotiFeedManager(FeedManagerBase):
    """Feed Manager for INGV Centro Nazionale Terremoti feed."""

    def __init__(
        self,
        generate_callback,
        update_callback,
        remove_callback,
        coordinates: Tuple[float, float],
        filter_radius: float = None,
        filter_minimum_magnitude: float = None,
    ):
        """Initialize the INGV Centro Nazionale Terremoti Feed Manager."""
        feed = IngvCentroNazionaleTerremotiFeed(
            coordinates,
            filter_radius=filter_radius,
            filter_minimum_magnitude=filter_minimum_magnitude,
        )
        super().__init__(feed, generate_callback, update_callback, remove_callback)
