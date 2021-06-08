"""Test for the INGV Centro Nazionale Terremoti feed."""
import datetime
import unittest
from unittest import mock

from georss_client import UPDATE_OK

from georss_ingv_centro_nazionale_terremoti_client import (
    IngvCentroNazionaleTerremotiFeed,
)
from georss_ingv_centro_nazionale_terremoti_client.feed_manager import (
    IngvCentroNazionaleTerremotiFeedManager,
)
from tests import load_fixture

HOME_COORDINATES = (40.84, 14.25)


class TestIngvCentroNazionaleTerremotiFeed(unittest.TestCase):
    """Test the INGV Centro Nazionale Terremoti feed."""

    @mock.patch("requests.Request")
    @mock.patch("requests.Session")
    def test_update_ok(self, mock_session, mock_request):
        """Test updating feed is ok."""
        mock_session.return_value.__enter__.return_value.send.return_value.ok = True
        mock_session.return_value.__enter__.return_value.send.return_value.text = (
            load_fixture("ingv_centro_nazionale_terremoti_feed.xml")
        )

        feed = IngvCentroNazionaleTerremotiFeed(HOME_COORDINATES)
        assert (
            repr(feed) == "<IngvCentroNazionaleTerremotiFeed(home="
            "(40.84, 14.25), url=http://cnt.rm.ingv.it/"
            "feed/atom/all_week, radius=None, "
            "magnitude=None)>"
        )
        status, entries = feed.update()
        assert status == UPDATE_OK
        self.assertIsNotNone(entries)
        assert len(entries) == 3

        feed_entry = entries[0]
        assert (
            feed_entry.title == "2018-10-06 10:21:33 UTC - Magnitude(ML)"
            " 2.3 - 1 km NE Biancavilla (CT)"
        )
        assert (
            feed_entry.external_id == "smi:webservices.ingv.it/fdsnws/"
            "event/1/query?eventId=1234"
        )
        assert feed_entry.event_id == 1234
        assert feed_entry.image_url is None
        assert feed_entry.coordinates == (37.654, 14.878)
        self.assertAlmostEqual(feed_entry.distance_to_home, 358.4, 1)
        assert feed_entry.published == datetime.datetime(
            2018, 10, 6, 8, 0, tzinfo=datetime.timezone.utc
        )
        assert feed_entry.updated == datetime.datetime(
            2018, 10, 6, 8, 30, tzinfo=datetime.timezone.utc
        )
        assert feed_entry.region == "1 km NE Biancavilla (CT)"
        assert feed_entry.magnitude == 2.3
        assert (
            feed_entry.attribution == "Istituto Nazionale di Geofisica "
            "e Vulcanologia"
        )
        assert (
            repr(feed_entry) == "<IngvCentroNazionaleTerremotiFeedEntry"
            "(id=smi:webservices.ingv.it/fdsnws/"
            "event/1/query?eventId=1234)>"
        )

        feed_entry = entries[1]
        assert (
            feed_entry.title == "2018-10-06 09:14:11 UTC - Magnitude(ML)"
            " 0.7 - 1 km NE Norcia (PG)"
        )
        self.assertIsNone(feed_entry.published)

        feed_entry = entries[2]
        assert feed_entry.event_id == 3456
        assert (
            feed_entry.image_url == "http://shakemap.rm.ingv.it/"
            "shake4/data/3456/current/products/intensity.jpg"
        )

    @mock.patch("requests.Request")
    @mock.patch("requests.Session")
    def test_update_ok_with_category(self, mock_session, mock_request):
        """Test updating feed is ok."""
        mock_session.return_value.__enter__.return_value.send.return_value.ok = True
        mock_session.return_value.__enter__.return_value.send.return_value.text = (
            load_fixture("ingv_centro_nazionale_terremoti_feed.xml")
        )

        feed = IngvCentroNazionaleTerremotiFeed(
            HOME_COORDINATES, filter_minimum_magnitude=2.0
        )
        status, entries = feed.update()
        assert status == UPDATE_OK
        self.assertIsNotNone(entries)
        assert len(entries) == 2

        feed_entry = entries[0]
        assert (
            feed_entry.title == "2018-10-06 10:21:33 UTC - Magnitude(ML)"
            " 2.3 - 1 km NE Biancavilla (CT)"
        )
        assert (
            feed_entry.external_id == "smi:webservices.ingv.it/fdsnws/"
            "event/1/query?eventId=1234"
        )

    @mock.patch("requests.Request")
    @mock.patch("requests.Session")
    def test_feed_manager(self, mock_session, mock_request):
        """Test the feed manager."""
        mock_session.return_value.__enter__.return_value.send.return_value.ok = True
        mock_session.return_value.__enter__.return_value.send.return_value.text = (
            load_fixture("ingv_centro_nazionale_terremoti_feed.xml")
        )

        # This will just record calls and keep track of external ids.
        generated_entity_external_ids = []
        updated_entity_external_ids = []
        removed_entity_external_ids = []

        def _generate_entity(external_id):
            """Generate new entity."""
            generated_entity_external_ids.append(external_id)

        def _update_entity(external_id):
            """Update entity."""
            updated_entity_external_ids.append(external_id)

        def _remove_entity(external_id):
            """Remove entity."""
            removed_entity_external_ids.append(external_id)

        feed_manager = IngvCentroNazionaleTerremotiFeedManager(
            _generate_entity, _update_entity, _remove_entity, HOME_COORDINATES
        )
        assert (
            repr(feed_manager) == "<IngvCentroNazionaleTerremoti"
            "FeedManager(feed=<IngvCentroNazionale"
            "TerremotiFeed(home="
            "(40.84, 14.25), "
            "url=http://cnt.rm.ingv.it/"
            "feed/atom/all_week, "
            "radius=None, magnitude=None)>)>"
        )
        feed_manager.update()
        entries = feed_manager.feed_entries
        self.assertIsNotNone(entries)
        assert len(entries) == 3
        assert feed_manager.last_timestamp == datetime.datetime(
            2018, 10, 6, 8, 0, tzinfo=datetime.timezone.utc
        )
        assert len(generated_entity_external_ids) == 3
        assert len(updated_entity_external_ids) == 0
        assert len(removed_entity_external_ids) == 0
