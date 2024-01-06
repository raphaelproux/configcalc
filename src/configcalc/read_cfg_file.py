from decimal import Decimal
from numbers import Number
from pathlib import Path
import tomllib
from typing import Any, Callable


def read_config_file(path: Path, parse_float: Callable[[Number | str], float | Decimal]=float) -> dict[str, Any]:
    """use parse_float argument to select whether you want numbers to be recognized
    as float or Decimal (typically)"""
    content = tomllib.load(path.open('rb'), parse_float=parse_float)
    return content