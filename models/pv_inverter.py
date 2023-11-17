from pydantic import BaseModel


class PvInverter(BaseModel):
    start_voltage: float
    nominal_voltage: float
    max_voltage: float
    nominal_power: float
    mpp_min_voltage: float
    mpp_max_voltage: float
    max_isc: float
    mppt_qtd: int
