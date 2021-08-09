# Global Warming Potentials

This work is released under a **Creative Commons CC0 Public Domain Dedication**.
Read the [LICENSE](LICENSE).

[![PyPI](https://img.shields.io/pypi/v/globalwarmingpotentials.svg)](https://pypi.org/project/globalwarmingpotentials/)
[![npm](https://img.shields.io/npm/v/globalwarmingpotentials.svg)](https://www.npmjs.com/package/globalwarmingpotentials)

Global warming potentials of greenhouse gases.

## GWP metrics included in this repository

### 100-year-GWP from IPCC reports

- Second Assessment Report (SAR) - **SARGWP100**
  [Data source](https://www.ghgprotocol.org/sites/default/files/ghgp/Global-Warming-Potential-Values%20%28Feb%2016%202016%29_1.pdf)
- Fourth Assessment Report (AR4) - **AR4GWP100**
  [Data source](https://www.ghgprotocol.org/sites/default/files/ghgp/Global-Warming-Potential-Values%20%28Feb%2016%202016%29_1.pdf)
- Fifth Assessment Report (AR5) - **AR5GWP100**
  [Data source](https://www.ghgprotocol.org/sites/default/files/ghgp/Global-Warming-Potential-Values%20%28Feb%2016%202016%29_1.pdf)
- Sixth Assessment Report (AR6) - **AR6GWP100**
  [Data Source](https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_Chapter_07_Supplementary_Material.pdf)

### 100-year-GWP including climate carbon cycle feedbacks

- Fifth Assessment Report (AR5) - **AR5CCFGWP100**
  Data sources:
  - [Table 8.SM.16](https://www.ipcc.ch/site/assets/uploads/2018/07/WGI_AR5.Chap_.8_SM.pdf)
  - [Table 8.7](https://www.ipcc.ch/site/assets/uploads/2018/02/WG1AR5_Chapter08_FINAL.pdf)
    (page 714)

## CSV file

CSV file: [globalwarmingpotentials.csv](./globalwarmingpotentials.csv)

## Python

```
pip install globalwarmingpotentials
```

Example usage:

```python
import globalwarmingpotentials as gwp

print(gwp.data["AR5GWP100"]["CH4"])  # prints '28'

df = gwp.as_frame()  # Returns a Pandas DataFrame
```

## Node

```
npm install globalwarmingpotentials
```

## Releasing

Running
```
make tag
```

and pushing with
```
git push origin main --tags
```

will create new releases on PyPI and NPM.
