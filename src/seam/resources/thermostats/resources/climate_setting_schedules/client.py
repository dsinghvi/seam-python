# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic
import typing_extensions

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....environment import SeamEnvironment
from .....errors.bad_request_error import BadRequestError
from .....errors.unauthorized_error import UnauthorizedError
from .....types.thermostats_climate_setting_schedules_create_request_hvac_mode_setting import (
    ThermostatsClimateSettingSchedulesCreateRequestHvacModeSetting,
)
from .....types.thermostats_climate_setting_schedules_create_response import (
    ThermostatsClimateSettingSchedulesCreateResponse,
)
from .....types.thermostats_climate_setting_schedules_delete_response import (
    ThermostatsClimateSettingSchedulesDeleteResponse,
)
from .....types.thermostats_climate_setting_schedules_get_response import ThermostatsClimateSettingSchedulesGetResponse
from .....types.thermostats_climate_setting_schedules_list_response import (
    ThermostatsClimateSettingSchedulesListResponse,
)
from .....types.thermostats_climate_setting_schedules_update_request_hvac_mode_setting import (
    ThermostatsClimateSettingSchedulesUpdateRequestHvacModeSetting,
)
from .....types.thermostats_climate_setting_schedules_update_response import (
    ThermostatsClimateSettingSchedulesUpdateResponse,
)

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ClimateSettingSchedulesClient:
    def __init__(self, *, environment: SeamEnvironment = SeamEnvironment.DEFAULT, client_wrapper: SyncClientWrapper):
        self._environment = environment
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        schedule_type: typing.Optional[typing_extensions.Literal["time_bound"]] = OMIT,
        device_id: str,
        name: typing.Optional[str] = OMIT,
        schedule_starts_at: str,
        schedule_ends_at: str,
        automatic_heating_enabled: typing.Optional[bool] = OMIT,
        automatic_cooling_enabled: typing.Optional[bool] = OMIT,
        hvac_mode_setting: typing.Optional[ThermostatsClimateSettingSchedulesCreateRequestHvacModeSetting] = OMIT,
        cooling_set_point_celsius: typing.Optional[float] = OMIT,
        heating_set_point_celsius: typing.Optional[float] = OMIT,
        cooling_set_point_fahrenheit: typing.Optional[float] = OMIT,
        heating_set_point_fahrenheit: typing.Optional[float] = OMIT,
        manual_override_allowed: typing.Optional[bool] = OMIT,
    ) -> ThermostatsClimateSettingSchedulesCreateResponse:
        """
        Parameters:
            - schedule_type: typing.Optional[typing_extensions.Literal["time_bound"]].

            - device_id: str.

            - name: typing.Optional[str].

            - schedule_starts_at: str.

            - schedule_ends_at: str.

            - automatic_heating_enabled: typing.Optional[bool].

            - automatic_cooling_enabled: typing.Optional[bool].

            - hvac_mode_setting: typing.Optional[ThermostatsClimateSettingSchedulesCreateRequestHvacModeSetting].

            - cooling_set_point_celsius: typing.Optional[float].

            - heating_set_point_celsius: typing.Optional[float].

            - cooling_set_point_fahrenheit: typing.Optional[float].

            - heating_set_point_fahrenheit: typing.Optional[float].

            - manual_override_allowed: typing.Optional[bool].
        """
        _request: typing.Dict[str, typing.Any] = {
            "device_id": device_id,
            "schedule_starts_at": schedule_starts_at,
            "schedule_ends_at": schedule_ends_at,
        }
        if schedule_type is not OMIT:
            _request["schedule_type"] = schedule_type
        if name is not OMIT:
            _request["name"] = name
        if automatic_heating_enabled is not OMIT:
            _request["automatic_heating_enabled"] = automatic_heating_enabled
        if automatic_cooling_enabled is not OMIT:
            _request["automatic_cooling_enabled"] = automatic_cooling_enabled
        if hvac_mode_setting is not OMIT:
            _request["hvac_mode_setting"] = hvac_mode_setting
        if cooling_set_point_celsius is not OMIT:
            _request["cooling_set_point_celsius"] = cooling_set_point_celsius
        if heating_set_point_celsius is not OMIT:
            _request["heating_set_point_celsius"] = heating_set_point_celsius
        if cooling_set_point_fahrenheit is not OMIT:
            _request["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if heating_set_point_fahrenheit is not OMIT:
            _request["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit
        if manual_override_allowed is not OMIT:
            _request["manual_override_allowed"] = manual_override_allowed
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "thermostats/climate_setting_schedules/create"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ThermostatsClimateSettingSchedulesCreateResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, *, climate_setting_schedule_id: str) -> ThermostatsClimateSettingSchedulesDeleteResponse:
        """
        Parameters:
            - climate_setting_schedule_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "thermostats/climate_setting_schedules/delete"),
            json=jsonable_encoder({"climate_setting_schedule_id": climate_setting_schedule_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ThermostatsClimateSettingSchedulesDeleteResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self, *, climate_setting_schedule_id: typing.Optional[str] = OMIT, device_id: typing.Optional[str] = OMIT
    ) -> ThermostatsClimateSettingSchedulesGetResponse:
        """
        Parameters:
            - climate_setting_schedule_id: typing.Optional[str].

            - device_id: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if climate_setting_schedule_id is not OMIT:
            _request["climate_setting_schedule_id"] = climate_setting_schedule_id
        if device_id is not OMIT:
            _request["device_id"] = device_id
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "thermostats/climate_setting_schedules/get"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ThermostatsClimateSettingSchedulesGetResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(self, *, device_id: str) -> ThermostatsClimateSettingSchedulesListResponse:
        """
        Parameters:
            - device_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "thermostats/climate_setting_schedules/list"),
            json=jsonable_encoder({"device_id": device_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ThermostatsClimateSettingSchedulesListResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        *,
        climate_setting_schedule_id: str,
        schedule_type: typing.Optional[typing_extensions.Literal["time_bound"]] = OMIT,
        name: typing.Optional[str] = OMIT,
        schedule_starts_at: typing.Optional[str] = OMIT,
        schedule_ends_at: typing.Optional[str] = OMIT,
        automatic_heating_enabled: typing.Optional[bool] = OMIT,
        automatic_cooling_enabled: typing.Optional[bool] = OMIT,
        hvac_mode_setting: typing.Optional[ThermostatsClimateSettingSchedulesUpdateRequestHvacModeSetting] = OMIT,
        cooling_set_point_celsius: typing.Optional[float] = OMIT,
        heating_set_point_celsius: typing.Optional[float] = OMIT,
        cooling_set_point_fahrenheit: typing.Optional[float] = OMIT,
        heating_set_point_fahrenheit: typing.Optional[float] = OMIT,
        manual_override_allowed: typing.Optional[bool] = OMIT,
    ) -> ThermostatsClimateSettingSchedulesUpdateResponse:
        """
        Parameters:
            - climate_setting_schedule_id: str.

            - schedule_type: typing.Optional[typing_extensions.Literal["time_bound"]].

            - name: typing.Optional[str].

            - schedule_starts_at: typing.Optional[str].

            - schedule_ends_at: typing.Optional[str].

            - automatic_heating_enabled: typing.Optional[bool].

            - automatic_cooling_enabled: typing.Optional[bool].

            - hvac_mode_setting: typing.Optional[ThermostatsClimateSettingSchedulesUpdateRequestHvacModeSetting].

            - cooling_set_point_celsius: typing.Optional[float].

            - heating_set_point_celsius: typing.Optional[float].

            - cooling_set_point_fahrenheit: typing.Optional[float].

            - heating_set_point_fahrenheit: typing.Optional[float].

            - manual_override_allowed: typing.Optional[bool].
        """
        _request: typing.Dict[str, typing.Any] = {"climate_setting_schedule_id": climate_setting_schedule_id}
        if schedule_type is not OMIT:
            _request["schedule_type"] = schedule_type
        if name is not OMIT:
            _request["name"] = name
        if schedule_starts_at is not OMIT:
            _request["schedule_starts_at"] = schedule_starts_at
        if schedule_ends_at is not OMIT:
            _request["schedule_ends_at"] = schedule_ends_at
        if automatic_heating_enabled is not OMIT:
            _request["automatic_heating_enabled"] = automatic_heating_enabled
        if automatic_cooling_enabled is not OMIT:
            _request["automatic_cooling_enabled"] = automatic_cooling_enabled
        if hvac_mode_setting is not OMIT:
            _request["hvac_mode_setting"] = hvac_mode_setting
        if cooling_set_point_celsius is not OMIT:
            _request["cooling_set_point_celsius"] = cooling_set_point_celsius
        if heating_set_point_celsius is not OMIT:
            _request["heating_set_point_celsius"] = heating_set_point_celsius
        if cooling_set_point_fahrenheit is not OMIT:
            _request["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if heating_set_point_fahrenheit is not OMIT:
            _request["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit
        if manual_override_allowed is not OMIT:
            _request["manual_override_allowed"] = manual_override_allowed
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "thermostats/climate_setting_schedules/update"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ThermostatsClimateSettingSchedulesUpdateResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncClimateSettingSchedulesClient:
    def __init__(self, *, environment: SeamEnvironment = SeamEnvironment.DEFAULT, client_wrapper: AsyncClientWrapper):
        self._environment = environment
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        schedule_type: typing.Optional[typing_extensions.Literal["time_bound"]] = OMIT,
        device_id: str,
        name: typing.Optional[str] = OMIT,
        schedule_starts_at: str,
        schedule_ends_at: str,
        automatic_heating_enabled: typing.Optional[bool] = OMIT,
        automatic_cooling_enabled: typing.Optional[bool] = OMIT,
        hvac_mode_setting: typing.Optional[ThermostatsClimateSettingSchedulesCreateRequestHvacModeSetting] = OMIT,
        cooling_set_point_celsius: typing.Optional[float] = OMIT,
        heating_set_point_celsius: typing.Optional[float] = OMIT,
        cooling_set_point_fahrenheit: typing.Optional[float] = OMIT,
        heating_set_point_fahrenheit: typing.Optional[float] = OMIT,
        manual_override_allowed: typing.Optional[bool] = OMIT,
    ) -> ThermostatsClimateSettingSchedulesCreateResponse:
        """
        Parameters:
            - schedule_type: typing.Optional[typing_extensions.Literal["time_bound"]].

            - device_id: str.

            - name: typing.Optional[str].

            - schedule_starts_at: str.

            - schedule_ends_at: str.

            - automatic_heating_enabled: typing.Optional[bool].

            - automatic_cooling_enabled: typing.Optional[bool].

            - hvac_mode_setting: typing.Optional[ThermostatsClimateSettingSchedulesCreateRequestHvacModeSetting].

            - cooling_set_point_celsius: typing.Optional[float].

            - heating_set_point_celsius: typing.Optional[float].

            - cooling_set_point_fahrenheit: typing.Optional[float].

            - heating_set_point_fahrenheit: typing.Optional[float].

            - manual_override_allowed: typing.Optional[bool].
        """
        _request: typing.Dict[str, typing.Any] = {
            "device_id": device_id,
            "schedule_starts_at": schedule_starts_at,
            "schedule_ends_at": schedule_ends_at,
        }
        if schedule_type is not OMIT:
            _request["schedule_type"] = schedule_type
        if name is not OMIT:
            _request["name"] = name
        if automatic_heating_enabled is not OMIT:
            _request["automatic_heating_enabled"] = automatic_heating_enabled
        if automatic_cooling_enabled is not OMIT:
            _request["automatic_cooling_enabled"] = automatic_cooling_enabled
        if hvac_mode_setting is not OMIT:
            _request["hvac_mode_setting"] = hvac_mode_setting
        if cooling_set_point_celsius is not OMIT:
            _request["cooling_set_point_celsius"] = cooling_set_point_celsius
        if heating_set_point_celsius is not OMIT:
            _request["heating_set_point_celsius"] = heating_set_point_celsius
        if cooling_set_point_fahrenheit is not OMIT:
            _request["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if heating_set_point_fahrenheit is not OMIT:
            _request["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit
        if manual_override_allowed is not OMIT:
            _request["manual_override_allowed"] = manual_override_allowed
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "thermostats/climate_setting_schedules/create"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ThermostatsClimateSettingSchedulesCreateResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, *, climate_setting_schedule_id: str) -> ThermostatsClimateSettingSchedulesDeleteResponse:
        """
        Parameters:
            - climate_setting_schedule_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "thermostats/climate_setting_schedules/delete"),
            json=jsonable_encoder({"climate_setting_schedule_id": climate_setting_schedule_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ThermostatsClimateSettingSchedulesDeleteResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, *, climate_setting_schedule_id: typing.Optional[str] = OMIT, device_id: typing.Optional[str] = OMIT
    ) -> ThermostatsClimateSettingSchedulesGetResponse:
        """
        Parameters:
            - climate_setting_schedule_id: typing.Optional[str].

            - device_id: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if climate_setting_schedule_id is not OMIT:
            _request["climate_setting_schedule_id"] = climate_setting_schedule_id
        if device_id is not OMIT:
            _request["device_id"] = device_id
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "thermostats/climate_setting_schedules/get"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ThermostatsClimateSettingSchedulesGetResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(self, *, device_id: str) -> ThermostatsClimateSettingSchedulesListResponse:
        """
        Parameters:
            - device_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "thermostats/climate_setting_schedules/list"),
            json=jsonable_encoder({"device_id": device_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ThermostatsClimateSettingSchedulesListResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        *,
        climate_setting_schedule_id: str,
        schedule_type: typing.Optional[typing_extensions.Literal["time_bound"]] = OMIT,
        name: typing.Optional[str] = OMIT,
        schedule_starts_at: typing.Optional[str] = OMIT,
        schedule_ends_at: typing.Optional[str] = OMIT,
        automatic_heating_enabled: typing.Optional[bool] = OMIT,
        automatic_cooling_enabled: typing.Optional[bool] = OMIT,
        hvac_mode_setting: typing.Optional[ThermostatsClimateSettingSchedulesUpdateRequestHvacModeSetting] = OMIT,
        cooling_set_point_celsius: typing.Optional[float] = OMIT,
        heating_set_point_celsius: typing.Optional[float] = OMIT,
        cooling_set_point_fahrenheit: typing.Optional[float] = OMIT,
        heating_set_point_fahrenheit: typing.Optional[float] = OMIT,
        manual_override_allowed: typing.Optional[bool] = OMIT,
    ) -> ThermostatsClimateSettingSchedulesUpdateResponse:
        """
        Parameters:
            - climate_setting_schedule_id: str.

            - schedule_type: typing.Optional[typing_extensions.Literal["time_bound"]].

            - name: typing.Optional[str].

            - schedule_starts_at: typing.Optional[str].

            - schedule_ends_at: typing.Optional[str].

            - automatic_heating_enabled: typing.Optional[bool].

            - automatic_cooling_enabled: typing.Optional[bool].

            - hvac_mode_setting: typing.Optional[ThermostatsClimateSettingSchedulesUpdateRequestHvacModeSetting].

            - cooling_set_point_celsius: typing.Optional[float].

            - heating_set_point_celsius: typing.Optional[float].

            - cooling_set_point_fahrenheit: typing.Optional[float].

            - heating_set_point_fahrenheit: typing.Optional[float].

            - manual_override_allowed: typing.Optional[bool].
        """
        _request: typing.Dict[str, typing.Any] = {"climate_setting_schedule_id": climate_setting_schedule_id}
        if schedule_type is not OMIT:
            _request["schedule_type"] = schedule_type
        if name is not OMIT:
            _request["name"] = name
        if schedule_starts_at is not OMIT:
            _request["schedule_starts_at"] = schedule_starts_at
        if schedule_ends_at is not OMIT:
            _request["schedule_ends_at"] = schedule_ends_at
        if automatic_heating_enabled is not OMIT:
            _request["automatic_heating_enabled"] = automatic_heating_enabled
        if automatic_cooling_enabled is not OMIT:
            _request["automatic_cooling_enabled"] = automatic_cooling_enabled
        if hvac_mode_setting is not OMIT:
            _request["hvac_mode_setting"] = hvac_mode_setting
        if cooling_set_point_celsius is not OMIT:
            _request["cooling_set_point_celsius"] = cooling_set_point_celsius
        if heating_set_point_celsius is not OMIT:
            _request["heating_set_point_celsius"] = heating_set_point_celsius
        if cooling_set_point_fahrenheit is not OMIT:
            _request["cooling_set_point_fahrenheit"] = cooling_set_point_fahrenheit
        if heating_set_point_fahrenheit is not OMIT:
            _request["heating_set_point_fahrenheit"] = heating_set_point_fahrenheit
        if manual_override_allowed is not OMIT:
            _request["manual_override_allowed"] = manual_override_allowed
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "thermostats/climate_setting_schedules/update"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ThermostatsClimateSettingSchedulesUpdateResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
