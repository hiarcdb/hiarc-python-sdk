# hiarc.TokenApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_token**](TokenApi.md#create_user_token) | **POST** /tokens/user | Create a Token for a User

# **create_user_token**
> UserCredentials create_user_token(body)

Create a Token for a User

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
api_instance = hiarc.TokenApi(hiarc.ApiClient(configuration))
body = hiarc.CreateUserTokenRequest() # CreateUserTokenRequest | User information

try:
    # Create a Token for a User
    api_response = api_instance.create_user_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->create_user_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserTokenRequest**](CreateUserTokenRequest.md)| User information | 

### Return type

[**UserCredentials**](UserCredentials.md)

### Authorization

[AdminApiKeyAuth](../README.md#AdminApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

