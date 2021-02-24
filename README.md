# hack-busses-gtfs

Currently information about busses is not available on google maps. There are few sources of information which has to be parsed and aggregated for Google Maps. An example for trolleys is [here](https://github.com/roataway/gtfs-data)

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

#### File requirements
The following requirements apply to the format and contents of the dataset files:

All files must be saved as comma-delimited text.
The first line of each file must contain field names. Each subsection of the Field definitions section corresponds to one of the files in a GTFS dataset and lists the field names that may be used in that file.
All field names are case-sensitive.
Field values may not contain tabs, carriage returns or new lines.
Field values that contain quotation marks or commas must be enclosed within quotation marks. In addition, each quotation mark in the field value must be preceded with a quotation mark. This is consistent with the manner in which Microsoft Excel outputs comma-delimited (CSV) files. For more information on the CSV file format, see http://tools.ietf.org/html/rfc4180. The following example demonstrates how a field value would appear in a comma-delimited file:
Original field value: Contains "quotes", commas and text
Field value in CSV file: "Contains ""quotes"", commas and text"
Field values must not contain HTML tags, comments or escape sequences.
Remove any extra spaces between fields or field names. Many parsers consider the spaces to be part of the value, which may cause errors.
Each line must end with a CRLF or LF linebreak character.
Files should be encoded in UTF-8 to support all Unicode characters. Files that include the Unicode byte-order mark (BOM) character are acceptable. See http://unicode.org/faq/utf_bom.html#BOM for more information on the BOM character and UTF-8.
All dataset files must be zipped together.

#### How do I get the data? 

1.    Using this [endpoint](https://nimbus.wialon.com/api/locator/5f59baffc37144a3939d21bd8acc5e45/data) parse and take all the stops + routes and other information.
2.    Using this https://nimbus.wialon.com/api/locator/5f59baffc37144a3939d21bd8acc5e45/online/route/18864 you can take the information for a given route, in our example is route 18864.
3.    Understand all the given information and conclude if it is possible to create trips.txt .








