from setuptools import setup, find_packages

NAME = "georss_ingv_centro_nazionale_terremoti_client"
AUTHOR = "Malte Franken"
AUTHOR_EMAIL = "coding@subspace.de"
DESCRIPTION = "A GeoRSS client library for the INGV Centro Nazionale Terremoti (Earthquakes) feed."
URL = "https://github.com/exxamalte/python-georss-ingv-centro-nazionale-terremoti-client"

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRES = [
    'georss_client>=0.8',
]

setup(
    name=NAME,
    version="0.1",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRES
)
