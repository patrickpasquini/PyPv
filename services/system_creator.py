from ..models.pv_inverter import PvInverter
from ..models.pv_module import PvModule
from ..models.land_type import LandType, land_properties
from .inverter_setting import (
    available_strings_per_mppt,
    ideal_modules_quantity,
    min_modules_per_string,
    max_modules_per_string,
)


def system_creator(
    pv_module: PvModule,
    pv_inverter: PvInverter,
    min_temperature: float,
    max_temperature: float,
    land_type: LandType = "urban",
):
    string_qtd = available_strings_per_mppt(pv_module, pv_inverter, max_temperature)
    ideal_qtd = ideal_modules_quantity(pv_module, pv_inverter, max_temperature)
    min_qtd = min_modules_per_string(pv_module, pv_inverter, max_temperature)
    max_qtd = max_modules_per_string(pv_module, pv_inverter, min_temperature)
    breakpoint()
