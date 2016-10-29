from dc_base_scrapers.geojson_scraper import RandomIdGeoJSONScraper


stations_url = "http://inspire.misoportal.com/geoserver/hastings_borough_council_hbc_0015_polling_stations_2015_10_27/ows?service=WFS&version=1.1.1&request=GetFeature&outputFormat=json&srsName=EPSG%3A4326&typeNames=hastings_borough_council_hbc_0015_polling_stations_2015_10_27"
districts_url = "http://inspire.misoportal.com/geoserver/hastings_borough_council_hbc_0014_polling_districts_2015_10_27/ows?service=WFS&version=1.1.1&request=GetFeature&outputFormat=json&srsName=EPSG%3A4326&typeNames=hastings_borough_council_hbc_0014_polling_districts_2015_10_27"
council_id = 'E07000062'


stations_scraper = RandomIdGeoJSONScraper(stations_url, council_id, 'utf-8', 'stations')
stations_scraper.scrape()
districts_scraper = RandomIdGeoJSONScraper(districts_url, council_id, 'utf-8', 'districts')
districts_scraper.scrape()
