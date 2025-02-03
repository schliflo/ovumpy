from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class OvumAddressDTO:
    address: int
    value: int
    min: int
    max: int
    default: int
    label: Optional[str] = None
