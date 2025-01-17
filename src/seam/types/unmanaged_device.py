# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .unmanaged_device_capabilities_supported_item import UnmanagedDeviceCapabilitiesSupportedItem
from .unmanaged_device_device_type import UnmanagedDeviceDeviceType
from .unmanaged_device_errors_item import UnmanagedDeviceErrorsItem
from .unmanaged_device_properties import UnmanagedDeviceProperties
from .unmanaged_device_warnings_item import UnmanagedDeviceWarningsItem


class UnmanagedDevice(pydantic.BaseModel):
    device_id: str
    device_type: UnmanagedDeviceDeviceType
    connected_account_id: str
    capabilities_supported: typing.List[UnmanagedDeviceCapabilitiesSupportedItem]
    workspace_id: str
    errors: typing.List[UnmanagedDeviceErrorsItem]
    warnings: typing.List[UnmanagedDeviceWarningsItem]
    created_at: str
    is_managed: str
    properties: UnmanagedDeviceProperties

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
