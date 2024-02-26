from setuptools import setup, find_packages

setup(
    name="pypv",
    version="0.3.0",
    author="Patrick Pasquini",
    author_email="contatopasquini@gmail.com",
    description="pypv is a state-of-the-art Python library designed to empower engineers and developers in the field of solar energy. This library simplifies the use of complex physical models, making it easier to calculate key solar parameters and optimize solar energy systems. ",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/patrickpasquini/PyPv.git",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="photovoltaic, pv panel, pv inverter, mppt, pv-calculator",
    python_requires=">=3.11",
)
