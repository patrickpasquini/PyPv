# import math
# from datetime import datetime


# class SolarPhysics:
#     def solar_position(
#         self, latitude: float, longitude: float, date_time: datetime
#     ) -> tuple:
#         """
#         Calculate the solar position, including solar zenith angle and azimuth.

#         Args:
#             latitude (float): Latitude of the location in degrees.
#             longitude (float): Longitude of the location in degrees.
#             date_time (datetime): The date and time for which to calculate the solar position.

#         Returns:
#             tuple: Solar zenith angle and azimuth in degrees.
#         """
#         lat_rad = math.radians(latitude)
#         day_of_year = date_time.timetuple().tm_yday
#         b = 2 * math.pi * (day_of_year - 81) / 364
#         eot = 9.87 * math.sin(2 * b) - 7.53 * math.cos(b) - 1.5 * math.sin(b)
#         tst = (
#             date_time.hour * 60
#             + date_time.minute
#             + 4 * (longitude - 15 * date_time.hour)
#             + eot
#         )
#         h = math.radians((tst / 4) - 180)
#         declination = 23.45 * math.sin(math.radians((360 / 365) * (day_of_year - 81)))
#         sin_theta_z = math.sin(lat_rad) * math.sin(
#             math.radians(declination)
#         ) + math.cos(lat_rad) * math.cos(math.radians(declination)) * math.cos(h)
#         theta_z = math.acos(min(max(sin_theta_z, -1), 1))
#         sin_az = -(math.sin(h) * math.cos(math.radians(declination))) / math.cos(
#             theta_z
#         )
#         cos_az = (
#             math.sin(math.radians(declination)) - math.sin(lat_rad) * math.sin(theta_z)
#         ) / (math.cos(lat_rad) * math.cos(theta_z))
#         az = math.atan2(sin_az, cos_az)
#         az = az + math.pi if az < 0 else az
#         return math.degrees(theta_z), math.degrees(az)

#     def angle_incidence(
#         self,
#         solar_zenith: float,
#         solar_azimuth: float,
#         surface_tilt: float,
#         surface_azimuth: float,
#     ) -> float:
#         """
#         Calculate the angle of incidence of solar radiation on an inclined surface.

#         Args:
#             solar_zenith (float): Solar zenith angle in degrees.
#             solar_azimuth (float): Solar azimuth angle in degrees.
#             surface_tilt (float): Tilt of the surface in degrees (angle from the horizontal plane).
#             surface_azimuth (float): Azimuth of the surface in degrees (angle from the north).

#         Returns:
#             float: Angle of incidence in degrees.
#         """
#         solar_zenith_rad = math.radians(solar_zenith)
#         solar_azimuth_rad = math.radians(solar_azimuth)
#         surface_tilt_rad = math.radians(surface_tilt)
#         surface_azimuth_rad = math.radians(surface_azimuth)
#         cos_incidence = math.cos(solar_zenith_rad) * math.cos(
#             surface_tilt_rad
#         ) + math.sin(solar_zenith_rad) * math.sin(surface_tilt_rad) * math.cos(
#             solar_azimuth_rad - surface_azimuth_rad
#         )
#         angle_incidence_rad = math.acos(min(max(cos_incidence, -1), 1))
#         return math.degrees(angle_incidence_rad)

#     def kt(self, ghr: float, solar_zenith: float) -> float:
#         """
#         Calculate the clearness index based on Global Horizontal Radiation and zenith angle.

#         Args:
#             ghr (float): Global Horizontal Radiation in W/m².
#             solar_zenith (float): Solar zenith angle in degrees.

#         Returns:
#             float: Clearness index.
#         """
#         zenith_rad = math.radians(solar_zenith)
#         return ghr / (1367 * math.cos(zenith_rad))

#     def dni(self, kt: float, ghr: float) -> float:
#         """
#         Estimate the Direct Normal Irradiance (DNI) using the clearness index and GHR.

#         Args:
#             kt (float): Clearness index.
#             ghr (float): Global Horizontal Radiation in W/m².

#         Returns:
#             float: Estimated Direct Normal Irradiance in W/m².
#         """
#         if kt <= 0.22:
#             dni = ghr / (1 - 0.09 * kt)
#         elif kt > 0.22 and kt <= 0.8:
#             dni = ghr / (
#                 0.9511 - 0.1604 * kt + 4.388 * kt**2 - 16.638 * kt**3 + 12.336 * kt**4
#             )
#         else:
#             dni = ghr / (0.165)
#         return dni

#     def direct_irradiance(self, dni: float, angle_incidence: float) -> float:
#         """
#         Calculate the direct solar irradiance on a tilted surface.

#         Args:
#             dni (float): Direct Normal Irradiance in W/m².
#             angle_incidence (float): Angle of incidence in degrees.

#         Returns:
#             float: Direct horizontal solar irradiance in W/m².
#         """
#         angle_incidence_rad = math.radians(angle_incidence)
#         return abs(dni * math.cos(angle_incidence_rad))

#     def diffuse_irradiance(self, dhi: float, surface_tilt: float) -> float:
#         """
#         Calculate the diffuse solar irradiance.

#         Args:
#             dhi (float): Diffuse Horizontal Irradiance in W/m².
#             surface_tilt (float): Tilt of the surface in degrees.

#         Returns:
#             float: Diffuse solar irradiance in W/m².
#         """
#         surface_tilt_rad = math.radians(surface_tilt)
#         return dhi * (1 + math.cos(surface_tilt_rad)) / 2

#     def reflected_irradiance(
#         self,
#         ghr: float,
#         albedo: float,
#         surface_tilt: float,
#     ) -> float:
#         """
#         Calculate the reflected solar irradiance based on GHR, albedo, and surface tilt.

#         Args:
#             ghr (float): Global Horizontal Radiation in W/m².
#             albedo (float): Reflectivity of the surrounding surface.
#             surface_tilt (float): Tilt of the surface in degrees.

#         Returns:
#             float: Reflected solar irradiance in W/m².
#         """
#         return ghr * albedo * (1 - math.cos(math.radians(surface_tilt))) / 2
