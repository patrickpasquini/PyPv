from pydantic import BaseModel, model_validator


class PvModule(BaseModel):
    p_max: float
    vmp: float
    imp: float
    voc: float
    isc: float
    efficiency: float
    p_max_coefficient: float
    voc_coefficient: float
    isc_coefficient: float

    @model_validator(mode="before")
    def adjust_values(values):
        values["p_max"] = values["p_max"] / 1000
        percent_fields = [
            "efficiency",
            "p_max_coefficient",
            "voc_coefficient",
            "isc_coefficient",
        ]
        for field in percent_fields:
            values[field] = values[field] / 100
        return values
