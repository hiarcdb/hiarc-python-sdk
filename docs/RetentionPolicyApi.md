# hiarc.RetentionPolicyApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_retention_policy**](RetentionPolicyApi.md#create_retention_policy) | **POST** /retentionpolicies | Create a Retention Policy
[**find_retention_policies**](RetentionPolicyApi.md#find_retention_policies) | **POST** /retentionpolicies/find | Find a Retention Policy
[**get_all_retention_policies**](RetentionPolicyApi.md#get_all_retention_policies) | **GET** /retentionpolicies | Get all Retention Policies
[**get_retention_policy**](RetentionPolicyApi.md#get_retention_policy) | **GET** /retentionpolicies/{key} | Get a Retention Policy&#x27;s Info
[**update_retention_policy**](RetentionPolicyApi.md#update_retention_policy) | **PUT** /retentionpolicies/{key} | Update a Retention Policy

# **create_retention_policy**
> RetentionPolicy create_retention_policy(body)

Create a Retention Policy

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
api_instance = hiarc.RetentionPolicyApi(hiarc.ApiClient(configuration))
body = hiarc.CreateRetentionPolicyRequest() # CreateRetentionPolicyRequest | Retention Policy information

try:
    # Create a Retention Policy
    api_response = api_instance.create_retention_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionPolicyApi->create_retention_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRetentionPolicyRequest**](CreateRetentionPolicyRequest.md)| Retention Policy information | 

### Return type

[**RetentionPolicy**](RetentionPolicy.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_retention_policies**
> ListOfRetentionPolicies find_retention_policies(body)

Find a Retention Policy

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
api_instance = hiarc.RetentionPolicyApi(hiarc.ApiClient(configuration))
body = hiarc.FindRetentionPoliciesRequest() # FindRetentionPoliciesRequest | Retention Policy query

try:
    # Find a Retention Policy
    api_response = api_instance.find_retention_policies(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionPolicyApi->find_retention_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FindRetentionPoliciesRequest**](FindRetentionPoliciesRequest.md)| Retention Policy query | 

### Return type

[**ListOfRetentionPolicies**](ListOfRetentionPolicies.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_retention_policies**
> ListOfRetentionPolicies get_all_retention_policies()

Get all Retention Policies

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
api_instance = hiarc.RetentionPolicyApi(hiarc.ApiClient(configuration))

try:
    # Get all Retention Policies
    api_response = api_instance.get_all_retention_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionPolicyApi->get_all_retention_policies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListOfRetentionPolicies**](ListOfRetentionPolicies.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_retention_policy**
> RetentionPolicy get_retention_policy(key)

Get a Retention Policy's Info

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
api_instance = hiarc.RetentionPolicyApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of Retention Policy to get info

try:
    # Get a Retention Policy's Info
    api_response = api_instance.get_retention_policy(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionPolicyApi->get_retention_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of Retention Policy to get info | 

### Return type

[**RetentionPolicy**](RetentionPolicy.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_retention_policy**
> RetentionPolicy update_retention_policy(body, key)

Update a Retention Policy

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
api_instance = hiarc.RetentionPolicyApi(hiarc.ApiClient(configuration))
body = hiarc.UpdateRetentionPolicyRequest() # UpdateRetentionPolicyRequest | RetentionPolicy information
key = 'key_example' # str | Key of Retention Policy to update

try:
    # Update a Retention Policy
    api_response = api_instance.update_retention_policy(body, key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetentionPolicyApi->update_retention_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRetentionPolicyRequest**](UpdateRetentionPolicyRequest.md)| RetentionPolicy information | 
 **key** | **str**| Key of Retention Policy to update | 

### Return type

[**RetentionPolicy**](RetentionPolicy.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

