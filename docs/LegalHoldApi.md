# hiarc.LegalHoldApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_legal_hold**](LegalHoldApi.md#create_legal_hold) | **POST** /legalholds | Create a Legal Hold
[**get_legal_hold**](LegalHoldApi.md#get_legal_hold) | **GET** /legalholds/{key} | Get a Legal Hold&#x27;s Info

# **create_legal_hold**
> LegalHold create_legal_hold(body)

Create a Legal Hold

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
api_instance = hiarc.LegalHoldApi(hiarc.ApiClient(configuration))
body = hiarc.CreateLegalHoldRequest() # CreateLegalHoldRequest | Legal Hold information

try:
    # Create a Legal Hold
    api_response = api_instance.create_legal_hold(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegalHoldApi->create_legal_hold: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateLegalHoldRequest**](CreateLegalHoldRequest.md)| Legal Hold information | 

### Return type

[**LegalHold**](LegalHold.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_legal_hold**
> LegalHold get_legal_hold(key)

Get a Legal Hold's Info

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
api_instance = hiarc.LegalHoldApi(hiarc.ApiClient(configuration))
key = 'key_example' # str | Key of Legal Hold to get info

try:
    # Get a Legal Hold's Info
    api_response = api_instance.get_legal_hold(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegalHoldApi->get_legal_hold: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key of Legal Hold to get info | 

### Return type

[**LegalHold**](LegalHold.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

