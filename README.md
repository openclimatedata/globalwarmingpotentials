# Global Warming Potentials
[![PyPI](https://img.shields.io/pypi/v/globalwarmingpotentials.svg)](https://pypi.org/project/globalwarmingpotentials/)
[![npm](https://img.shields.io/npm/v/globalwarmingpotentials.svg)](https://www.npmjs.com/package/globalwarmingpotentials)

Global warming potentials of greenhouse gases.

IPCC reports:

- Second assessment Report (SAR)
- Fourth Assessment Report (AR4)
- Fifth Assessment Report (AR5)

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

## Sources

https://www.ghgprotocol.org/sites/default/files/ghgp/Global-Warming-Potential-Values%20%28Feb%2016%202016%29_1.pdf

`AR5CCFGWP100` are AR5 100 year GWPs with climate carbon cycle feedbacks:
https://www.ipcc.ch/site/assets/uploads/2018/07/WGI_AR5.Chap_.8_SM.pdf, Table 8.SM.16 and https://www.ipcc.ch/site/assets/uploads/2018/02/WG1AR5_Chapter08_FINAL.pdf , Table 8.7 (page 714).

This project was based on the implementations in the [OpenSCM project](https://github.com/openscm/openscm-units/).
