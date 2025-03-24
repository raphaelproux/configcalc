# Configcalc

Configcalc is a library to handle TOML configuration files with formulas. Formulas can make simple operations between variables contained in other parts of the configuration or given by the user at runtime. 

# Usage

Configcalc uses a TOML file. For example:
```toml
title = "TOML Example"

[owner]

[owner.info]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00
nb_of_days_per_month = 30
nb_of_months = 3
nb_of_days = "=nb_of_months * nb_of_days_per_month"
calculated_value = "= nb_of_days^3 * database.nb_of_ports + 2 / database.data[1][0]^2 * 2.32e-3 * _input_parts - cos(2*nb_of_days)"
```

Some strings are actually a formula which begins with "=". This formula can refer to its context (here, for example, `nb_of_months`). The content of the TOML file can be read and the formulas calculated automatically.

```python
import configcalc as cc
config1 = cc.read_config_file(Path(r"path/to/config_file1.toml"))
config2 = cc.read_config_file(Path(r"path/to/config_file2.toml"))
merged_config = cc.merge_configs(config1, config2)
calculated_config = cc.perform_calculations(
        config=config,
    )
```

