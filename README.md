# python-georss-ingv-centro-nazionale-terremoti-client

[![Build Status](https://github.com/exxamalte/python-georss-ingv-centro-nazionale-terremoti-client/workflows/CI/badge.svg?branch=master)](https://github.com/exxamalte/python-georss-ingv-centro-nazionale-terremoti-client/actions?workflow=CI)
[![codecov](https://codecov.io/gh/exxamalte/python-georss-ingv-centro-nazionale-terremoti-client/branch/master/graph/badge.svg?token=PHASSFXFVU)](https://codecov.io/gh/exxamalte/python-georss-ingv-centro-nazionale-terremoti-client)
[![PyPi](https://img.shields.io/pypi/v/georss-ingv-centro-nazionale-terremoti-client.svg)](https://pypi.python.org/pypi/georss-ingv-centro-nazionale-terremoti-client)
[![Version](https://img.shields.io/pypi/pyversions/georss-ingv-centro-nazionale-terremoti-client.svg)](https://pypi.python.org/pypi/georss-ingv-centro-nazionale-terremoti-client)

This library provides convenient access to the [INGV Centro Nazionale Terremoti (Earthquakes) Feed](http://cnt.rm.ingv.it/).

## Installation
`pip install georss-ingv-centro-nazionale-terremoti-client`

## Usage
See below for an example of how this library can be used. After instantiating 
the feed class and supplying the required parameters, you can call `update` to 
retrieve the feed data. The return value will be a tuple of a status code and 
the actual data in the form of a list of specific feed entries.

**Status Codes**
* _UPDATE_OK_: Update went fine and data was retrieved. The library may still return empty data, for example because no entries fulfilled the filter criteria.
* _UPDATE_OK_NO_DATA_: Update went fine but no data was retrieved, for example because the server indicated that there was not update since the last request.
* _UPDATE_ERROR_: Something went wrong during the update

**Supported Filters**

| Filter            |                            | Description |
|-------------------|----------------------------|-------------|
| Radius            | `filter_radius`            | Radius in kilometers around the home coordinates in which events from feed are included. |
| Minimum Magnitude | `filter_minimum_magnitude` | Minimum magnitude as float value. Only events with a magnitude equal or above this value are included. |

**Example**
```python
from georss_ingv_centro_nazionale_terremoti_client import \
    IngvCentroNazionaleTerremotiFeed
# Home Coordinates: Latitude: 40.84, Longitude: 14.25
# Filter radius: 200 km
# Filter minimum magnitude: 4.0
feed = IngvCentroNazionaleTerremotiFeed((40.84, 14.25), 
                                        filter_radius=200, 
                                        filter_minimum_magnitude=4.0)
status, entries = feed.update()
```

## Feed Manager

The Feed Manager helps managing feed updates over time, by notifying the 
consumer of the feed about new feed entries, updates and removed entries 
compared to the last feed update.

* If the current feed update is the first one, then all feed entries will be 
  reported as new. The feed manager will keep track of all feed entries' 
  external IDs that it has successfully processed.
* If the current feed update is not the first one, then the feed manager will 
  produce three sets:
  * Feed entries that were not in the previous feed update but are in the 
    current feed update will be reported as new.
  * Feed entries that were in the previous feed update and are still in the 
    current feed update will be reported as to be updated.
  * Feed entries that were in the previous feed update but are not in the 
    current feed update will be reported to be removed.
* If the current update fails, then all feed entries processed in the previous
  feed update will be reported to be removed.

After a successful update from the feed, the feed manager will provide two
different dates:

* `last_update` will be the timestamp of the last successful update from the
  feed. This date may be useful if the consumer of this library wants to
  treat intermittent errors from feed updates differently.
* `last_timestamp` will be the latest timestamp extracted from the feed data. 
  This requires that the underlying feed data actually contains a suitable 
  date. This date may be useful if the consumer of this library wants to 
  process feed entries differently if they haven't actually been updated.
