from .pv_inverter import PvInverter
from .pv_module import PvModule
import math


class PvSystem:
    """
    This class models the configuration and calculation of a photovoltaic system,
    including the arrangement of solar modules, inverters, and the target power.

    Args:
        pv_module (PvModule): The photovoltaic module used in the system.
        pv_inverter (PvInverter): The inverter used in the system.
        target_power (float): The target power output for the system.
        max_temperature (float): The maximum operating temperature of the system.
        min_temperature (float): The minimum operating temperature of the system.
    """

    class Layout:
        """
        This class is used to define the physical arrangement of solar modules
        in a row within the photovoltaic system.

        Args:
            line_quantity (int): The quantity of rows of solar modules in the layout.
            modules_per_line (int): The quantity of solar modules per row in the layout.
        """

        def __init__(self, line_quantity: int, modules_per_line: int):
            self.line_quantity = line_quantity
            self.modules_per_line = modules_per_line

        def __repr__(self):
            return f"Layout(line_quantity={self.line_quantity}, modules_per_line={self.modules_per_line})"

    class Response:
        """
        This class encapsulates the results of a calculation for a photovoltaic system,
        including information about the number of inverters, the rate of system efficiency (ROS),
        and the layouts of solar modules.

        Args:
            inverter_quantity (int): The number of inverters in the photovoltaic system.
            ROS (float): The rate of system efficiency.
            layouts (list): A list of Layout objects representing the physical configurations.
        """

        def __init__(
            self,
            inverter_quantity: int,
            ROS: float,
            layouts: list["PvSystem.Layout"],
        ):
            self.inverter_quantity = inverter_quantity
            self.ROS = ROS
            self.layouts = layouts

        def __repr__(self):
            return f"PvSystem(inverter_quantity={self.inverter_quantity}, ROS={self.ROS}, layouts={self.layouts})"

    def __init__(
        self,
        pv_module: PvModule,
        pv_inverter: PvInverter,
        target_power: float,
        max_temperature: float,
        min_temperature: float,
    ):
        self.pv_module = pv_module
        self.pv_inverter = pv_inverter
        self.target_power = target_power
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature

    def __merge_layouts(self, layout: Layout, layouts: list[Layout]):
        """
        This method is used to merge a new layout with existing layouts if they have the same
        number of modules per line. If a match is found, the line quantity is added to the existing layout.

        Args:
            layout (Layout): The layout to be merged.
            layouts (list): The list of layouts to merge with.
        """
        for index, single_layout in enumerate(layouts):
            if single_layout.modules_per_line == layout.modules_per_line:
                layouts[index].line_quantity += layout.line_quantity
                return
        layouts.append(layout)

    def calculate(self):
        """
        This method calculates the configuration of the photovoltaic system, including the
        number of inverters, the rate of system efficiency (ROS), and the layouts of solar modules.

        Returns:
            Response: An instance of the Response class containing the calculation results.
        """
        pv_module_power = self.pv_module.p_max * 0.001
        pv_module_max_vmp_adj = self.pv_module.max_vmp_adjusted(self.max_temperature)
        pv_module_min_vmp_adj = self.pv_module.min_vmp_adjusted(self.min_temperature)
        pv_module_voc_adj = self.pv_module.voc_adjusted(self.min_temperature)
        pv_module_isc_adj = self.pv_module.isc_adjusted(self.max_temperature)
        max_modules_per_inverter = self.pv_inverter.max_pv_power / pv_module_power
        pv_system_qtd = math.ceil(
            self.target_power / (max_modules_per_inverter * pv_module_power)
        )
        remaining_module_qtd = self.target_power / pv_module_power
        MPPTs_qtd = len(self.pv_inverter.MPPTs)
        ROS = (self.pv_inverter.nominal_power * pv_system_qtd) / self.target_power
        layouts: list[self.Layout] = []
        for i in range(pv_system_qtd):
            remaining_pv_system_qtd = pv_system_qtd - i
            pv_system_target_module_qtd = round(
                remaining_module_qtd / remaining_pv_system_qtd
            )
            for MPPT_idx, MPPT in enumerate(self.pv_inverter.MPPTs):
                min_modules_per_string = self.pv_inverter.min_modules_per_string(
                    mpp_min_voltage=MPPT.min_voltage,
                    max_vmp_adjusted=pv_module_max_vmp_adj,
                )
                max_modules_per_string = self.pv_inverter.max_modules_per_string(
                    mpp_max_voltage=MPPT.max_voltage,
                    min_vmp_adjusted=pv_module_min_vmp_adj,
                    voc_adjusted=pv_module_voc_adj,
                )
                max_string_qtd = self.pv_inverter.available_strings_per_MPPT(
                    mpp_max_isc=MPPT.isc, isc_adjusted=pv_module_isc_adj
                )
                target_mppt_module_qtd = pv_system_target_module_qtd / (
                    MPPTs_qtd - MPPT_idx
                )
                for string_qtd in range(1, max_string_qtd + 1):
                    module_per_string = round(target_mppt_module_qtd / string_qtd)
                    is_above_limit = module_per_string >= min_modules_per_string
                    is_under_limit = module_per_string <= max_modules_per_string
                    if not is_above_limit and is_under_limit:
                        continue
                    layout = self.Layout(
                        line_quantity=string_qtd,
                        modules_per_line=module_per_string,
                    )
                    self.__merge_layouts(layout, layouts)
                    pv_system_target_module_qtd -= module_per_string
                    remaining_module_qtd -= module_per_string
        return self.Response(
            inverter_quantity=pv_system_qtd,
            ROS=ROS,
            layouts=layouts,
        )
