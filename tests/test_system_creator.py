from ..services.system_creator import system_creator
from ..models.pv_inverter import PvInverter
from ..models.pv_module import PvModule


def test_system_creator():
    pv_inverter = PvInverter(
        start_voltage=200,
        nominal_voltage=360,
        max_voltage=850,
        nominal_power=15,
        mpp_min_voltage=160,
        mpp_max_voltage=800,
        max_isc=40,
        mppt_qtd=2,
    )
    pv_module = PvModule(
        p_max=545,
        vmp=41.93,
        imp=13,
        voc=49.9,
        isc=13.92,
        efficiency=21.3,
        p_max_coefficient=-0.35,
        voc_coefficient=-0.285,
        isc_coefficient=0.045,
    )
    system_creator(
        pv_module=pv_module,
        pv_inverter=pv_inverter,
        min_temperature=0,
        max_temperature=70,
    )
