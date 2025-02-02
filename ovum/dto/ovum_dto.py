from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class OvumAddressDTO:
    address: int
    value: int
    min: int
    max: int
    default: int
