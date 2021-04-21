import xml.etree.ElementTree as ET
import dateutil.parser.parse

from pymetno.error import ParseError


def parse_time_element_into_forecast(time_etree: ET.Element):
    if not time_etree.get('datatype') == 'forecast':
        raise ParseError(f"Expected time element's datatype to be forecast, found {time_etree.get('datatype')}")

    timestamp_from = dateutil.parser.parse(time_etree.get('from'))
    timestamp_to = dateutil.parser.parse(time_etree.get('to'))

    location: ET.Element = time_etree.find('location')


def parse_location_temperature_data(location_etree: ET.Element):
    pass


def parse_location_wind_direction_data(location_etree: ET.Element):
    pass


def parse_location_wind_speed_data(location_etree: ET.Element):
    pass


def parse_location_area_max_wind_speed_data(location_etree: ET.Element):
    pass


def parse_location_humidity_data(location_etree: ET.Element):
    pass


def parse_location_pressure_data(location_etree: ET.Element):
    pass


def parse_location_cloudiness_data(location_etree: ET.Element):
    pass


def parse_location_fog_data(location_etree: ET.Element):
    pass


def parse_location_lowclouds_data(location_etree: ET.Element):
    pass


def parse_location_mediumclouds_data(location_etree: ET.Element):
    pass


def parse_location_highclouds_data(location_etree: ET.Element):
    pass



