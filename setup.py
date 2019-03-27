from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRES = [
    'georss_client>=0.8',
]

setup(
    name="georss_ingv_centro_nazionale_terremoti_client",
    version="0.1",
    author="Malte Franken",
    author_email="coding@subspace.de",
    description="A GeoRSS client library for the INGV Centro Nazionale Terremoti (Earthquakes) feed.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/exxamalte/python-georss-ingv-centro-nazionale-terremoti-client",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRES
)
