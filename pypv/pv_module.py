class PvModule:
    def __init__(
        self,
        p_max: float,
        vmp: float,
        imp: float,
        voc: float,
        isc: float,
        efficiency: float,
        p_max_coefficient: float,
        voc_coefficient: float,
        isc_coefficient: float,
    ):
        """
        Initialize a Photovoltaic (PV) Module object.

        Args:
            p_max (float): Maximum power output of the PV module.
            vmp (float): Voltage at the maximum power point (Vmp) of the PV module.
            imp (float): Current at the maximum power point (Imp) of the PV module.
            voc (float): Open-circuit voltage (Voc) of the PV module.
            isc (float): Short-circuit current (Isc) of the PV module.
            efficiency (float): The efficiency of the PV module. [0-100%]
            p_max_coefficient (float): Coefficient for adjusting maximum power (Pmax) with temperature. [0-100%]
            voc_coefficient (float): Coefficient for adjusting Voc with temperature. [0-100%]
            isc_coefficient (float): Coefficient for adjusting Isc with temperature. [0-100%]
        """
        self.p_max = p_max
        self.vmp = vmp
        self.imp = imp
        self.voc = voc
        self.isc = isc
        self.efficiency = efficiency * 0.01
        self.p_max_coefficient = p_max_coefficient * 0.01
        self.voc_coefficient = voc_coefficient * 0.01
        self.isc_coefficient = isc_coefficient * 0.01

    stc_temperature = 25

    def voc_adjusted(self, min_temperature: float):
        """
        Calculate the adjusted Voc (open-circuit voltage) of the PV module based on temperature.

        Args:
            min_temperature (float): Minimum temperature for adjustment.

        Returns:
            float: Adjusted Voc.
        """
        alpha = self.voc * self.voc_coefficient
        return self.voc + (alpha * (min_temperature - self.stc_temperature))

    def min_vmp_adjusted(self, min_temperature: float):
        """
        Calculate the adjusted minimum Vmp (voltage at maximum power point) of the PV module based on temperature.

        Args:
            min_temperature (float): Minimum temperature for adjustment.

        Returns:
            float: Adjusted minimum Vmp.
        """
        alpha = self.vmp * self.p_max_coefficient
        return self.vmp + (alpha * (min_temperature - self.stc_temperature))

    def max_vmp_adjusted(self, max_temperature: float):
        """
        Calculate the adjusted maximum Vmp (voltage at maximum power point) of the PV module based on temperature.

        Args:
            max_temperature (float): Maximum temperature for adjustment.

        Returns:
            float: Adjusted maximum Vmp.
        """
        alpha = self.vmp * self.p_max_coefficient
        return self.vmp + (alpha * (max_temperature - self.stc_temperature))

    def isc_adjusted(self, max_temperature: float):
        """
        Calculate the adjusted Isc (short-circuit current) of the PV module based on temperature.

        Args:
            max_temperature (float): Maximum temperature for adjustment.

        Returns:
            float: Adjusted Isc.
        """
        alpha = self.isc * self.isc_coefficient
        return self.isc + (alpha * (max_temperature - self.stc_temperature))
