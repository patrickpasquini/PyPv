from ..models.pv_inverter import PvInverter
from ..models.pv_module import PvModule
from math import radians


def average_energy_generation(
    pv_module: PvModule,
    pv_inverter: PvInverter,
    latitude: float,
    orientation: float,
    inclination: float,
    albedo: float,
    extra_losses: float,
    ghr_of_the_months_of_the_year: list[float],
):
    range_of_days_of_the_months_of_the_year = (
        (1, 31),
        (32, 59),
        (60, 90),
        (91, 120),
        (121, 151),
        (152, 181),
        (182, 212),
        (213, 243),
        (244, 273),
        (274, 304),
        (305, 334),
        (335, 365),
    )
    module_area = pv_module.p_max / (pv_module.efficiency * 1000)
    all_losses = pv_module.efficiency * pv_inverter.efficiency * (1 - extra_losses)
    for index, ghr in enumerate(ghr_of_the_months_of_the_year):
        initial_day = range_of_days_of_the_months_of_the_year[index][0]
        final_day = range_of_days_of_the_months_of_the_year[index][1]
