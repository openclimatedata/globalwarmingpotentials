"""
Generate Python and JavaScript modules with GWP by species as
listed in Data Package CSV file.
"""

import json
import numpy as np

from pathlib import Path
from pandas_datapackage_reader import read_datapackage
from yapf.yapflib.yapf_api import FormatCode

root = Path(__file__).parents[1]

df = read_datapackage(root / "datapackage.json", "globalwarmingpotentials")

py_out = '''"""
globalwarmingpotentials
-----------------------

"""

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

'''

for column in df.columns:
    py_out += f"{column} = {df[column].replace({np.nan: None}).to_dict()}\n\n"

with open(str(root / "src/globalwarmingpotentials/__init__.py"), "w") as f:
    f.write(FormatCode(py_out)[0])

js_out = """// Global Warming potentials

"""

for column in df.columns:
    js_out += f"exports.{column} = {df[column].to_json(indent=2)}\n\n"


with open(str(root / "index.js"), "w") as f:
    f.write(js_out)
