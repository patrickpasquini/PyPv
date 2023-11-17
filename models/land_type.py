from pydantic import BaseModel, field_validator
from typing import Literal


class LandType(BaseModel):
    land: Literal["desert", "farm", "urban", "flooded_area"]

    @field_validator("land")
    def check_land(cls, v):
        valid_land = ["desert", "farm", "urban", "flooded_area"]
        error_message = f"Invalid land. Choose between: {valid_land}"
        if v not in valid_land:
            raise ValueError(error_message)
        return v


land_properties = {
    "desert": {"albedo": 0.30, "loss": 0.10},
    "farm": {"albedo": 0.20, "loss": 0.15},
    "urban": {"albedo": 0.25, "loss": 0.20},
    "flooded_area": {"albedo": 0.10, "loss": 0.12},
}
