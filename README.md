# hack-busses-gtfs

# What is GTFS?

The General Transit Feed Specification (GTFS) defines a common format for public transportation schedules and associated geographic information. GTFS "feeds" allow public transit agencies to publish their transit data and developers to write applications that consume that data in an interoperable way.

## How do I start?

1.  Continue reading the overview below.
2.  Take a look at the [GTFS STATIC TROLLEY for Chisinau](https://github.com/roataway/gtfs-data/tree/master/GTFS_static)
3.  Create your own feeds using the [reference](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md) as a guide.
4.  Test your feed using using gtfs validators(check below)





#### GTFS Validators

- [feedValidator](https://github.com/google/transitfeed/wiki/FeedValidator) - Google supported Python-based GTFS validator.
- [gtfs-validator](https://github.com/conveyal/gtfs-validator) - A GTFS validator based on the OneBusAway GTFS Modules, runs in Java and is faster than the Google provided one.
- [gtfs-lib](https://github.com/conveyal/gtfs-lib/) - Conveyal's successor to gtfs-validator, a library for loading and saving GTFS feeds of arbitrary size with disk-backed storage.
- [GTFS Data Package Specification](https://github.com/Stephen-Gates/GTFS) - A [Data Package specification](http://specs.frictionlessdata.io/data-packages/) with validation accomplished with [Good Tables](http://goodtables.okfnlabs.org/). Includes a data package, schemas, tests, and uses South East Queensland GTFS data as an example.
- [Web GTFS Meta-Validator (hosted by Omni)](http://gtfsvalidator.omnimodal.io) - A web-based GTFS validator that runs both [feedValidator](https://github.com/google/transitfeed/wiki/FeedValidator) and [gtfs-validator](https://github.com/conveyal/gtfs-validator) on uploaded GTFS files.
- [gtfs-validator](https://github.com/MobilityData/gtfs-validator) - An open-source GTFS validator implemented in Java licensed under Apache v2.0 maintained by [MobilityData](https://mobilitydata.org/).
- [GTFSVTOR](https://github.com/mecatran/gtfsvtor) - An open-source GTFS validator implemented in Java licensed under GPLv3 maintained by [Mecatran](https://www.mecatran.com/).
- [Transport Validator](https://github.com/etalab/transport-validator/) - An open-source validator implemented in [Rust](https://www.rust-lang.org/). Used by the [French National Access Point](https://transport.data.gouv.fr/validation/).

#### How do I get the data? 

1.Using this [endpoint](https://nimbus.wialon.com/api/locator/5f59baffc37144a3939d21bd8acc5e45/data) parse and take all the stops. 





