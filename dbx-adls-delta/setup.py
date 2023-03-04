from setuptools import find_packages, setup
from dbx_adls_delta import __version__

setup(
    name="dbx_adls_delta",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="",
    author=""
)
