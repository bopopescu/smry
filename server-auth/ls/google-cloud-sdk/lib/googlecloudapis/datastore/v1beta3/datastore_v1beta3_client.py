"""Generated client library for datastore version v1beta3."""
# NOTE: This file is autogenerated and should not be edited by hand.

from googlecloudapis.apitools.base.py import base_api
from googlecloudapis.datastore.v1beta3 import datastore_v1beta3_messages as messages


class DatastoreV1beta3(base_api.BaseApiClient):
  """Generated client library for service datastore version v1beta3."""

  MESSAGES_MODULE = messages

  _PACKAGE = u'datastore'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/datastore']
  _VERSION = u'v1beta3'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = ''
  _CLIENT_CLASS_NAME = u'DatastoreV1beta3'
  _URL_VERSION = u'v1beta3'

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new datastore handle."""
    url = url or u'https://datastore.googleapis.com/'
    super(DatastoreV1beta3, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.projects_indexes = self.ProjectsIndexesService(self)
    self.projects_operations = self.ProjectsOperationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsIndexesService(base_api.BaseApiService):
    """Service class for the projects_indexes resource."""

    _NAME = u'projects_indexes'

    def __init__(self, client):
      super(DatastoreV1beta3.ProjectsIndexesService, self).__init__(client)
      self._method_configs = {
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'datastore.projects.indexes.get',
              ordered_params=[u'projectId', u'indexId'],
              path_params=[u'indexId', u'projectId'],
              query_params=[u'databaseId'],
              relative_path=u'v1beta3/projects/{projectId}/indexes/{+indexId}',
              request_field='',
              request_type_name=u'DatastoreProjectsIndexesGetRequest',
              response_type_name=u'Index',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'datastore.projects.indexes.list',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[u'databaseId', u'filter', u'pageSize', u'pageToken'],
              relative_path=u'v1beta3/projects/{projectId}/indexes',
              request_field='',
              request_type_name=u'DatastoreProjectsIndexesListRequest',
              response_type_name=u'ListIndexesResponse',
              supports_download=False,
          ),
          'Lookup': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'datastore.projects.indexes.lookup',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectId}/indexes:lookup',
              request_field=u'lookupIndexRequest',
              request_type_name=u'DatastoreProjectsIndexesLookupRequest',
              response_type_name=u'Index',
              supports_download=False,
          ),
          'Update': base_api.ApiMethodInfo(
              http_method=u'PUT',
              method_id=u'datastore.projects.indexes.update',
              ordered_params=[u'projectId', u'indexId'],
              path_params=[u'indexId', u'projectId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectId}/indexes/{+indexId}',
              request_field='<request>',
              request_type_name=u'Index',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Gets an index.

      Args:
        request: (DatastoreProjectsIndexesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Index) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists the indexes that match the specified filters.
Only lists indexes that are not in their initial state.

      Args:
        request: (DatastoreProjectsIndexesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListIndexesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Lookup(self, request, global_params=None):
      """Looks up an index by definition.

      Args:
        request: (DatastoreProjectsIndexesLookupRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Index) The response message.
      """
      config = self.GetMethodConfig('Lookup')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Update(self, request, global_params=None):
      """Updates an index's state.
The input index must specify a (project_id, index_id) tuple
or an index definition (but not both), and a new state.
This new state must be SERVING or OFF.
The state of the key index and the kind index cannot be updated.
If the index is already in the requested state, does nothing and returns
a successful but unnamed operation.  Otherwise:
Returns an unfinished operation.
- If the new state is SERVING, sets the index's state to BUILDING and the
    result operation's field metadata.common.operation_type is BUILD_INDEX.
- If the new state is OFF, sets the index's state to CLEARING and the
   result operation's field metadata.common.operation_type is CLEAR_INDEX.
