from dataclasses import dataclass, field
from typing import Optional, List
from dataclasses_json import dataclass_json, config


@dataclass_json
@dataclass
class AlgorithmsDto:
    start: Optional[str] = field(default=None, metadata=config(field_name='from'))
    end: Optional[str] = field(default=None, metadata=config(field_name='to'))
    algorithm: Optional[str] = None


@dataclass_json
@dataclass
class LocationDto:
    id: str
    name: str
    longitude: float = field(metadata=config(field_name='lon'))
    latitude: float = field(metadata=config(field_name='lat'))
    algorithm: Optional[List[AlgorithmsDto]] = field(default_factory=list)


@dataclass_json
@dataclass
class SeasonDto:
    start: float = field(metadata=config(field_name='from'))
    end: Optional[float] = field(default=None, metadata=config(field_name='to'))


@dataclass_json
@dataclass
class PollenDataDto:
    start: float = field(metadata=config(field_name='from'))
    end: float = field(metadata=config(field_name='to'))
    value: float


@dataclass_json
@dataclass
class PollenMeasurementDto:
    polle: str
    location: str
    data: List[PollenDataDto] = field(default_factory=list)


@dataclass_json
@dataclass
class PollenDto:
    start: float = field(metadata=config(field_name='from'))
    end: float = field(metadata=config(field_name='to'))
    measurements: List[PollenMeasurementDto] = field(default_factory=list)
