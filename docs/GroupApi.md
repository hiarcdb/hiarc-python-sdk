# hiarc.GroupApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_to_group**](GroupApi.md#add_user_to_group) | **PUT** /groups/{key}/users/{userKey} | Add a User to a Group
[**create_group**](GroupApi.md#create_group) | **POST** /groups | Create a Group
[**delete_group**](GroupApi.md#delete_group) | **DELETE** /groups/{key} | Delete a Group
[**find_group**](GroupApi.md#find_group) | **POST** /groups/find | Find a Group
[**get_all_groups**](GroupApi.md#get_all_groups) | **GET** /groups | Get all Groups
[**get_group**](GroupApi.md#get_group) | **GET** /groups/{key} | Get a Group&#x27;s Info
[**get_groups_for_current_user**](GroupApi.md#get_groups_for_current_user) | **GET** /users/current/groups | Get the Groups for the current User
[**update_group**](GroupApi.md#update_group) | **PUT** /groups/{key} | Update a Group
[**get_groups_for_user**](GroupApi.md#get_groups_for_user) | **GET** /users/{key}/groups | Get Groups for a User

# **add_user_to_group**
> Empty add_user_to_group(key, user_key)

Add a User to a Group

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
api_instance = hiarc.GroupApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of Group
user_key = 'user_key_example' # str | Key of User to add to Group

try:
    # Add a User to a Group
    api_response = api_instance.add_user_to_group(key, user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->add_user_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of Group | 
 **user_key** | **str**| Key of User to add to Group | 

### Return type

[**Empty**](Empty.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> Group create_group(body)

Create a Group

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
api_instance = hiarc.GroupApi(hiarc.ApiClient(configuration))
body = hiarc.CreateGroupRequest() # CreateGroupRequest | Group information

try:
    # Create a Group
    api_response = api_instance.create_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateGroupRequest**](CreateGroupRequest.md)| Group information | 

### Return type

[**Group**](Group.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> Empty delete_group(key)

Delete a Group

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
api_instance = hiarc.GroupApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of Group to delete

try:
    # Delete a Group
    api_response = api_instance.delete_group(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of Group to delete | 

### Return type

[**Empty**](Empty.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_group**
> ListOfGroups find_group(body)

Find a Group

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
api_instance = hiarc.GroupApi(hiarc.ApiClient(configuration))
body = hiarc.FindGroupsRequest() # FindGroupsRequest | Group query

try:
    # Find a Group
    api_response = api_instance.find_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->find_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FindGroupsRequest**](FindGroupsRequest.md)| Group query | 

### Return type

[**ListOfGroups**](ListOfGroups.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_groups**
> ListOfGroups get_all_groups()

Get all Groups

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
api_instance = hiarc.GroupApi(hiarc.ApiClient(configuration))

try:
    # Get all Groups
    api_response = api_instance.get_all_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_all_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListOfGroups**](ListOfGroups.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> Group get_group(key)

Get a Group's Info

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
api_instance = hiarc.GroupApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of Group to get info

try:
    # Get a Group's Info
    api_response = api_instance.get_group(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of Group to get info | 

### Return type

[**Group**](Group.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_for_current_user**
> ListOfGroups get_groups_for_current_user(x_hiarc_user_key=x_hiarc_user_key)

Get the Groups for the current User

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
api_instance = hiarc.GroupApi(hiarc.ApiClient(configuration))
x_hiarc_user_key = 'x_hiarc_user_key_example' # str |  (optional)

try:
    # Get the Groups for the current User
    api_response = api_instance.get_groups_for_current_user(x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_groups_for_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_hiarc_user_key** | **str**|  | [optional] 

### Return type

[**ListOfGroups**](ListOfGroups.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth), [JWTBearerAuth](../README.md#JWTBearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> Group update_group(body, key)

Update a Group

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
api_instance = hiarc.GroupApi(hiarc.ApiClient(configuration))
body = hiarc.UpdateGroupRequest() # UpdateGroupRequest | Group information
key = 'key_example' # str | Key of Group to update

try:
    # Update a Group
    api_response = api_instance.update_group(body, key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateGroupRequest**](UpdateGroupRequest.md)| Group information | 
 **key** | **str**| Key of Group to update | 

### Return type

[**Group**](Group.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_for_user**
> ListOfGroups get_groups_for_user(key, x_hiarc_user_key=x_hiarc_user_key)

Get Groups for a User

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
api_instance = hiarc.GroupApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of user
x_hiarc_user_key = 'x_hiarc_user_key_example' # str |  (optional)

try:
    # Get Groups for a User
    api_response = api_instance.get_groups_for_user(key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_groups_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of user | 
 **x_hiarc_user_key** | **str**|  | [optional] 

### Return type

[**ListOfGroups**](ListOfGroups.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

