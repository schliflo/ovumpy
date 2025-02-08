from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class OvumAddressDTO:
    address: int
    value: float
    min: float
    max: float
    default: float
    label: Optional[str] = None
    unit: Optional[str] = None
