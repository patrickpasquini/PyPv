from setuptools import setup, find_packages

setup(
    name="pypv",
    version="0.1.1",
    author="Patrick Pasquini",
    author_email="contatopasquini@gmail.com",
    description="A concise tool for solar system design. It offers essential resources for sizing photovoltaic installations, fostering sustainable energy solutions. Ideal for engineers, hobbyists and developers",
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
