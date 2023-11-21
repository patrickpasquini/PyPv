import math


class PvInverter:
    def __init__(
        self,
        start_voltage: float,
        nominal_voltage: float,
        max_voltage: float,
        nominal_power: float,
        mpp_min_voltage: float,
        mpp_max_voltage: float,
        mpp_max_isc: float,
        mppt_qtd: int,
        efficiency: float,
    ):
        """
        Initialize a Photovoltaic (PV) Inverter object with various parameters.

        Args:
            start_voltage (float): The voltage at which the inverter starts operating.
            nominal_voltage (float): The nominal operating voltage of the inverter.
            max_voltage (float): The maximum input voltage supported by the inverter.
            nominal_power (float): The nominal power rating of the inverter.
            mpp_min_voltage (float): Minimum voltage for Maximum Power Point Tracking (MPPT).
            mpp_max_voltage (float): Maximum voltage for MPPT.
            mpp_max_isc (float): Maximum short-circuit current for MPPT.
            mppt_qtd (int): Number of Maximum Power Point Trackers (MPPT) channels.
            efficiency (float): The efficiency of the inverter.
        """
        self.start_voltage = start_voltage
        self.nominal_voltage = nominal_voltage
        self.max_voltage = max_voltage
        self.nominal_power = nominal_power
        self.mpp_min_voltage = mpp_min_voltage
        self.mpp_max_voltage = mpp_max_voltage
        self.mpp_max_isc = mpp_max_isc
        self.mppt_qtd = mppt_qtd
        self.efficiency = efficiency

    def available_strings_per_mppt(self, isc_adjusted: float):
        """
        Calculate the number of available PV strings per Maximum Power Point Tracker (MPPT) channel.

        Args:
            isc_adjusted (float): Adjusted short-circuit current.

        Returns:
            int: Number of PV strings that can be connected to each MPPT channel.
        """
        return math.floor(self.mpp_max_isc / isc_adjusted)

    def ideal_modules_per_string(self, vmp: float):
        """
        Calculate the ideal number of PV modules per string.

        Args:
            vmp (float): Voltage at the maximum power point (Vmp) of PV modules.

        Returns:
            int: Ideal number of PV modules per string.
        """
        return math.floor(self.nominal_voltage / vmp)

    def min_modules_per_string(self, max_vmp_adjusted: float):
        """
        Calculate the minimum number of PV modules per string.

        Args:
            max_vmp_adjusted (float): Adjusted maximum Vmp for calculation.

        Returns:
            int: Minimum number of PV modules per string.
        """
        return math.ceil(self.mpp_min_voltage / max_vmp_adjusted)

    def max_modules_per_string(self, min_vmp_adjusted: float, voc_adjusted: float):
        """
        Calculate the maximum number of PV modules per string.

        Args:
            min_vmp_adjusted (float): Adjusted minimum Vmp for calculation.
            voc_adjusted (float): Adjusted open-circuit voltage (Voc) for calculation.

        Returns:
            int: Maximum number of PV modules per string.
        """
        module_qtd_by_vmp = math.floor(self.mpp_max_voltage / min_vmp_adjusted)
        module_qtd_by_voc = math.floor(self.max_voltage / voc_adjusted)
        if module_qtd_by_vmp > module_qtd_by_voc:
            return module_qtd_by_voc
        return module_qtd_by_vmp
