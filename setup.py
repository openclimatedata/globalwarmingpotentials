"""
globalwarmingpotentials
-------------

Install using ::

    pip install globalwarmingpotentials

See README.md and repository for details:
    https://github.com/openclimatedate/globalwarmingpotentials
"""

from setuptools import find_packages, setup
import os

import versioneer

path = os.path.abspath(os.path.dirname(__file__))

description = "Global warming potentials of greenhouse gases from various IPCC reports"

with open(os.path.join(path, "./README.md"), "r") as f:
    readme = f.read()

cmdclass = versioneer.get_cmdclass()

SOURCE_DIR = "src"
PACKAGES = find_packages(SOURCE_DIR)
PACKAGE_DIR = {"": SOURCE_DIR}
PACKAGE_DATA = {"globalwarmingpotentials": ["globalwarmingpotentials.csv"]}

setup(
    name="globalwarmingpotentials",
    version=versioneer.get_version(),
    description=description,
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/openclimatedata/globalwarmingpotentials",
    author="Robert Gieseke",
    author_email="rob.g@web.de",
    license="CC0",
    platforms="any",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=[
        "climate research",
        "greenhouse gases",
        "global warming potentials",
        "climate change",
    ],
    cmdclass=cmdclass,
    packages=PACKAGES,
    package_dir=PACKAGE_DIR,
    package_data=PACKAGE_DATA,
)