Once the operation finishes,
if it is successful the index's state is the new state,
and otherwise the index's state is ERROR.
The result operation's field response is of type google.protobuf.Empty.
The result operation's field metadata is of type UpdateIndexMetadata.

      Args:
        request: (Index) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsOperationsService(base_api.BaseApiService):
    """Service class for the projects_operations resource."""

    _NAME = u'projects_operations'

    def __init__(self, client):
      super(DatastoreV1beta3.ProjectsOperationsService, self).__init__(client)
      self._method_configs = {
          'Cancel': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'datastore.projects.operations.cancel',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1beta3/{+name}:cancel',
              request_field='',
              request_type_name=u'DatastoreProjectsOperationsCancelRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'datastore.projects.operations.delete',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1beta3/{+name}',
              request_field='',
              request_type_name=u'DatastoreProjectsOperationsDeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'datastore.projects.operations.get',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1beta3/{+name}',
              request_field='',
              request_type_name=u'DatastoreProjectsOperationsGetRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'datastore.projects.operations.list',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[u'filter', u'pageSize', u'pageToken'],
              relative_path=u'v1beta3/{+name}',
              request_field='',
              request_type_name=u'DatastoreProjectsOperationsListRequest',
              response_type_name=u'ListOperationsResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      """Starts asynchronous cancellation on a long-running operation.  The server.
makes a best effort to cancel the operation, but success is not
guaranteed.  If the server doesn't support this method, it shall return
`google.rpc.Code.UNIMPLEMENTED`.  Clients may use
[Operations.GetOperation][google.longrunning.Operations.GetOperation] or
other methods to check whether the cancellation succeeded or the operation
completed despite cancellation.

      Args:
        request: (DatastoreProjectsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Deletes a long-running operation.  It indicates the client is no longer.
interested in the operation result. It does not cancel the operation. If
the server doesn't support this method, it shall return
`google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (DatastoreProjectsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Gets the latest state of a long-running operation.  Clients may use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (DatastoreProjectsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it shall return `UNIMPLEMENTED`.

NOTE: the `name` binding below allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`.

      Args:
        request: (DatastoreProjectsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(DatastoreV1beta3.ProjectsService, self).__init__(client)
      self._method_configs = {
          'AllocateIds': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'datastore.projects.allocateIds',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectId}:allocateIds',
              request_field=u'allocateIdsRequest',
              request_type_name=u'DatastoreProjectsAllocateIdsRequest',
              response_type_name=u'AllocateIdsResponse',
              supports_download=False,
          ),
          'BeginTransaction': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'datastore.projects.beginTransaction',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectId}:beginTransaction',
              request_field=u'beginTransactionRequest',
              request_type_name=u'DatastoreProjectsBeginTransactionRequest',
              response_type_name=u'BeginTransactionResponse',
              supports_download=False,
          ),
          'Commit': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'datastore.projects.commit',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectId}:commit',
              request_field=u'commitRequest',
              request_type_name=u'DatastoreProjectsCommitRequest',
              response_type_name=u'CommitResponse',
              supports_download=False,
          ),
          'Export': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'datastore.projects.export',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectId}:export',
              request_field=u'exportRequest',
              request_type_name=u'DatastoreProjectsExportRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          'Import': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'datastore.projects.import',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectId}:import',
              request_field=u'importRequest',
              request_type_name=u'DatastoreProjectsImportRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          'Lookup': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'datastore.projects.lookup',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectId}:lookup',
              request_field=u'lookupRequest',
              request_type_name=u'DatastoreProjectsLookupRequest',
              response_type_name=u'LookupResponse',
              supports_download=False,
          ),
          'Rollback': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'datastore.projects.rollback',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectId}:rollback',
              request_field=u'rollbackRequest',
              request_type_name=u'DatastoreProjectsRollbackRequest',
              response_type_name=u'RollbackResponse',
              supports_download=False,
          ),
          'RunQuery': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'datastore.projects.runQuery',
              ordered_params=[u'projectId'],
              path_params=[u'projectId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectId}:runQuery',
              request_field=u'runQueryRequest',
              request_type_name=u'DatastoreProjectsRunQueryRequest',
              response_type_name=u'RunQueryResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def AllocateIds(self, request, global_params=None):
      """Allocate IDs for the given keys (useful for referencing an entity before.
it is inserted).

      Args:
        request: (DatastoreProjectsAllocateIdsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AllocateIdsResponse) The response message.
      """
      config = self.GetMethodConfig('AllocateIds')
      return self._RunMethod(
          config, request, global_params=global_params)

    def BeginTransaction(self, request, global_params=None):
      """Begin a new transaction.

      Args:
        request: (DatastoreProjectsBeginTransactionRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BeginTransactionResponse) The response message.
      """
      config = self.GetMethodConfig('BeginTransaction')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Commit(self, request, global_params=None):
      """Commit a transaction, optionally creating, deleting or modifying some.
entities.

      Args:
        request: (DatastoreProjectsCommitRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CommitResponse) The response message.
      """
      config = self.GetMethodConfig('Commit')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Export(self, request, global_params=None):
      """Exports a copy of all or a subset of Entities from a Google Cloud Datastore.
Project to another storage system, such as Google Cloud Storage. Recent
updates to Entities may not be reflected in the export. The export occurs
in the background and its progress can be monitored and managed via the
Operation resource that is created.  The output of an export may only be
used once the associated Operation is done. If an export Operation is
cancelled before completion it may leave partial data behind in Google
Cloud Storage.

      Args:
        request: (DatastoreProjectsExportRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Export')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Import(self, request, global_params=None):
      """Imports Entities into a Google Cloud Datastore Project. Existing Entities.
with the same key are overwritten. The import occurs in the background and
its progress can be monitored and managed via the Operation resource that
is created.  If an Import Operation is cancelled, it is possible that a
subset of the data has already been imported to the Datastore.

      Args:
        request: (DatastoreProjectsImportRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Import')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Lookup(self, request, global_params=None):
      """Look up entities by key.

      Args:
        request: (DatastoreProjectsLookupRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LookupResponse) The response message.
      """
      config = self.GetMethodConfig('Lookup')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Rollback(self, request, global_params=None):
      """Roll back a transaction.

      Args:
        request: (DatastoreProjectsRollbackRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RollbackResponse) The response message.
      """
      config = self.GetMethodConfig('Rollback')
      return self._RunMethod(
          config, request, global_params=global_params)

    def RunQuery(self, request, global_params=None):
      """Query for entities.

      Args:
        request: (DatastoreProjectsRunQueryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RunQueryResponse) The response message.
      """
      config = self.GetMethodConfig('RunQuery')
      return self._RunMethod(
          config, request, global_params=global_params)