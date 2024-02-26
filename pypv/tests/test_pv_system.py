from re import A
from ..pv_system import PvSystem
from ..pv_module import PvModule
from ..pv_inverter import MPPT, PvInverter
from pathlib import Path
import json

absolute_path = Path().absolute()


pv_modules_json_file = absolute_path / "json" / "pv_modules.json"
pv_inverters_json_file = absolute_path / "json" / "pv_inverters.json"


def test_pv_system():
    with open(pv_modules_json_file) as file:
        pv_modules = [PvModule(**pv_module) for pv_module in json.load(file)]
    with open(pv_inverters_json_file) as file:
        pv_inverters = [PvInverter(**pv_module) for pv_module in json.load(file)]
    MPPTs = [MPPT(**mppt) for mppt in pv_inverters[0].MPPTs]
    pv_inverters[0].MPPTs = MPPTs
    pv_system = PvSystem(
        pv_module=pv_modules[0],
        pv_inverter=pv_inverters[0],
        target_power=12,
        min_temperature=0,
        max_temperature=75,
    )
    pv_system = pv_system.calculate()
    assert pv_system.inverter_quantity == 2
    assert pv_system.ROS == 0.8333333333333334
    assert pv_system.layouts[0].line_quantity == 2
    assert pv_system.layouts[1].line_quantity == 2
    assert pv_system.layouts[0].modules_per_line == 6
    assert pv_system.layouts[1].modules_per_line == 5
