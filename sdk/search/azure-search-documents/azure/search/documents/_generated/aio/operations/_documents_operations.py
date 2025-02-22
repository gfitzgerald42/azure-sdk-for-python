# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, List, Optional, TypeVar

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._documents_operations import build_autocomplete_get_request, build_autocomplete_post_request, build_count_request, build_get_request, build_index_request, build_search_get_request, build_search_post_request, build_suggest_get_request, build_suggest_post_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class DocumentsOperations:
    """DocumentsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.search.documents.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def count(
        self,
        request_options: Optional["_models.RequestOptions"] = None,
        **kwargs: Any
    ) -> int:
        """Queries the number of documents in the index.

        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: long, or the result of cls(response)
        :rtype: long
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[int]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-04-30-Preview")  # type: str

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        request = build_count_request(
            api_version=api_version,
            x_ms_client_request_id=_x_ms_client_request_id,
            template_url=self.count.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            "indexName": self._serialize.url("self._config.index_name", self._config.index_name, 'str'),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('long', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    count.metadata = {'url': "/docs/$count"}  # type: ignore


    @distributed_trace_async
    async def search_get(
        self,
        search_text: Optional[str] = None,
        search_options: Optional["_models.SearchOptions"] = None,
        request_options: Optional["_models.RequestOptions"] = None,
        **kwargs: Any
    ) -> "_models.SearchDocumentsResult":
        """Searches for documents in the index.

        :param search_text: A full-text search query expression; Use "*" or omit this parameter to
         match all documents.
        :type search_text: str
        :param search_options: Parameter group.
        :type search_options: ~azure.search.documents.models.SearchOptions
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchDocumentsResult, or the result of cls(response)
        :rtype: ~azure.search.documents.models.SearchDocumentsResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SearchDocumentsResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-04-30-Preview")  # type: str

        _include_total_result_count = None
        _facets = None
        _filter = None
        _highlight_fields = None
        _highlight_post_tag = None
        _highlight_pre_tag = None
        _minimum_coverage = None
        _order_by = None
        _query_type = None
        _scoring_parameters = None
        _scoring_profile = None
        _semantic_configuration = None
        _search_fields = None
        _query_language = None
        _speller = None
        _answers = None
        _search_mode = None
        _scoring_statistics = None
        _session_id = None
        _select = None
        _skip = None
        _top = None
        _captions = None
        _semantic_fields = None
        _x_ms_client_request_id = None
        if search_options is not None:
            _include_total_result_count = search_options.include_total_result_count
            _facets = search_options.facets
            _filter = search_options.filter
            _highlight_fields = search_options.highlight_fields
            _highlight_post_tag = search_options.highlight_post_tag
            _highlight_pre_tag = search_options.highlight_pre_tag
            _minimum_coverage = search_options.minimum_coverage
            _order_by = search_options.order_by
            _query_type = search_options.query_type
            _scoring_parameters = search_options.scoring_parameters
            _scoring_profile = search_options.scoring_profile
            _semantic_configuration = search_options.semantic_configuration
            _search_fields = search_options.search_fields
            _query_language = search_options.query_language
            _speller = search_options.speller
            _answers = search_options.answers
            _search_mode = search_options.search_mode
            _scoring_statistics = search_options.scoring_statistics
            _session_id = search_options.session_id
            _select = search_options.select
            _skip = search_options.skip
            _top = search_options.top
            _captions = search_options.captions
            _semantic_fields = search_options.semantic_fields
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        request = build_search_get_request(
            api_version=api_version,
            search_text=search_text,
            include_total_result_count=_include_total_result_count,
            facets=_facets,
            filter=_filter,
            highlight_fields=_highlight_fields,
            highlight_post_tag=_highlight_post_tag,
            highlight_pre_tag=_highlight_pre_tag,
            minimum_coverage=_minimum_coverage,
            order_by=_order_by,
            query_type=_query_type,
            scoring_parameters=_scoring_parameters,
            scoring_profile=_scoring_profile,
            semantic_configuration=_semantic_configuration,
            search_fields=_search_fields,
            query_language=_query_language,
            speller=_speller,
            answers=_answers,
            search_mode=_search_mode,
            scoring_statistics=_scoring_statistics,
            session_id=_session_id,
            select=_select,
            skip=_skip,
            top=_top,
            captions=_captions,
            semantic_fields=_semantic_fields,
            x_ms_client_request_id=_x_ms_client_request_id,
            template_url=self.search_get.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            "indexName": self._serialize.url("self._config.index_name", self._config.index_name, 'str'),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SearchDocumentsResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    search_get.metadata = {'url': "/docs"}  # type: ignore


    @distributed_trace_async
    async def search_post(
        self,
        search_request: "_models.SearchRequest",
        request_options: Optional["_models.RequestOptions"] = None,
        **kwargs: Any
    ) -> "_models.SearchDocumentsResult":
        """Searches for documents in the index.

        :param search_request: The definition of the Search request.
        :type search_request: ~azure.search.documents.models.SearchRequest
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SearchDocumentsResult, or the result of cls(response)
        :rtype: ~azure.search.documents.models.SearchDocumentsResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SearchDocumentsResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-04-30-Preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        _json = self._serialize.body(search_request, 'SearchRequest')

        request = build_search_post_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            x_ms_client_request_id=_x_ms_client_request_id,
            template_url=self.search_post.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            "indexName": self._serialize.url("self._config.index_name", self._config.index_name, 'str'),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SearchDocumentsResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    search_post.metadata = {'url': "/docs/search.post.search"}  # type: ignore


    @distributed_trace_async
    async def get(
        self,
        key: str,
        selected_fields: Optional[List[str]] = None,
        request_options: Optional["_models.RequestOptions"] = None,
        **kwargs: Any
    ) -> Any:
        """Retrieves a document from the index.

        :param key: The key of the document to retrieve.
        :type key: str
        :param selected_fields: List of field names to retrieve for the document; Any field not
         retrieved will be missing from the returned document.
        :type selected_fields: list[str]
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: any, or the result of cls(response)
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-04-30-Preview")  # type: str

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        request = build_get_request(
            key=key,
            api_version=api_version,
            selected_fields=selected_fields,
            x_ms_client_request_id=_x_ms_client_request_id,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            "indexName": self._serialize.url("self._config.index_name", self._config.index_name, 'str'),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('object', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/docs(\'{key}\')"}  # type: ignore


    @distributed_trace_async
    async def suggest_get(
        self,
        search_text: str,
        suggester_name: str,
        suggest_options: Optional["_models.SuggestOptions"] = None,
        request_options: Optional["_models.RequestOptions"] = None,
        **kwargs: Any
    ) -> "_models.SuggestDocumentsResult":
        """Suggests documents in the index that match the given partial query text.

        :param search_text: The search text to use to suggest documents. Must be at least 1 character,
         and no more than 100 characters.
        :type search_text: str
        :param suggester_name: The name of the suggester as specified in the suggesters collection
         that's part of the index definition.
        :type suggester_name: str
        :param suggest_options: Parameter group.
        :type suggest_options: ~azure.search.documents.models.SuggestOptions
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SuggestDocumentsResult, or the result of cls(response)
        :rtype: ~azure.search.documents.models.SuggestDocumentsResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SuggestDocumentsResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-04-30-Preview")  # type: str

        _filter = None
        _use_fuzzy_matching = None
        _highlight_post_tag = None
        _highlight_pre_tag = None
        _minimum_coverage = None
        _order_by = None
        _search_fields = None
        _select = None
        _top = None
        _x_ms_client_request_id = None
        if suggest_options is not None:
            _filter = suggest_options.filter
            _use_fuzzy_matching = suggest_options.use_fuzzy_matching
            _highlight_post_tag = suggest_options.highlight_post_tag
            _highlight_pre_tag = suggest_options.highlight_pre_tag
            _minimum_coverage = suggest_options.minimum_coverage
            _order_by = suggest_options.order_by
            _search_fields = suggest_options.search_fields
            _select = suggest_options.select
            _top = suggest_options.top
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        request = build_suggest_get_request(
            api_version=api_version,
            search_text=search_text,
            suggester_name=suggester_name,
            filter=_filter,
            use_fuzzy_matching=_use_fuzzy_matching,
            highlight_post_tag=_highlight_post_tag,
            highlight_pre_tag=_highlight_pre_tag,
            minimum_coverage=_minimum_coverage,
            order_by=_order_by,
            search_fields=_search_fields,
            select=_select,
            top=_top,
            x_ms_client_request_id=_x_ms_client_request_id,
            template_url=self.suggest_get.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            "indexName": self._serialize.url("self._config.index_name", self._config.index_name, 'str'),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SuggestDocumentsResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    suggest_get.metadata = {'url': "/docs/search.suggest"}  # type: ignore


    @distributed_trace_async
    async def suggest_post(
        self,
        suggest_request: "_models.SuggestRequest",
        request_options: Optional["_models.RequestOptions"] = None,
        **kwargs: Any
    ) -> "_models.SuggestDocumentsResult":
        """Suggests documents in the index that match the given partial query text.

        :param suggest_request: The Suggest request.
        :type suggest_request: ~azure.search.documents.models.SuggestRequest
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SuggestDocumentsResult, or the result of cls(response)
        :rtype: ~azure.search.documents.models.SuggestDocumentsResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SuggestDocumentsResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-04-30-Preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        _json = self._serialize.body(suggest_request, 'SuggestRequest')

        request = build_suggest_post_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            x_ms_client_request_id=_x_ms_client_request_id,
            template_url=self.suggest_post.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            "indexName": self._serialize.url("self._config.index_name", self._config.index_name, 'str'),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('SuggestDocumentsResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    suggest_post.metadata = {'url': "/docs/search.post.suggest"}  # type: ignore


    @distributed_trace_async
    async def index(
        self,
        actions: List["_models.IndexAction"],
        request_options: Optional["_models.RequestOptions"] = None,
        **kwargs: Any
    ) -> "_models.IndexDocumentsResult":
        """Sends a batch of document write actions to the index.

        :param actions: The actions in the batch.
        :type actions: list[~azure.search.documents.models.IndexAction]
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IndexDocumentsResult, or the result of cls(response)
        :rtype: ~azure.search.documents.models.IndexDocumentsResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.IndexDocumentsResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-04-30-Preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        _batch = _models.IndexBatch(actions=actions)
        _json = self._serialize.body(_batch, 'IndexBatch')

        request = build_index_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            x_ms_client_request_id=_x_ms_client_request_id,
            template_url=self.index.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            "indexName": self._serialize.url("self._config.index_name", self._config.index_name, 'str'),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 207]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize('IndexDocumentsResult', pipeline_response)

        if response.status_code == 207:
            deserialized = self._deserialize('IndexDocumentsResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    index.metadata = {'url': "/docs/search.index"}  # type: ignore


    @distributed_trace_async
    async def autocomplete_get(
        self,
        search_text: str,
        suggester_name: str,
        request_options: Optional["_models.RequestOptions"] = None,
        autocomplete_options: Optional["_models.AutocompleteOptions"] = None,
        **kwargs: Any
    ) -> "_models.AutocompleteResult":
        """Autocompletes incomplete query terms based on input text and matching terms in the index.

        :param search_text: The incomplete term which should be auto-completed.
        :type search_text: str
        :param suggester_name: The name of the suggester as specified in the suggesters collection
         that's part of the index definition.
        :type suggester_name: str
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.models.RequestOptions
        :param autocomplete_options: Parameter group.
        :type autocomplete_options: ~azure.search.documents.models.AutocompleteOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AutocompleteResult, or the result of cls(response)
        :rtype: ~azure.search.documents.models.AutocompleteResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AutocompleteResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-04-30-Preview")  # type: str

        _x_ms_client_request_id = None
        _autocomplete_mode = None
        _filter = None
        _use_fuzzy_matching = None
        _highlight_post_tag = None
        _highlight_pre_tag = None
        _minimum_coverage = None
        _search_fields = None
        _top = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        if autocomplete_options is not None:
            _autocomplete_mode = autocomplete_options.autocomplete_mode
            _filter = autocomplete_options.filter
            _use_fuzzy_matching = autocomplete_options.use_fuzzy_matching
            _highlight_post_tag = autocomplete_options.highlight_post_tag
            _highlight_pre_tag = autocomplete_options.highlight_pre_tag
            _minimum_coverage = autocomplete_options.minimum_coverage
            _search_fields = autocomplete_options.search_fields
            _top = autocomplete_options.top

        request = build_autocomplete_get_request(
            api_version=api_version,
            search_text=search_text,
            suggester_name=suggester_name,
            x_ms_client_request_id=_x_ms_client_request_id,
            autocomplete_mode=_autocomplete_mode,
            filter=_filter,
            use_fuzzy_matching=_use_fuzzy_matching,
            highlight_post_tag=_highlight_post_tag,
            highlight_pre_tag=_highlight_pre_tag,
            minimum_coverage=_minimum_coverage,
            search_fields=_search_fields,
            top=_top,
            template_url=self.autocomplete_get.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            "indexName": self._serialize.url("self._config.index_name", self._config.index_name, 'str'),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('AutocompleteResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    autocomplete_get.metadata = {'url': "/docs/search.autocomplete"}  # type: ignore


    @distributed_trace_async
    async def autocomplete_post(
        self,
        autocomplete_request: "_models.AutocompleteRequest",
        request_options: Optional["_models.RequestOptions"] = None,
        **kwargs: Any
    ) -> "_models.AutocompleteResult":
        """Autocompletes incomplete query terms based on input text and matching terms in the index.

        :param autocomplete_request: The definition of the Autocomplete request.
        :type autocomplete_request: ~azure.search.documents.models.AutocompleteRequest
        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AutocompleteResult, or the result of cls(response)
        :rtype: ~azure.search.documents.models.AutocompleteResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AutocompleteResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-04-30-Preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id
        _json = self._serialize.body(autocomplete_request, 'AutocompleteRequest')

        request = build_autocomplete_post_request(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            x_ms_client_request_id=_x_ms_client_request_id,
            template_url=self.autocomplete_post.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            "indexName": self._serialize.url("self._config.index_name", self._config.index_name, 'str'),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('AutocompleteResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    autocomplete_post.metadata = {'url': "/docs/search.post.autocomplete"}  # type: ignore

