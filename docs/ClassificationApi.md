# hiarc.ClassificationApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_classification**](ClassificationApi.md#create_classification) | **POST** /classifications | Create a Classification
[**delete_classification**](ClassificationApi.md#delete_classification) | **DELETE** /classifications/{key} | Delete a Classification
[**find_classification**](ClassificationApi.md#find_classification) | **POST** /classifications/find | Find a Classification
[**get_all_classifications**](ClassificationApi.md#get_all_classifications) | **GET** /classifications | Get all Classifications
[**get_classification**](ClassificationApi.md#get_classification) | **GET** /classifications/{key} | Get a Classification&#x27;s Info
[**update_classification**](ClassificationApi.md#update_classification) | **PUT** /classifications/{key} | Update a Classification

# **create_classification**
> Classification create_classification(body, x_hiarc_user_key=x_hiarc_user_key)

Create a Classification

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
api_instance = hiarc.ClassificationApi(hiarc.ApiClient(configuration))
body = hiarc.CreateClassificationRequest() # CreateClassificationRequest | Classification information
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Create a Classification
    api_response = api_instance.create_classification(body, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationApi->create_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateClassificationRequest**](CreateClassificationRequest.md)| Classification information | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**Classification**](Classification.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_classification**
> Empty delete_classification(key, x_hiarc_user_key=x_hiarc_user_key)

Delete a Classification

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
api_instance = hiarc.ClassificationApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of Classification to delete
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Delete a Classification
    api_response = api_instance.delete_classification(key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationApi->delete_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of Classification to delete | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_classification**
> ListOfClassifications find_classification(body, x_hiarc_user_key=x_hiarc_user_key)

Find a Classification

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
api_instance = hiarc.ClassificationApi(hiarc.ApiClient(configuration))
body = hiarc.FindClassificationsRequest() # FindClassificationsRequest | Classification query
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Find a Classification
    api_response = api_instance.find_classification(body, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationApi->find_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FindClassificationsRequest**](FindClassificationsRequest.md)| Classification query | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**ListOfClassifications**](ListOfClassifications.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_classifications**
> ListOfClassifications get_all_classifications(x_hiarc_user_key=x_hiarc_user_key)

Get all Classifications

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
api_instance = hiarc.ClassificationApi(hiarc.ApiClient(configuration))
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Get all Classifications
    api_response = api_instance.get_all_classifications(x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationApi->get_all_classifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**ListOfClassifications**](ListOfClassifications.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classification**
> Classification get_classification(key, x_hiarc_user_key=x_hiarc_user_key)

Get a Classification's Info

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
api_instance = hiarc.ClassificationApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of Classification to get info
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Get a Classification's Info
    api_response = api_instance.get_classification(key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationApi->get_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of Classification to get info | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**Classification**](Classification.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_classification**
> Classification update_classification(body, key, x_hiarc_user_key=x_hiarc_user_key)

Update a Classification

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
api_instance = hiarc.ClassificationApi(hiarc.ApiClient(configuration))
body = hiarc.UpdateClassificationRequest() # UpdateClassificationRequest | Classification information
key = 'key_example' # str | Key of Classification to get info
x_hiarc_user_key = 'x_hiarc_user_key_example' # str | Optional key of user to impersonate (optional)

try:
    # Update a Classification
    api_response = api_instance.update_classification(body, key, x_hiarc_user_key=x_hiarc_user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationApi->update_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateClassificationRequest**](UpdateClassificationRequest.md)| Classification information | 
 **key** | **str**| Key of Classification to get info | 
 **x_hiarc_user_key** | **str**| Optional key of user to impersonate | [optional] 

### Return type

[**Classification**](Classification.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

