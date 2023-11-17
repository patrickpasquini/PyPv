from pydantic import BaseModel, model_validator


class PvInverter(BaseModel):
    start_voltage: float
    nominal_voltage: float
    max_voltage: float
    nominal_power: float
    mpp_min_voltage: float
    mpp_max_voltage: float
    max_isc: float
    mppt_qtd: int
    efficiency: float

    @model_validator(mode="before")
    def adjust_values(values):
        values["efficiency"] = values["efficiency"] / 100
