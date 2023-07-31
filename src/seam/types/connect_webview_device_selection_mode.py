# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConnectWebviewDeviceSelectionMode(str, enum.Enum):
    NONE = "none"
    SINGLE = "single"
    MULTIPLE = "multiple"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        single: typing.Callable[[], T_Result],
        multiple: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConnectWebviewDeviceSelectionMode.NONE:
            return none()
        if self is ConnectWebviewDeviceSelectionMode.SINGLE:
            return single()
        if self is ConnectWebviewDeviceSelectionMode.MULTIPLE:
            return multiple()