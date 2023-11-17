from ..models.pv_module import PvModule
from ..models.pv_inverter import PvInverter
from .module_setting import (
    isc_adjusted,
    min_vmp_adjusted,
    max_vmp_adjusted,
    voc_adjusted,
)
from math import floor, ceil


def available_strings_per_mppt(
    pv_module: PvModule, pv_inverter: PvInverter, max_temperature: float
):
    isc = isc_adjusted(pv_module, max_temperature)
    return floor(pv_inverter.max_isc / isc)


def ideal_modules_quantity(
    pv_module: PvModule, pv_inverter: PvInverter, max_temperature: float
):
    vmp = max_vmp_adjusted(pv_module, max_temperature)
    return floor(pv_inverter.nominal_voltage / vmp)


def min_modules_per_string(
    pv_module: PvModule, pv_inverter: PvInverter, max_temperature: float
):
    vmp = max_vmp_adjusted(pv_module, max_temperature)
    return ceil(pv_inverter.mpp_min_voltage / vmp)


def max_modules_per_string(
    pv_module: PvModule, pv_inverter: PvInverter, min_temperature: float
):
    voc = voc_adjusted(pv_module, min_temperature)
    vmp = min_vmp_adjusted(pv_module, min_temperature)
    mpp_ref = floor(pv_inverter.mpp_max_voltage / vmp)
    inverter_ref = floor(pv_inverter.max_voltage / voc)
    if mpp_ref > inverter_ref:
        return inverter_ref
    return mpp_ref
