"""
Generate Python and JavaScript modules with GWP by species as
listed in Data Package CSV file.
"""

import json
import numpy as np
import pandas as pd

from pathlib import Path
from yapf.yapflib.yapf_api import FormatCode

root = Path(__file__).parents[1]

df = pd.read_csv(root / "globalwarmingpotentials.csv", comment="#", index_col="Species")

py_out = '''"""
globalwarmingpotentials
-----------------------

"""

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions


def as_frame():
    """Return Global Warming Potentials as a Pandas DataFrame."""
    try:
        import pandas as pd
    except ImportError:
        raise ImportError(
            "pandas is required for reading global warming "
            "potentials as a Data Frame."
        ) from None

    import importlib.resources as pkg_resources

    return pd.read_csv(
        pkg_resources.open_text(
            "globalwarmingpotentials", "globalwarmingpotentials.csv"
        ),
        index_col=0,
        comment="#",
    )


data = {
'''

for column in df.columns:
    py_out += f"'{column}': {df[column].dropna().to_dict()},\n\n"

py_out += "}\n"

with open(str(root / "src/globalwarmingpotentials/__init__.py"), "w") as f:
    f.write(FormatCode(py_out)[0])

js_out = """// Global Warming potentials

"""

for column in df.columns:
    js_out += f"export const {column} = {df[column].to_json(indent=2)}\n\n"


with open(str(root / "index.js"), "w") as f:
    f.write(js_out)
