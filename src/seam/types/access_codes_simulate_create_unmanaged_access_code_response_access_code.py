# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .access_codes_simulate_create_unmanaged_access_code_response_access_code_ongoing import (
    AccessCodesSimulateCreateUnmanagedAccessCodeResponseAccessCodeOngoing,
)
from .access_codes_simulate_create_unmanaged_access_code_response_access_code_time_bound import (
    AccessCodesSimulateCreateUnmanagedAccessCodeResponseAccessCodeTimeBound,
)


class AccessCodesSimulateCreateUnmanagedAccessCodeResponseAccessCode_Ongoing(
    AccessCodesSimulateCreateUnmanagedAccessCodeResponseAccessCodeOngoing
):
    type: typing_extensions.Literal["ongoing"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class AccessCodesSimulateCreateUnmanagedAccessCodeResponseAccessCode_TimeBound(
    AccessCodesSimulateCreateUnmanagedAccessCodeResponseAccessCodeTimeBound
):
    type: typing_extensions.Literal["time_bound"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


AccessCodesSimulateCreateUnmanagedAccessCodeResponseAccessCode = typing.Union[
    AccessCodesSimulateCreateUnmanagedAccessCodeResponseAccessCode_Ongoing,
    AccessCodesSimulateCreateUnmanagedAccessCodeResponseAccessCode_TimeBound,
]
