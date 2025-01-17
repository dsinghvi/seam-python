# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions

from ..core.datetime_utils import serialize_datetime
from .climate_setting_schedule_hvac_mode_setting import ClimateSettingScheduleHvacModeSetting


class ClimateSettingSchedule(pydantic.BaseModel):
    climate_setting_schedule_id: str
    schedule_type: typing_extensions.Literal["time_bound"]
    device_id: str
    name: typing.Optional[str]
    schedule_starts_at: str
    schedule_ends_at: str
    created_at: str
    automatic_heating_enabled: typing.Optional[bool]
    automatic_cooling_enabled: typing.Optional[bool]
    hvac_mode_setting: typing.Optional[ClimateSettingScheduleHvacModeSetting]
    cooling_set_point_celsius: typing.Optional[float]
    heating_set_point_celsius: typing.Optional[float]
    cooling_set_point_fahrenheit: typing.Optional[float]
    heating_set_point_fahrenheit: typing.Optional[float]
    manual_override_allowed: typing.Optional[bool]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
