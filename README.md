# configcalc

[![PyPI - Version](https://img.shields.io/pypi/v/configcalc.svg)](https://pypi.org/project/configcalc)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/configcalc.svg)](https://pypi.org/project/configcalc)

-----

Configcalc is a library to handle TOML configuration files with formulas. Formulas can make simple operations between variables contained in other parts of the configuration or given by the user at runtime. 

[Documentation](https://raphaelproux.github.io/configcalc/)


**Table of Contents**

- [configcalc](#configcalc)
  - [Installation](#installation)
  - [Usage](#usage)
  - [License](#license)

## Installation

```console
pip install configcalc
```


## Usage

```python
import configcalc as cc
config1 = cc.read_config_file(Path(r"path/to/config_file1.toml"))
config2 = cc.read_config_file(Path(r"path/to/config_file2.toml"))
merged_config = cc.merge_configs(config1, config2)
calculated_config = cc.perform_calculations(
        config=config,
    )
```

## License

`configcalc` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
