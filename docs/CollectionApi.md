# hiarc.CollectionApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_child_to_collection**](CollectionApi.md#add_child_to_collection) | **PUT** /collections/{key}/children/{childKey} | Add a child item to a Collection
[**add_file_to_collection**](CollectionApi.md#add_file_to_collection) | **PUT** /collections/{key}/files | Add a File to a Collection
[**add_group_to_collection**](CollectionApi.md#add_group_to_collection) | **PUT** /collections/{key}/groups | Add a Group to a Collection
[**add_user_to_collection**](CollectionApi.md#add_user_to_collection) | **PUT** /collections/{key}/users | Add a User to a Collection
[**create_collection**](CollectionApi.md#create_collection) | **POST** /collections | Create a Collection
[**delete_collection**](CollectionApi.md#delete_collection) | **DELETE** /collections/{key} | Delete a Collection
[**find_collection**](CollectionApi.md#find_collection) | **POST** /collections/find | Find a Collection
[**get_all_collections**](CollectionApi.md#get_all_collections) | **GET** /collections | Get all Collections
[**get_collection**](CollectionApi.md#get_collection) | **GET** /collections/{key} | Get a Collection&#x27;s Info
[**get_collection_children**](CollectionApi.md#get_collection_children) | **GET** /collections/{key}/children | Get a Collection&#x27;s child Collections
[**get_collection_files**](CollectionApi.md#get_collection_files) | **GET** /collections/{key}/files | Get a Collection&#x27;s Files
[**get_collection_items**](CollectionApi.md#get_collection_items) | **GET** /collections/{key}/items | Get a Collection&#x27;s child items, including Collections and Files
[**remove_file_from_collection**](CollectionApi.md#remove_file_from_collection) | **DELETE** /collections/{key}/files/{fileKey} | Remove a File from a Collection
[**update_collection**](CollectionApi.md#update_collection) | **PUT** /collections/{key} | Update a Collection

# **add_child_to_collection**
> Empty add_child_to_collection(key, child_key, x_hiarc_user_key=x_hiarc_user_key)

Add a child item to a Collection

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
api_instance = hiarc.CollectionApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of Collection
child_key = 'child_key_example' # str | Key of item to add as child to Collection
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Add a child item to a Collection
    api_response = api_instance.add_child_to_collection(key, child_key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->add_child_to_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of Collection | 
 **child_key** | **str**| Key of item to add as child to Collection | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_file_to_collection**
> Empty add_file_to_collection(body, key, x_hiarc_user_key=x_hiarc_user_key)

Add a File to a Collection

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
api_instance = hiarc.CollectionApi(hiarc.ApiClient(configuration))
body = hiarc.AddFileToCollectionRequest() # AddFileToCollectionRequest | Add File request
key = 'key_example' # str | Key of Collection
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Add a File to a Collection
    api_response = api_instance.add_file_to_collection(body, key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->add_file_to_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddFileToCollectionRequest**](AddFileToCollectionRequest.md)| Add File request | 
 **key** | **str**| Key of Collection | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_group_to_collection**
> Empty add_group_to_collection(body, key, x_hiarc_user_key=x_hiarc_user_key)

Add a Group to a Collection

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
api_instance = hiarc.CollectionApi(hiarc.ApiClient(configuration))
body = hiarc.AddGroupToCollectionRequest() # AddGroupToCollectionRequest | Add Group request
key = 'key_example' # str | Key of Collection
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Add a Group to a Collection
    api_response = api_instance.add_group_to_collection(body, key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->add_group_to_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddGroupToCollectionRequest**](AddGroupToCollectionRequest.md)| Add Group request | 
 **key** | **str**| Key of Collection | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_to_collection**
> Empty add_user_to_collection(body, key, x_hiarc_user_key=x_hiarc_user_key)

Add a User to a Collection

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
api_instance = hiarc.CollectionApi(hiarc.ApiClient(configuration))
body = hiarc.AddUserToCollectionRequest() # AddUserToCollectionRequest | Add User request
key = 'key_example' # str | Key of Collection
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Add a User to a Collection
    api_response = api_instance.add_user_to_collection(body, key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->add_user_to_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddUserToCollectionRequest**](AddUserToCollectionRequest.md)| Add User request | 
 **key** | **str**| Key of Collection | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_collection**
> Collection create_collection(body, x_hiarc_user_key=x_hiarc_user_key)

Create a Collection

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
api_instance = hiarc.CollectionApi(hiarc.ApiClient(configuration))
body = hiarc.CreateCollectionRequest() # CreateCollectionRequest | Collection information
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Create a Collection
    api_response = api_instance.create_collection(body, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->create_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCollectionRequest**](CreateCollectionRequest.md)| Collection information | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**Collection**](Collection.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection**
> Empty delete_collection(key, x_hiarc_user_key=x_hiarc_user_key)

Delete a Collection

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
api_instance = hiarc.CollectionApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of Collection to delete
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Delete a Collection
    api_response = api_instance.delete_collection(key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->delete_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of Collection to delete | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_collection**
> ListOfCollections find_collection(body, x_hiarc_user_key=x_hiarc_user_key)

Find a Collection

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
api_instance = hiarc.CollectionApi(hiarc.ApiClient(configuration))
body = hiarc.FindCollectionsRequest() # FindCollectionsRequest | Collection query
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Find a Collection
    api_response = api_instance.find_collection(body, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->find_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FindCollectionsRequest**](FindCollectionsRequest.md)| Collection query | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**ListOfCollections**](ListOfCollections.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_collections**
> ListOfCollections get_all_collections(x_hiarc_user_key=x_hiarc_user_key)

Get all Collections

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
api_instance = hiarc.CollectionApi(hiarc.ApiClient(configuration))
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Get all Collections
    api_response = api_instance.get_all_collections(x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->get_all_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**ListOfCollections**](ListOfCollections.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection**
> Collection get_collection(key, x_hiarc_user_key=x_hiarc_user_key)

Get a Collection's Info

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
api_instance = hiarc.CollectionApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of collection to get info
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Get a Collection's Info
    api_response = api_instance.get_collection(key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->get_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of collection to get info | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**Collection**](Collection.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_children**
> ListOfCollections get_collection_children(key, x_hiarc_user_key=x_hiarc_user_key)

Get a Collection's child Collections

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
api_instance = hiarc.CollectionApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of collection
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Get a Collection's child Collections
    api_response = api_instance.get_collection_children(key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->get_collection_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of collection | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**ListOfCollections**](ListOfCollections.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_files**
> ListOfFiles get_collection_files(key, x_hiarc_user_key=x_hiarc_user_key)

Get a Collection's Files

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
api_instance = hiarc.CollectionApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of collection
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Get a Collection's Files
    api_response = api_instance.get_collection_files(key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->get_collection_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of collection | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**ListOfFiles**](ListOfFiles.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_items**
> CollectionItems get_collection_items(key, x_hiarc_user_key=x_hiarc_user_key)

Get a Collection's child items, including Collections and Files

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
api_instance = hiarc.CollectionApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of collection
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Get a Collection's child items, including Collections and Files
    api_response = api_instance.get_collection_items(key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->get_collection_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of collection | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**CollectionItems**](CollectionItems.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_file_from_collection**
> Empty remove_file_from_collection(key, file_key, x_hiarc_user_key=x_hiarc_user_key)

Remove a File from a Collection

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
api_instance = hiarc.CollectionApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of Collection
file_key = 'file_key_example' # str | Key of File to remove from Collection
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Remove a File from a Collection
    api_response = api_instance.remove_file_from_collection(key, file_key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->remove_file_from_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of Collection | 
 **file_key** | **str**| Key of File to remove from Collection | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collection**
> Collection update_collection(body, key, x_hiarc_user_key=x_hiarc_user_key)

Update a Collection

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
api_instance = hiarc.CollectionApi(hiarc.ApiClient(configuration))
body = hiarc.UpdateCollectionRequest() # UpdateCollectionRequest | Collection information
key = 'key_example' # str | Key of collection to get info
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Update a Collection
    api_response = api_instance.update_collection(body, key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->update_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCollectionRequest**](UpdateCollectionRequest.md)| Collection information | 
 **key** | **str**| Key of collection to get info | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**Collection**](Collection.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

