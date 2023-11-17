from math import radians, sin, cos, tan, acos, pi


def solar_declination(day):
    """
    Calculates the solar declination for a given day of the year.

    :param day: Day of the year (1 to 365, or 366 in leap years).
    :return: Solar declination in radians.

    Solar declination is the angle between the sun's rays and the Earth's equatorial plane.
    It varies throughout the year due to the Earth's axial tilt.
    """

    max_tilt = radians(23.45)
    declination = max_tilt * sin(2 * pi * ((284 + day) / 365))
    return declination


def sunset_angle(latitude, solar_declination):
    """
    Calculates the sunset angle (ws) based on latitude and solar declination.

    :param latitude_deg: Latitude in degrees.
    :param solar_declination_deg: Solar declination in degrees.
    :return: Sunset angle in radians.
    """

    cos_ws = -tan(latitude) * tan(solar_declination)
    if cos_ws >= 1:
        ws = 0
    elif cos_ws <= -1:
        ws = pi
    else:
        ws = acos(cos_ws)
    return ws
