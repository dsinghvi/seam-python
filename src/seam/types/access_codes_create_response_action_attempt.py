# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .access_codes_create_response_action_attempt_error import AccessCodesCreateResponseActionAttemptError
from .access_codes_create_response_action_attempt_pending import AccessCodesCreateResponseActionAttemptPending
from .access_codes_create_response_action_attempt_success import AccessCodesCreateResponseActionAttemptSuccess


class AccessCodesCreateResponseActionAttempt_Success(AccessCodesCreateResponseActionAttemptSuccess):
    status: typing_extensions.Literal["success"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class AccessCodesCreateResponseActionAttempt_Pending(AccessCodesCreateResponseActionAttemptPending):
    status: typing_extensions.Literal["pending"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class AccessCodesCreateResponseActionAttempt_Error(AccessCodesCreateResponseActionAttemptError):
    status: typing_extensions.Literal["error"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


AccessCodesCreateResponseActionAttempt = typing_extensions.Annotated[
    typing.Union[
        AccessCodesCreateResponseActionAttempt_Success,
        AccessCodesCreateResponseActionAttempt_Pending,
        AccessCodesCreateResponseActionAttempt_Error,
    ],
    pydantic.Field(discriminator="status"),
]
