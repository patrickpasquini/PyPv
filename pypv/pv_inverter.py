import math


class MPPT:
    def __init__(
        self,
        min_voltage: float,
        max_voltage: float,
        isc: float,
        dc_inputs: int,
    ):
        """
        Initialize a MPPT (Maximum Power Point Tracking) object.

        Args:
            min_voltage (float): Min MPPT voltage
            max_voltage (float): Max MPPT voltage
            isc (float): Maximum MPPT short-circuit current
            dc_inputs (float): Number of entries/strings per MPTT
        """
        self.min_voltage = min_voltage
        self.max_voltage = max_voltage
        self.isc = isc
        self.dc_inputs = dc_inputs


class PvInverter:
    def __init__(
        self,
        max_pv_power: float,
        start_voltage: float,
        nominal_voltage: float,
        max_voltage: float,
        nominal_power: float,
        efficiency: float,
        MPPTs: list[MPPT],
    ):
        """
        Initialize a Photovoltaic (PV) Inverter object.

        Args:
            max_pv_power (float): The maximum pv inverter power
            start_voltage (float): The voltage at which the inverter starts operating.
            nominal_voltage (float): The nominal operating voltage of the inverter.
            max_voltage (float): The maximum input voltage supported by the inverter.
            nominal_power (float): The nominal power rating of the inverter.
            efficiency (float): The efficiency of the inverter. [0-100%]
            MPPTs (list): List of MPPTs objects
        """
        self.max_pv_power = max_pv_power
        self.start_voltage = start_voltage
        self.nominal_voltage = nominal_voltage
        self.max_voltage = max_voltage
        self.nominal_power = nominal_power
        self.efficiency = efficiency * 0.01
        self.MPPTs = MPPTs

    def available_strings_per_MPPT(self, mpp_max_isc: float, isc_adjusted: float):
        """
        Calculate the number of available PV strings per Maximum Power Point Tracker (MPPT) channel.

        Args:
            mpp_max_isc (float): Maximum MPPT short-circuit current
            isc_adjusted (float): Pv Module adjusted short-circuit current.

        Returns:
            int: Number of PV strings that can be connected to each MPPT channel.
        """
        return math.floor(mpp_max_isc / isc_adjusted)

    def ideal_modules_per_string(self, vmp: float):
        """
        Calculate the ideal number of PV modules per string.

        Args:
            vmp (float): Voltage at the maximum power point (Vmp) of PV modules.

        Returns:
            int: Ideal number of PV modules per string.
        """
        return math.floor(self.nominal_voltage / vmp)

    def min_modules_per_string(self, mpp_min_voltage: float, max_vmp_adjusted: float):
        """
        Calculate the minimum number of PV modules per string.

        Args:
            mpp_min_voltage (float): Min MPPT voltage
            max_vmp_adjusted (float): Pv Module adjusted maximum Vmp for calculation.

        Returns:
            int: Minimum number of PV modules per string.
        """
        return math.ceil(mpp_min_voltage / max_vmp_adjusted)

    def max_modules_per_string(
        self, mpp_max_voltage: float, min_vmp_adjusted: float, voc_adjusted: float
    ):
        """
        Calculate the maximum number of PV modules per string.

        Args:
            mpp_max_voltage (float): Max MPPT voltage
            min_vmp_adjusted (float): Pv Module adjusted minimum Vmp for calculation.
            voc_adjusted (float): Pv Module adjusted open-circuit voltage (Voc) for calculation.

        Returns:
            int: Maximum number of PV modules per string.
        """
        module_qtd_by_vmp = math.floor(mpp_max_voltage / min_vmp_adjusted)
        module_qtd_by_voc = math.floor(self.max_voltage / voc_adjusted)
        if module_qtd_by_vmp > module_qtd_by_voc:
            return module_qtd_by_voc
        return module_qtd_by_vmp


pv_inverter = PvInverter(
    start_voltage=90,
    max_voltage=600,
    nominal_voltage=360,
    nominal_power=5,
    efficiency=98,
    max_pv_power=6.5,
    MPPTs=[
        MPPT(min_voltage=90, max_voltage=560, isc=15, dc_inputs=1),
        MPPT(min_voltage=90, max_voltage=560, isc=15, dc_inputs=1),
    ],
)
