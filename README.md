<div align="center">
    <a href="https://github.com/patrickpasquini/PyPv" target="_blank">
      <img src="./docs/assets/logo.png" alt="PyPv Logo">
    </a>
</div>

<div align="center">
    <a href="https://pypi.org/project/pypv/" target="_blank">
      <img src="https://img.shields.io/pypi/v/pypv" alt="PyPv Version">
    </a>
    <a href="https://pypi.org/project/pypv/" target="_blank">
      <img src="https://img.shields.io/badge/Python-3.11-blue" alt="Python Version">
    </a>
    <!-- <a href="LINK_TO_YOUR_COVERAGE_REPORT" target="_blank">
      <img src="https://img.shields.io/endpoint?url=URL_TO_YOUR_COVERAGE_BADGE_JSON&logo=pytest" alt="Coverage">
    </a> -->
    <a href="https://pepy.tech/project/pypv" target="_blank">
      <img src="https://static.pepy.tech/badge/pypv" alt="Downloads">
    </a>
</div>

---

**Documentation**: Building...

**Source Code**: <a href="https://github.com/patrickpasquini/PyPv" target="_blank">https://github.com/patrickpasquini/PyPv</a>

---

## Installation

You can install `pypv` using pip:
```bash
pip install pypv
```

## What is it?

**pypv** is a state-of-the-art Python library designed to empower engineers and developers in the field of solar energy. This library simplifies the use of complex physical models, making it easier to calculate key solar parameters and optimize solar energy systems. 

## Key Features

Here's a simple example of how to use the `calculate_pv_system` method:

```python
from pypv import PvSystem

# Config module and inverter
pv_module = PvModule(
    p_max=545,
    vmp=41.8,
    imp=13.09,
    voc=49.65,
    isc=13.92,
    efficiency=21.1,
    p_max_coefficient=-0.35,
    voc_coefficient=-0.27,
    isc_coefficient=0.048,
)

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

# Creating an instance of PvSystem
pv_system = PvSystem(pv_module=pv_module, pv_inverter=pv_inverter, target_power=6, max_temperature=75, min_temperature=0)
pv_system.calculate()

# Displaying the results
PvSystem(inverter_quantity=2, ROS=0.8333333333333334, layouts=[Layout(line_quantity=2, modules_per_line=6), Layout(line_quantity=2, modules_per_line=5)])
```


## Contributing

We warmly welcome contributions to **pypv** Whether you're fixing a bug, adding a feature, or improving documentation, your help is invaluable.