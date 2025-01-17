# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...environment import SeamEnvironment
from ...errors.bad_request_error import BadRequestError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.access_codes_create_multiple_request_behavior_when_code_cannot_be_shared import (
    AccessCodesCreateMultipleRequestBehaviorWhenCodeCannotBeShared,
)
from ...types.access_codes_create_multiple_response import AccessCodesCreateMultipleResponse
from ...types.access_codes_create_response import AccessCodesCreateResponse
from ...types.access_codes_delete_response import AccessCodesDeleteResponse
from ...types.access_codes_get_response import AccessCodesGetResponse
from ...types.access_codes_list_response import AccessCodesListResponse
from ...types.access_codes_pull_backup_access_code_response import AccessCodesPullBackupAccessCodeResponse
from ...types.access_codes_update_request_type import AccessCodesUpdateRequestType
from ...types.access_codes_update_response import AccessCodesUpdateResponse
from .resources.simulate.client import AsyncSimulateClient, SimulateClient
from .resources.unmanaged.client import AsyncUnmanagedClient, UnmanagedClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AccessCodesClient:
    def __init__(self, *, environment: SeamEnvironment = SeamEnvironment.DEFAULT, client_wrapper: SyncClientWrapper):
        self._environment = environment
        self._client_wrapper = client_wrapper
        self.simulate = SimulateClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.unmanaged = UnmanagedClient(environment=self._environment, client_wrapper=self._client_wrapper)

    def create(
        self,
        *,
        device_id: str,
        name: typing.Optional[str] = OMIT,
        starts_at: typing.Optional[str] = OMIT,
        ends_at: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        sync: typing.Optional[bool] = OMIT,
        attempt_for_offline_device: typing.Optional[bool] = OMIT,
        common_code_key: typing.Optional[str] = OMIT,
        prefer_native_scheduling: typing.Optional[bool] = OMIT,
        use_backup_access_code_pool: typing.Optional[bool] = OMIT,
    ) -> AccessCodesCreateResponse:
        """
        Parameters:
            - device_id: str.

            - name: typing.Optional[str].

            - starts_at: typing.Optional[str].

            - ends_at: typing.Optional[str].

            - code: typing.Optional[str]. <span style="white-space: nowrap">`<= 8 characters`</span>

            - sync: typing.Optional[bool].

            - attempt_for_offline_device: typing.Optional[bool].

            - common_code_key: typing.Optional[str].

            - prefer_native_scheduling: typing.Optional[bool].

            - use_backup_access_code_pool: typing.Optional[bool].
        """
        _request: typing.Dict[str, typing.Any] = {"device_id": device_id}
        if name is not OMIT:
            _request["name"] = name
        if starts_at is not OMIT:
            _request["starts_at"] = starts_at
        if ends_at is not OMIT:
            _request["ends_at"] = ends_at
        if code is not OMIT:
            _request["code"] = code
        if sync is not OMIT:
            _request["sync"] = sync
        if attempt_for_offline_device is not OMIT:
            _request["attempt_for_offline_device"] = attempt_for_offline_device
        if common_code_key is not OMIT:
            _request["common_code_key"] = common_code_key
        if prefer_native_scheduling is not OMIT:
            _request["prefer_native_scheduling"] = prefer_native_scheduling
        if use_backup_access_code_pool is not OMIT:
            _request["use_backup_access_code_pool"] = use_backup_access_code_pool
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "access_codes/create"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AccessCodesCreateResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_multiple(
        self,
        *,
        device_ids: typing.List[str],
        behavior_when_code_cannot_be_shared: typing.Optional[
            AccessCodesCreateMultipleRequestBehaviorWhenCodeCannotBeShared
        ] = OMIT,
        name: typing.Optional[str] = OMIT,
        starts_at: typing.Optional[str] = OMIT,
        ends_at: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        attempt_for_offline_device: typing.Optional[bool] = OMIT,
        prefer_native_scheduling: typing.Optional[bool] = OMIT,
        use_backup_access_code_pool: typing.Optional[bool] = OMIT,
    ) -> AccessCodesCreateMultipleResponse:
        """
        Parameters:
            - device_ids: typing.List[str].

            - behavior_when_code_cannot_be_shared: typing.Optional[AccessCodesCreateMultipleRequestBehaviorWhenCodeCannotBeShared].

            - name: typing.Optional[str].

            - starts_at: typing.Optional[str].

            - ends_at: typing.Optional[str].

            - code: typing.Optional[str]. <span style="white-space: nowrap">`<= 8 characters`</span>

            - attempt_for_offline_device: typing.Optional[bool].

            - prefer_native_scheduling: typing.Optional[bool].

            - use_backup_access_code_pool: typing.Optional[bool].
        """
        _request: typing.Dict[str, typing.Any] = {"device_ids": device_ids}
        if behavior_when_code_cannot_be_shared is not OMIT:
            _request["behavior_when_code_cannot_be_shared"] = behavior_when_code_cannot_be_shared
        if name is not OMIT:
            _request["name"] = name
        if starts_at is not OMIT:
            _request["starts_at"] = starts_at
        if ends_at is not OMIT:
            _request["ends_at"] = ends_at
        if code is not OMIT:
            _request["code"] = code
        if attempt_for_offline_device is not OMIT:
            _request["attempt_for_offline_device"] = attempt_for_offline_device
        if prefer_native_scheduling is not OMIT:
            _request["prefer_native_scheduling"] = prefer_native_scheduling
        if use_backup_access_code_pool is not OMIT:
            _request["use_backup_access_code_pool"] = use_backup_access_code_pool
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "access_codes/create_multiple"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AccessCodesCreateMultipleResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(
        self, *, device_id: typing.Optional[str] = OMIT, access_code_id: str, sync: typing.Optional[bool] = OMIT
    ) -> AccessCodesDeleteResponse:
        """
        Parameters:
            - device_id: typing.Optional[str].

            - access_code_id: str.

            - sync: typing.Optional[bool].
        """
        _request: typing.Dict[str, typing.Any] = {"access_code_id": access_code_id}
        if device_id is not OMIT:
            _request["device_id"] = device_id
        if sync is not OMIT:
            _request["sync"] = sync
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "access_codes/delete"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AccessCodesDeleteResponse, _response.json())  # type: ignore
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
        self,
        *,
        device_id: typing.Optional[str] = OMIT,
        access_code_id: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
    ) -> AccessCodesGetResponse:
        """
        Parameters:
            - device_id: typing.Optional[str].

            - access_code_id: typing.Optional[str].

            - code: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if device_id is not OMIT:
            _request["device_id"] = device_id
        if access_code_id is not OMIT:
            _request["access_code_id"] = access_code_id
        if code is not OMIT:
            _request["code"] = code
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "access_codes/get"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AccessCodesGetResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(
        self, *, device_id: str, access_code_ids: typing.Optional[typing.List[str]] = OMIT
    ) -> AccessCodesListResponse:
        """
        Parameters:
            - device_id: str.

            - access_code_ids: typing.Optional[typing.List[str]].
        """
        _request: typing.Dict[str, typing.Any] = {"device_id": device_id}
        if access_code_ids is not OMIT:
            _request["access_code_ids"] = access_code_ids
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "access_codes/list"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AccessCodesListResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def pull_backup_access_code(self, *, access_code_id: str) -> AccessCodesPullBackupAccessCodeResponse:
        """
        Parameters:
            - access_code_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "access_codes/pull_backup_access_code"),
            json=jsonable_encoder({"access_code_id": access_code_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AccessCodesPullBackupAccessCodeResponse, _response.json())  # type: ignore
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
        name: typing.Optional[str] = OMIT,
        starts_at: typing.Optional[str] = OMIT,
        ends_at: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        sync: typing.Optional[bool] = OMIT,
        attempt_for_offline_device: typing.Optional[bool] = OMIT,
        prefer_native_scheduling: typing.Optional[bool] = OMIT,
        use_backup_access_code_pool: typing.Optional[bool] = OMIT,
        access_code_id: str,
        device_id: typing.Optional[str] = OMIT,
        type: typing.Optional[AccessCodesUpdateRequestType] = OMIT,
    ) -> AccessCodesUpdateResponse:
        """
        Parameters:
            - name: typing.Optional[str].

            - starts_at: typing.Optional[str].

            - ends_at: typing.Optional[str].

            - code: typing.Optional[str]. <span style="white-space: nowrap">`<= 8 characters`</span>

            - sync: typing.Optional[bool].

            - attempt_for_offline_device: typing.Optional[bool].

            - prefer_native_scheduling: typing.Optional[bool].

            - use_backup_access_code_pool: typing.Optional[bool].

            - access_code_id: str.

            - device_id: typing.Optional[str].

            - type: typing.Optional[AccessCodesUpdateRequestType].
        """
        _request: typing.Dict[str, typing.Any] = {"access_code_id": access_code_id}
        if name is not OMIT:
            _request["name"] = name
        if starts_at is not OMIT:
            _request["starts_at"] = starts_at
        if ends_at is not OMIT:
            _request["ends_at"] = ends_at
        if code is not OMIT:
            _request["code"] = code
        if sync is not OMIT:
            _request["sync"] = sync
        if attempt_for_offline_device is not OMIT:
            _request["attempt_for_offline_device"] = attempt_for_offline_device
        if prefer_native_scheduling is not OMIT:
            _request["prefer_native_scheduling"] = prefer_native_scheduling
        if use_backup_access_code_pool is not OMIT:
            _request["use_backup_access_code_pool"] = use_backup_access_code_pool
        if device_id is not OMIT:
            _request["device_id"] = device_id
        if type is not OMIT:
            _request["type"] = type
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "access_codes/update"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AccessCodesUpdateResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAccessCodesClient:
    def __init__(self, *, environment: SeamEnvironment = SeamEnvironment.DEFAULT, client_wrapper: AsyncClientWrapper):
        self._environment = environment
        self._client_wrapper = client_wrapper
        self.simulate = AsyncSimulateClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.unmanaged = AsyncUnmanagedClient(environment=self._environment, client_wrapper=self._client_wrapper)

    async def create(
        self,
        *,
        device_id: str,
        name: typing.Optional[str] = OMIT,
        starts_at: typing.Optional[str] = OMIT,
        ends_at: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        sync: typing.Optional[bool] = OMIT,
        attempt_for_offline_device: typing.Optional[bool] = OMIT,
        common_code_key: typing.Optional[str] = OMIT,
        prefer_native_scheduling: typing.Optional[bool] = OMIT,
        use_backup_access_code_pool: typing.Optional[bool] = OMIT,
    ) -> AccessCodesCreateResponse:
        """
        Parameters:
            - device_id: str.

            - name: typing.Optional[str].

            - starts_at: typing.Optional[str].

            - ends_at: typing.Optional[str].

            - code: typing.Optional[str]. <span style="white-space: nowrap">`<= 8 characters`</span>

            - sync: typing.Optional[bool].

            - attempt_for_offline_device: typing.Optional[bool].

            - common_code_key: typing.Optional[str].

            - prefer_native_scheduling: typing.Optional[bool].

            - use_backup_access_code_pool: typing.Optional[bool].
        """
        _request: typing.Dict[str, typing.Any] = {"device_id": device_id}
        if name is not OMIT:
            _request["name"] = name
        if starts_at is not OMIT:
            _request["starts_at"] = starts_at
        if ends_at is not OMIT:
            _request["ends_at"] = ends_at
        if code is not OMIT:
            _request["code"] = code
        if sync is not OMIT:
            _request["sync"] = sync
        if attempt_for_offline_device is not OMIT:
            _request["attempt_for_offline_device"] = attempt_for_offline_device
        if common_code_key is not OMIT:
            _request["common_code_key"] = common_code_key
        if prefer_native_scheduling is not OMIT:
            _request["prefer_native_scheduling"] = prefer_native_scheduling
        if use_backup_access_code_pool is not OMIT:
            _request["use_backup_access_code_pool"] = use_backup_access_code_pool
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "access_codes/create"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AccessCodesCreateResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_multiple(
        self,
        *,
        device_ids: typing.List[str],
        behavior_when_code_cannot_be_shared: typing.Optional[
            AccessCodesCreateMultipleRequestBehaviorWhenCodeCannotBeShared
        ] = OMIT,
        name: typing.Optional[str] = OMIT,
        starts_at: typing.Optional[str] = OMIT,
        ends_at: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        attempt_for_offline_device: typing.Optional[bool] = OMIT,
        prefer_native_scheduling: typing.Optional[bool] = OMIT,
        use_backup_access_code_pool: typing.Optional[bool] = OMIT,
    ) -> AccessCodesCreateMultipleResponse:
        """
        Parameters:
            - device_ids: typing.List[str].

            - behavior_when_code_cannot_be_shared: typing.Optional[AccessCodesCreateMultipleRequestBehaviorWhenCodeCannotBeShared].

            - name: typing.Optional[str].

            - starts_at: typing.Optional[str].

            - ends_at: typing.Optional[str].

            - code: typing.Optional[str]. <span style="white-space: nowrap">`<= 8 characters`</span>

            - attempt_for_offline_device: typing.Optional[bool].

            - prefer_native_scheduling: typing.Optional[bool].

            - use_backup_access_code_pool: typing.Optional[bool].
        """
        _request: typing.Dict[str, typing.Any] = {"device_ids": device_ids}
        if behavior_when_code_cannot_be_shared is not OMIT:
            _request["behavior_when_code_cannot_be_shared"] = behavior_when_code_cannot_be_shared
        if name is not OMIT:
            _request["name"] = name
        if starts_at is not OMIT:
            _request["starts_at"] = starts_at
        if ends_at is not OMIT:
            _request["ends_at"] = ends_at
        if code is not OMIT:
            _request["code"] = code
        if attempt_for_offline_device is not OMIT:
            _request["attempt_for_offline_device"] = attempt_for_offline_device
        if prefer_native_scheduling is not OMIT:
            _request["prefer_native_scheduling"] = prefer_native_scheduling
        if use_backup_access_code_pool is not OMIT:
            _request["use_backup_access_code_pool"] = use_backup_access_code_pool
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "access_codes/create_multiple"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AccessCodesCreateMultipleResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self, *, device_id: typing.Optional[str] = OMIT, access_code_id: str, sync: typing.Optional[bool] = OMIT
    ) -> AccessCodesDeleteResponse:
        """
        Parameters:
            - device_id: typing.Optional[str].

            - access_code_id: str.

            - sync: typing.Optional[bool].
        """
        _request: typing.Dict[str, typing.Any] = {"access_code_id": access_code_id}
        if device_id is not OMIT:
            _request["device_id"] = device_id
        if sync is not OMIT:
            _request["sync"] = sync
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "access_codes/delete"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AccessCodesDeleteResponse, _response.json())  # type: ignore
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
        self,
        *,
        device_id: typing.Optional[str] = OMIT,
        access_code_id: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
    ) -> AccessCodesGetResponse:
        """
        Parameters:
            - device_id: typing.Optional[str].

            - access_code_id: typing.Optional[str].

            - code: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {}
        if device_id is not OMIT:
            _request["device_id"] = device_id
        if access_code_id is not OMIT:
            _request["access_code_id"] = access_code_id
        if code is not OMIT:
            _request["code"] = code
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "access_codes/get"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AccessCodesGetResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(
        self, *, device_id: str, access_code_ids: typing.Optional[typing.List[str]] = OMIT
    ) -> AccessCodesListResponse:
        """
        Parameters:
            - device_id: str.

            - access_code_ids: typing.Optional[typing.List[str]].
        """
        _request: typing.Dict[str, typing.Any] = {"device_id": device_id}
        if access_code_ids is not OMIT:
            _request["access_code_ids"] = access_code_ids
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "access_codes/list"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AccessCodesListResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def pull_backup_access_code(self, *, access_code_id: str) -> AccessCodesPullBackupAccessCodeResponse:
        """
        Parameters:
            - access_code_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "access_codes/pull_backup_access_code"),
            json=jsonable_encoder({"access_code_id": access_code_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AccessCodesPullBackupAccessCodeResponse, _response.json())  # type: ignore
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
        name: typing.Optional[str] = OMIT,
        starts_at: typing.Optional[str] = OMIT,
        ends_at: typing.Optional[str] = OMIT,
        code: typing.Optional[str] = OMIT,
        sync: typing.Optional[bool] = OMIT,
        attempt_for_offline_device: typing.Optional[bool] = OMIT,
        prefer_native_scheduling: typing.Optional[bool] = OMIT,
        use_backup_access_code_pool: typing.Optional[bool] = OMIT,
        access_code_id: str,
        device_id: typing.Optional[str] = OMIT,
        type: typing.Optional[AccessCodesUpdateRequestType] = OMIT,
    ) -> AccessCodesUpdateResponse:
        """
        Parameters:
            - name: typing.Optional[str].

            - starts_at: typing.Optional[str].

            - ends_at: typing.Optional[str].

            - code: typing.Optional[str]. <span style="white-space: nowrap">`<= 8 characters`</span>

            - sync: typing.Optional[bool].

            - attempt_for_offline_device: typing.Optional[bool].

            - prefer_native_scheduling: typing.Optional[bool].

            - use_backup_access_code_pool: typing.Optional[bool].

            - access_code_id: str.

            - device_id: typing.Optional[str].

            - type: typing.Optional[AccessCodesUpdateRequestType].
        """
        _request: typing.Dict[str, typing.Any] = {"access_code_id": access_code_id}
        if name is not OMIT:
            _request["name"] = name
        if starts_at is not OMIT:
            _request["starts_at"] = starts_at
        if ends_at is not OMIT:
            _request["ends_at"] = ends_at
        if code is not OMIT:
            _request["code"] = code
        if sync is not OMIT:
            _request["sync"] = sync
        if attempt_for_offline_device is not OMIT:
            _request["attempt_for_offline_device"] = attempt_for_offline_device
        if prefer_native_scheduling is not OMIT:
            _request["prefer_native_scheduling"] = prefer_native_scheduling
        if use_backup_access_code_pool is not OMIT:
            _request["use_backup_access_code_pool"] = use_backup_access_code_pool
        if device_id is not OMIT:
            _request["device_id"] = device_id
        if type is not OMIT:
            _request["type"] = type
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "access_codes/update"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AccessCodesUpdateResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
