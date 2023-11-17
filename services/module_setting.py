from ..models.pv_module import PvModule

stc_temperature = 25


def voc_adjusted(pv_module: PvModule, min_temperature: float):
    voc = pv_module.voc
    alpha = voc * pv_module.voc_coefficient
    voc_adjusted = voc + (alpha * (min_temperature - stc_temperature))
    return voc_adjusted


def max_vmp_adjusted(pv_module: PvModule, max_temperature: float):
    vmp = pv_module.vmp
    beta = vmp * pv_module.p_max_coefficient
    vmp_adjusted_max_temp = vmp + (beta * (max_temperature - stc_temperature))
    return vmp_adjusted_max_temp


def min_vmp_adjusted(pv_module: PvModule, min_temperature: float):
    vmp = pv_module.vmp
    beta = vmp * pv_module.p_max_coefficient
    vmp_adjusted_min_temp = vmp + (beta * (min_temperature - stc_temperature))
    return vmp_adjusted_min_temp


def isc_adjusted(pv_module: PvModule, max_temperature: float):
    isc = pv_module.isc
    beta = isc * pv_module.isc_coefficient
    isc_adjusted = isc + (beta * (max_temperature - stc_temperature))
    return isc_adjusted
