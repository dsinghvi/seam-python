# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .access_codes_delete_response_action_attempt_error import AccessCodesDeleteResponseActionAttemptError
from .access_codes_delete_response_action_attempt_pending import AccessCodesDeleteResponseActionAttemptPending
from .access_codes_delete_response_action_attempt_success import AccessCodesDeleteResponseActionAttemptSuccess


class AccessCodesDeleteResponseActionAttempt_Success(AccessCodesDeleteResponseActionAttemptSuccess):
    status: typing_extensions.Literal["success"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class AccessCodesDeleteResponseActionAttempt_Pending(AccessCodesDeleteResponseActionAttemptPending):
    status: typing_extensions.Literal["pending"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


class AccessCodesDeleteResponseActionAttempt_Error(AccessCodesDeleteResponseActionAttemptError):
    status: typing_extensions.Literal["error"]

    class Config:
        frozen = True
        allow_population_by_field_name = True


AccessCodesDeleteResponseActionAttempt = typing_extensions.Annotated[
    typing.Union[
        AccessCodesDeleteResponseActionAttempt_Success,
        AccessCodesDeleteResponseActionAttempt_Pending,
        AccessCodesDeleteResponseActionAttempt_Error,
    ],
    pydantic.Field(discriminator="status"),
]
