# hiarc.FileApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_classification_to_file**](FileApi.md#add_classification_to_file) | **PUT** /files/{key}/classifications | Add a Classification to a File
[**add_group_to_file**](FileApi.md#add_group_to_file) | **PUT** /files/{key}/groups | Give a group access to a File
[**add_retention_policy_to_file**](FileApi.md#add_retention_policy_to_file) | **PUT** /files/{key}/retentionpolicies | Add a Retention Policy to a File
[**add_user_to_file**](FileApi.md#add_user_to_file) | **PUT** /files/{key}/users | Give a user access to a File
[**add_version**](FileApi.md#add_version) | **PUT** /files/{key}/versions | Add a new File Version
[**attach_to_exisiting_file**](FileApi.md#attach_to_exisiting_file) | **PUT** /files/{key}/attach | Attach to an existing File
[**copy_file**](FileApi.md#copy_file) | **PUT** /files/{key}/copy | Copy a File
[**create_direct_upload_url**](FileApi.md#create_direct_upload_url) | **POST** /files/directuploadurl | Create a direct upload url to a storage service
[**create_file**](FileApi.md#create_file) | **POST** /files | Create a File
[**delete_file**](FileApi.md#delete_file) | **DELETE** /files/{key} | Delete a File
[**download_file**](FileApi.md#download_file) | **GET** /files/{key}/download | Download a File
[**get_collections_for_file**](FileApi.md#get_collections_for_file) | **GET** /files/{key}/collections | Get a list of Collections for a File
[**get_direct_download_url**](FileApi.md#get_direct_download_url) | **GET** /files/{key}/directdownloadurl | Get a direct download URL to a File
[**get_file**](FileApi.md#get_file) | **GET** /files/{key} | Get a File&#x27;s Info
[**get_retention_policies**](FileApi.md#get_retention_policies) | **GET** /files/{key}/retentionpolicies | Get a list of Retention Policies on a File
[**get_versions**](FileApi.md#get_versions) | **GET** /files/{key}/versions | Get a list of File Versions
[**update_file**](FileApi.md#update_file) | **PUT** /files/{key} | Update a File
[**filter_allowed_files**](FileApi.md#filter_allowed_files) | **POST** /files/allowed | Filter a list of File keys that a User can access

# **add_classification_to_file**
> Empty add_classification_to_file(body, key, x_hiarc_user_key=x_hiarc_user_key)

Add a Classification to a File

### Example
```python
from __future__ import print_function
import time
import hiarc
from hiarc.rest import ApiException
from pprint import pprint

# Configure API key authorization: AdminApiKeyAuth
configuration = hiarc.Configuration()
configuration.api_key['X-Hiarc-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Hiarc-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = hiarc.FileApi(hiarc.ApiClient(configuration))
body = hiarc.AddClassificationToFileRequest() # AddClassificationToFileRequest | Classification information
key = 'key_example' # str | Key of file
x_hiarc_user_key = 'x_hiarc_user_key_example' # str |  (optional)

try:
    # Add a Classification to a File
    api_response = api_instance.add_classification_to_file(body, key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->add_classification_to_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddClassificationToFileRequest**](AddClassificationToFileRequest.md)| Classification information | 
 **key** | **str**| Key of file | 
 **x_hiarc_user_key** | **str**|  | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_group_to_file**
> Empty add_group_to_file(body, key, x_hiarc_user_key=x_hiarc_user_key)

Give a group access to a File

### Example
```python
from __future__ import print_function
import time
import hiarc
from hiarc.rest import ApiException
from pprint import pprint

# Configure API key authorization: AdminApiKeyAuth
configuration = hiarc.Configuration()
configuration.api_key['X-Hiarc-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Hiarc-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = hiarc.FileApi(hiarc.ApiClient(configuration))
body = hiarc.AddGroupToFileRequest() # AddGroupToFileRequest | Group information
key = 'key_example' # str | Key of file
x_hiarc_user_key = 'x_hiarc_user_key_example' # str |  (optional)

try:
    # Give a group access to a File
    api_response = api_instance.add_group_to_file(body, key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->add_group_to_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddGroupToFileRequest**](AddGroupToFileRequest.md)| Group information | 
 **key** | **str**| Key of file | 
 **x_hiarc_user_key** | **str**|  | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_retention_policy_to_file**
> Empty add_retention_policy_to_file(body, key, x_hiarc_user_key=x_hiarc_user_key)

Add a Retention Policy to a File

### Example
```python
from __future__ import print_function
import time
import hiarc
from hiarc.rest import ApiException
from pprint import pprint

# Configure API key authorization: AdminApiKeyAuth
configuration = hiarc.Configuration()
configuration.api_key['X-Hiarc-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Hiarc-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = hiarc.FileApi(hiarc.ApiClient(configuration))
body = hiarc.AddRetentionPolicyToFileRequest() # AddRetentionPolicyToFileRequest | Retention Policy information
key = 'key_example' # str | Key of file
x_hiarc_user_key = 'x_hiarc_user_key_example' # str |  (optional)

try:
    # Add a Retention Policy to a File
    api_response = api_instance.add_retention_policy_to_file(body, key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->add_retention_policy_to_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddRetentionPolicyToFileRequest**](AddRetentionPolicyToFileRequest.md)| Retention Policy information | 
 **key** | **str**| Key of file | 
 **x_hiarc_user_key** | **str**|  | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_to_file**
> Empty add_user_to_file(body, key, x_hiarc_user_key=x_hiarc_user_key)

Give a user access to a File

### Example
```python
from __future__ import print_function
import time
import hiarc
from hiarc.rest import ApiException
from pprint import pprint

# Configure API key authorization: AdminApiKeyAuth
configuration = hiarc.Configuration()
configuration.api_key['X-Hiarc-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Hiarc-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = hiarc.FileApi(hiarc.ApiClient(configuration))
body = hiarc.AddUserToFileRequest() # AddUserToFileRequest | User information
key = 'key_example' # str | Key of file
x_hiarc_user_key = 'x_hiarc_user_key_example' # str |  (optional)

try:
    # Give a user access to a File
    api_response = api_instance.add_user_to_file(body, key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->add_user_to_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddUserToFileRequest**](AddUserToFileRequest.md)| User information | 
 **key** | **str**| Key of file | 
 **x_hiarc_user_key** | **str**|  | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_version**
> File add_version(request, file, key, x_hiarc_user_key=x_hiarc_user_key)

Add a new File Version

### Example
```python
from __future__ import print_function
import time
import hiarc
from hiarc.rest import ApiException
from pprint import pprint

# Configure API key authorization: AdminApiKeyAuth
configuration = hiarc.Configuration()
configuration.api_key['X-Hiarc-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Hiarc-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = hiarc.FileApi(hiarc.ApiClient(configuration))
request = 'request_example' # str | 
file = 'file_example' # str | 
key = 'key_example' # str | Key of file to add a version
x_hiarc_user_key = 'x_hiarc_user_key_example' # str |  (optional)

try:
    # Add a new File Version
    api_response = api_instance.add_version(request, file, key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->add_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **str**|  | 
 **file** | **str**|  | 
 **key** | **str**| Key of file to add a version | 
 **x_hiarc_user_key** | **str**|  | [optional] 

### Return type

[**File**](File.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_to_exisiting_file**
> File attach_to_exisiting_file(body, key, x_hiarc_user_key=x_hiarc_user_key)

Attach to an existing File

### Example
```python
from __future__ import print_function
import time
import hiarc
from hiarc.rest import ApiException
from pprint import pprint

# Configure API key authorization: AdminApiKeyAuth
configuration = hiarc.Configuration()
configuration.api_key['X-Hiarc-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Hiarc-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = hiarc.FileApi(hiarc.ApiClient(configuration))
body = hiarc.AttachToExistingFileRequest() # AttachToExistingFileRequest | File information
key = 'key_example' # str | Key of file to attach to
x_hiarc_user_key = 'x_hiarc_user_key_example' # str |  (optional)

try:
    # Attach to an existing File
    api_response = api_instance.attach_to_exisiting_file(body, key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->attach_to_exisiting_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttachToExistingFileRequest**](AttachToExistingFileRequest.md)| File information | 
 **key** | **str**| Key of file to attach to | 
 **x_hiarc_user_key** | **str**|  | [optional] 

### Return type

[**File**](File.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_file**
> File copy_file(body, key, x_hiarc_user_key=x_hiarc_user_key)

Copy a File

### Example
```python
from __future__ import print_function
import time
import hiarc
from hiarc.rest import ApiException
from pprint import pprint

# Configure API key authorization: AdminApiKeyAuth
configuration = hiarc.Configuration()
configuration.api_key['X-Hiarc-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Hiarc-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = hiarc.FileApi(hiarc.ApiClient(configuration))
body = hiarc.CopyFileRequest() # CopyFileRequest | File information
key = 'key_example' # str | Key of file to attach to
x_hiarc_user_key = 'x_hiarc_user_key_example' # str |  (optional)

try:
    # Copy a File
    api_response = api_instance.copy_file(body, key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->copy_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CopyFileRequest**](CopyFileRequest.md)| File information | 
 **key** | **str**| Key of file to attach to | 
 **x_hiarc_user_key** | **str**|  | [optional] 

### Return type

[**File**](File.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_direct_upload_url**
> FileDirectUpload create_direct_upload_url(body, x_hiarc_user_key=x_hiarc_user_key, expires_in_seconds=expires_in_seconds)

Create a direct upload url to a storage service

### Example
```python
from __future__ import print_function
import time
import hiarc
from hiarc.rest import ApiException
from pprint import pprint

# Configure API key authorization: AdminApiKeyAuth
configuration = hiarc.Configuration()
configuration.api_key['X-Hiarc-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Hiarc-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = hiarc.FileApi(hiarc.ApiClient(configuration))
body = hiarc.CreateDirectUploadUrlRequest() # CreateDirectUploadUrlRequest | Storage service information
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)
expires_in_seconds = 56 # int | When access to the url should expire (optional)

try:
    # Create a direct upload url to a storage service
    api_response = api_instance.create_direct_upload_url(body, x_hiarc_user_key=x_hiarc_user_key, expires_in_seconds=expires_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->create_direct_upload_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDirectUploadUrlRequest**](CreateDirectUploadUrlRequest.md)| Storage service information | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 
 **expires_in_seconds** | **int**| When access to the url should expire | [optional] 

### Return type

[**FileDirectUpload**](FileDirectUpload.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file**
> File create_file(request, file, x_hiarc_user_key=x_hiarc_user_key)

Create a File

### Example
```python
from __future__ import print_function
import time
import hiarc
from hiarc.rest import ApiException
from pprint import pprint

# Configure API key authorization: AdminApiKeyAuth
configuration = hiarc.Configuration()
configuration.api_key['X-Hiarc-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Hiarc-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = hiarc.FileApi(hiarc.ApiClient(configuration))
request = 'request_example' # str | 
file = 'file_example' # str | 
x_hiarc_user_key = 'x_hiarc_user_key_example' # str |  (optional)

try:
    # Create a File
    api_response = api_instance.create_file(request, file, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->create_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **str**|  | 
 **file** | **str**|  | 
 **x_hiarc_user_key** | **str**|  | [optional] 

### Return type

[**File**](File.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> Empty delete_file(key, x_hiarc_user_key=x_hiarc_user_key)

Delete a File

### Example
```python
from __future__ import print_function
import time
import hiarc
from hiarc.rest import ApiException
from pprint import pprint

# Configure API key authorization: AdminApiKeyAuth
configuration = hiarc.Configuration()
configuration.api_key['X-Hiarc-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Hiarc-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = hiarc.FileApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of file to delete
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Delete a File
    api_response = api_instance.delete_file(key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of file to delete | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> str download_file(key, x_hiarc_user_key=x_hiarc_user_key)

Download a File

### Example
```python
from __future__ import print_function
import time
import hiarc
from hiarc.rest import ApiException
from pprint import pprint

# Configure API key authorization: AdminApiKeyAuth
configuration = hiarc.Configuration()
configuration.api_key['X-Hiarc-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Hiarc-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = hiarc.FileApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of file to download
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Download a File
    api_response = api_instance.download_file(key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of file to download | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

**str**

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collections_for_file**
> ListOfCollections get_collections_for_file(key, x_hiarc_user_key=x_hiarc_user_key)

Get a list of Collections for a File

### Example
```python
from __future__ import print_function
import time
import hiarc
from hiarc.rest import ApiException
from pprint import pprint

# Configure API key authorization: AdminApiKeyAuth
configuration = hiarc.Configuration()
configuration.api_key['X-Hiarc-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Hiarc-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = hiarc.FileApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of file to get all collections
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Get a list of Collections for a File
    api_response = api_instance.get_collections_for_file(key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->get_collections_for_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of file to get all collections | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**ListOfCollections**](ListOfCollections.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_direct_download_url**
> FileDirectDownload get_direct_download_url(key, x_hiarc_user_key=x_hiarc_user_key, expires_in_seconds=expires_in_seconds)

Get a direct download URL to a File

### Example
```python
from __future__ import print_function
import time
import hiarc
from hiarc.rest import ApiException
from pprint import pprint

# Configure API key authorization: AdminApiKeyAuth
configuration = hiarc.Configuration()
configuration.api_key['X-Hiarc-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Hiarc-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = hiarc.FileApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of file to get download URL
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)
expires_in_seconds = 56 # int | When access to the url should expire (optional)

try:
    # Get a direct download URL to a File
    api_response = api_instance.get_direct_download_url(key, x_hiarc_user_key=x_hiarc_user_key, expires_in_seconds=expires_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->get_direct_download_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of file to get download URL | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 
 **expires_in_seconds** | **int**| When access to the url should expire | [optional] 

### Return type

[**FileDirectDownload**](FileDirectDownload.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> File get_file(key, x_hiarc_user_key=x_hiarc_user_key)

Get a File's Info

### Example
```python
from __future__ import print_function
import time
import hiarc
from hiarc.rest import ApiException
from pprint import pprint

# Configure API key authorization: AdminApiKeyAuth
configuration = hiarc.Configuration()
configuration.api_key['X-Hiarc-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Hiarc-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = hiarc.FileApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of file to get info
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Get a File's Info
    api_response = api_instance.get_file(key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of file to get info | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**File**](File.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_retention_policies**
> ListOfRetentionPolicyApplication get_retention_policies(key, x_hiarc_user_key=x_hiarc_user_key)

Get a list of Retention Policies on a File

### Example
```python
from __future__ import print_function
import time
import hiarc
from hiarc.rest import ApiException
from pprint import pprint

# Configure API key authorization: AdminApiKeyAuth
configuration = hiarc.Configuration()
configuration.api_key['X-Hiarc-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Hiarc-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = hiarc.FileApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of file to get all retention policies
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Get a list of Retention Policies on a File
    api_response = api_instance.get_retention_policies(key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->get_retention_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of file to get all retention policies | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**ListOfRetentionPolicyApplication**](ListOfRetentionPolicyApplication.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versions**
> ListOfFileVersions get_versions(key, x_hiarc_user_key=x_hiarc_user_key)

Get a list of File Versions

### Example
```python
from __future__ import print_function
import time
import hiarc
from hiarc.rest import ApiException
from pprint import pprint

# Configure API key authorization: AdminApiKeyAuth
configuration = hiarc.Configuration()
configuration.api_key['X-Hiarc-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Hiarc-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = hiarc.FileApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of file to get all versions
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Get a list of File Versions
    api_response = api_instance.get_versions(key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->get_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of file to get all versions | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**ListOfFileVersions**](ListOfFileVersions.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file**
> File update_file(body, key)

Update a File

### Example
```python
from __future__ import print_function
import time
import hiarc
from hiarc.rest import ApiException
from pprint import pprint

# Configure API key authorization: AdminApiKeyAuth
configuration = hiarc.Configuration()
configuration.api_key['X-Hiarc-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Hiarc-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = hiarc.FileApi(hiarc.ApiClient(configuration))
body = hiarc.UpdateFileRequest() # UpdateFileRequest | File information
key = 'key_example' # str | Key of file to update

try:
    # Update a File
    api_response = api_instance.update_file(body, key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->update_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateFileRequest**](UpdateFileRequest.md)| File information | 
 **key** | **str**| Key of file to update | 

### Return type

[**File**](File.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_allowed_files**
> AllowedFiles filter_allowed_files(body, x_hiarc_user_key=x_hiarc_user_key)

Filter a list of File keys that a User can access

### Example
```python
from __future__ import print_function
import time
import hiarc
from hiarc.rest import ApiException
from pprint import pprint

# Configure API key authorization: AdminApiKeyAuth
configuration = hiarc.Configuration()
configuration.api_key['X-Hiarc-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Hiarc-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = hiarc.FileApi(hiarc.ApiClient(configuration))
body = hiarc.AllowedFilesRequest() # AllowedFilesRequest | File key list
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Filter a list of File keys that a User can access
    api_response = api_instance.filter_allowed_files(body, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->filter_allowed_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AllowedFilesRequest**](AllowedFilesRequest.md)| File key list | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**AllowedFiles**](AllowedFiles.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

