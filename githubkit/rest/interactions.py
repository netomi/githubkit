"""DO NOT EDIT THIS FILE!

This file is auto generated by github rest api description.
See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, Union, Literal, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import UNSET, Unset, exclude_unset

from .types import InteractionLimitType
from .models import (
    ValidationError,
    InteractionLimit,
    InteractionLimitResponse,
    UserInteractionLimitsGetResponse200Anyof1,
    OrgsOrgInteractionLimitsGetResponse200Anyof1,
    ReposOwnerRepoInteractionLimitsGetResponse200Anyof1,
)

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response


class InteractionsClient:
    def __init__(self, github: "GitHubCore"):
        self._github = github

    def get_restrictions_for_org(
        self,
        org: str,
    ) -> "Response[Union[InteractionLimitResponse, OrgsOrgInteractionLimitsGetResponse200Anyof1]]":
        url = f"/orgs/{org}/interaction-limits"

        return self._github.request(
            "GET",
            url,
            response_model=Union[
                InteractionLimitResponse, OrgsOrgInteractionLimitsGetResponse200Anyof1
            ],
        )

    async def async_get_restrictions_for_org(
        self,
        org: str,
    ) -> "Response[Union[InteractionLimitResponse, OrgsOrgInteractionLimitsGetResponse200Anyof1]]":
        url = f"/orgs/{org}/interaction-limits"

        return await self._github.arequest(
            "GET",
            url,
            response_model=Union[
                InteractionLimitResponse, OrgsOrgInteractionLimitsGetResponse200Anyof1
            ],
        )

    @overload
    def set_restrictions_for_org(
        self, org: str, *, data: InteractionLimitType
    ) -> "Response[InteractionLimitResponse]":
        ...

    @overload
    def set_restrictions_for_org(
        self,
        org: str,
        *,
        data: Unset = UNSET,
        limit: Literal["existing_users", "contributors_only", "collaborators_only"],
        expiry: Union[
            Unset,
            Literal["one_day", "three_days", "one_week", "one_month", "six_months"],
        ] = UNSET,
    ) -> "Response[InteractionLimitResponse]":
        ...

    def set_restrictions_for_org(
        self, org: str, *, data: Union[Unset, InteractionLimitType] = UNSET, **kwargs
    ) -> "Response[InteractionLimitResponse]":
        url = f"/orgs/{org}/interaction-limits"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(InteractionLimit, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PUT",
            url,
            json=exclude_unset(json),
            response_model=InteractionLimitResponse,
            error_models={
                "422": ValidationError,
            },
        )

    @overload
    async def async_set_restrictions_for_org(
        self, org: str, *, data: InteractionLimitType
    ) -> "Response[InteractionLimitResponse]":
        ...

    @overload
    async def async_set_restrictions_for_org(
        self,
        org: str,
        *,
        data: Unset = UNSET,
        limit: Literal["existing_users", "contributors_only", "collaborators_only"],
        expiry: Union[
            Unset,
            Literal["one_day", "three_days", "one_week", "one_month", "six_months"],
        ] = UNSET,
    ) -> "Response[InteractionLimitResponse]":
        ...

    async def async_set_restrictions_for_org(
        self, org: str, *, data: Union[Unset, InteractionLimitType] = UNSET, **kwargs
    ) -> "Response[InteractionLimitResponse]":
        url = f"/orgs/{org}/interaction-limits"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(InteractionLimit, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PUT",
            url,
            json=exclude_unset(json),
            response_model=InteractionLimitResponse,
            error_models={
                "422": ValidationError,
            },
        )

    def remove_restrictions_for_org(
        self,
        org: str,
    ) -> "Response":
        url = f"/orgs/{org}/interaction-limits"

        return self._github.request(
            "DELETE",
            url,
        )

    async def async_remove_restrictions_for_org(
        self,
        org: str,
    ) -> "Response":
        url = f"/orgs/{org}/interaction-limits"

        return await self._github.arequest(
            "DELETE",
            url,
        )

    def get_restrictions_for_repo(
        self,
        owner: str,
        repo: str,
    ) -> "Response[Union[InteractionLimitResponse, ReposOwnerRepoInteractionLimitsGetResponse200Anyof1]]":
        url = f"/repos/{owner}/{repo}/interaction-limits"

        return self._github.request(
            "GET",
            url,
            response_model=Union[
                InteractionLimitResponse,
                ReposOwnerRepoInteractionLimitsGetResponse200Anyof1,
            ],
        )

    async def async_get_restrictions_for_repo(
        self,
        owner: str,
        repo: str,
    ) -> "Response[Union[InteractionLimitResponse, ReposOwnerRepoInteractionLimitsGetResponse200Anyof1]]":
        url = f"/repos/{owner}/{repo}/interaction-limits"

        return await self._github.arequest(
            "GET",
            url,
            response_model=Union[
                InteractionLimitResponse,
                ReposOwnerRepoInteractionLimitsGetResponse200Anyof1,
            ],
        )

    @overload
    def set_restrictions_for_repo(
        self, owner: str, repo: str, *, data: InteractionLimitType
    ) -> "Response[InteractionLimitResponse]":
        ...

    @overload
    def set_restrictions_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        data: Unset = UNSET,
        limit: Literal["existing_users", "contributors_only", "collaborators_only"],
        expiry: Union[
            Unset,
            Literal["one_day", "three_days", "one_week", "one_month", "six_months"],
        ] = UNSET,
    ) -> "Response[InteractionLimitResponse]":
        ...

    def set_restrictions_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        data: Union[Unset, InteractionLimitType] = UNSET,
        **kwargs,
    ) -> "Response[InteractionLimitResponse]":
        url = f"/repos/{owner}/{repo}/interaction-limits"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(InteractionLimit, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PUT",
            url,
            json=exclude_unset(json),
            response_model=InteractionLimitResponse,
            error_models={},
        )

    @overload
    async def async_set_restrictions_for_repo(
        self, owner: str, repo: str, *, data: InteractionLimitType
    ) -> "Response[InteractionLimitResponse]":
        ...

    @overload
    async def async_set_restrictions_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        data: Unset = UNSET,
        limit: Literal["existing_users", "contributors_only", "collaborators_only"],
        expiry: Union[
            Unset,
            Literal["one_day", "three_days", "one_week", "one_month", "six_months"],
        ] = UNSET,
    ) -> "Response[InteractionLimitResponse]":
        ...

    async def async_set_restrictions_for_repo(
        self,
        owner: str,
        repo: str,
        *,
        data: Union[Unset, InteractionLimitType] = UNSET,
        **kwargs,
    ) -> "Response[InteractionLimitResponse]":
        url = f"/repos/{owner}/{repo}/interaction-limits"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(InteractionLimit, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PUT",
            url,
            json=exclude_unset(json),
            response_model=InteractionLimitResponse,
            error_models={},
        )

    def remove_restrictions_for_repo(
        self,
        owner: str,
        repo: str,
    ) -> "Response":
        url = f"/repos/{owner}/{repo}/interaction-limits"

        return self._github.request(
            "DELETE",
            url,
            error_models={},
        )

    async def async_remove_restrictions_for_repo(
        self,
        owner: str,
        repo: str,
    ) -> "Response":
        url = f"/repos/{owner}/{repo}/interaction-limits"

        return await self._github.arequest(
            "DELETE",
            url,
            error_models={},
        )

    def get_restrictions_for_authenticated_user(
        self,
    ) -> "Response[Union[InteractionLimitResponse, UserInteractionLimitsGetResponse200Anyof1]]":
        url = "/user/interaction-limits"

        return self._github.request(
            "GET",
            url,
            response_model=Union[
                InteractionLimitResponse, UserInteractionLimitsGetResponse200Anyof1
            ],
        )

    async def async_get_restrictions_for_authenticated_user(
        self,
    ) -> "Response[Union[InteractionLimitResponse, UserInteractionLimitsGetResponse200Anyof1]]":
        url = "/user/interaction-limits"

        return await self._github.arequest(
            "GET",
            url,
            response_model=Union[
                InteractionLimitResponse, UserInteractionLimitsGetResponse200Anyof1
            ],
        )

    @overload
    def set_restrictions_for_authenticated_user(
        self, *, data: InteractionLimitType
    ) -> "Response[InteractionLimitResponse]":
        ...

    @overload
    def set_restrictions_for_authenticated_user(
        self,
        *,
        data: Unset = UNSET,
        limit: Literal["existing_users", "contributors_only", "collaborators_only"],
        expiry: Union[
            Unset,
            Literal["one_day", "three_days", "one_week", "one_month", "six_months"],
        ] = UNSET,
    ) -> "Response[InteractionLimitResponse]":
        ...

    def set_restrictions_for_authenticated_user(
        self, *, data: Union[Unset, InteractionLimitType] = UNSET, **kwargs
    ) -> "Response[InteractionLimitResponse]":
        url = "/user/interaction-limits"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(InteractionLimit, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PUT",
            url,
            json=exclude_unset(json),
            response_model=InteractionLimitResponse,
            error_models={
                "422": ValidationError,
            },
        )

    @overload
    async def async_set_restrictions_for_authenticated_user(
        self, *, data: InteractionLimitType
    ) -> "Response[InteractionLimitResponse]":
        ...

    @overload
    async def async_set_restrictions_for_authenticated_user(
        self,
        *,
        data: Unset = UNSET,
        limit: Literal["existing_users", "contributors_only", "collaborators_only"],
        expiry: Union[
            Unset,
            Literal["one_day", "three_days", "one_week", "one_month", "six_months"],
        ] = UNSET,
    ) -> "Response[InteractionLimitResponse]":
        ...

    async def async_set_restrictions_for_authenticated_user(
        self, *, data: Union[Unset, InteractionLimitType] = UNSET, **kwargs
    ) -> "Response[InteractionLimitResponse]":
        url = "/user/interaction-limits"

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(InteractionLimit, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PUT",
            url,
            json=exclude_unset(json),
            response_model=InteractionLimitResponse,
            error_models={
                "422": ValidationError,
            },
        )

    def remove_restrictions_for_authenticated_user(
        self,
    ) -> "Response":
        url = "/user/interaction-limits"

        return self._github.request(
            "DELETE",
            url,
        )

    async def async_remove_restrictions_for_authenticated_user(
        self,
    ) -> "Response":
        url = "/user/interaction-limits"

        return await self._github.arequest(
            "DELETE",
            url,
        )
