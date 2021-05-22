from .error import *
from .http_request import HttpRequest
from .http_client import HttpClient

class SubscriptionApi:
    def __init__(self, config):
        self.base_url = config['base_url']
        self.http_client = HttpClient(config['api_key'])
        self.validator = Validation()

    def list_subscriptions(self, service_id, user_id):
        if not self.validator.is_valid_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The list_subscriptions method must be invoked with a non-empty string service_id argument."
            )
        
        if not self.validator.is_valid_id(user_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The list_subscriptions method must be invoked with a non-empty string user_id argument."
            )
        
        path = f"services/{service_id}/users/{user_id}/subscriptions"
        request = HttpRequest("GET", self.base_url, path)
        return self.http_client.send(request)
  
    def create_subscription(self, service_id, user_id, subscription_data):
        if not self.validator.is_valid_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The create_subscription method must be invoked with a non-empty string service_id argument."
            )
        
        if not self.validator.is_valid_id(user_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The create_subscription method must be invoked with a non-empty string user_id argument."
            )
        
        if not self.validator.is_valid_subscription_data(subscription_data):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The create_subscription method must be invoked with non-empty url and event_types arguments."
            )
        
        path = f"services/{service_id}/users/{user_id}/subscriptions"
        request = HttpRequest("POST", self.base_url, path, subscription_data)
        return self.http_client.send(request)
    
    def delete_subscription(self, service_id, user_id, subscription_id):
        if not self.validator.is_valid_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The delete_subscription method must be invoked with a non-empty string service_id argument."
            )
        
        if not self.validator.is_valid_id(user_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The delete_subscription method must be invoked with a non-empty string user_id argument."
            )
        
        if not self.validator.is_valid_id(subscription_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The delete_subscription method must be invoked with a non-empty string subscription_id argument."
            )
    
        path = f"services/{service_id}/users/{user_id}/subscriptions/{subscription_id}"
        request = HttpRequest("DELETE", self.base_url, path)
        return self.http_client.send(request)
    
    def get_subscription(self, service_id, user_id, subscription_id):
        if not self.validator.is_valid_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The get_subscription method must be invoked with a non-empty string service_id argument."
            )
        
        if not self.validator.is_valid_id(user_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The get_subscription method must be invoked with a non-empty string user_id argument."
            )
        
        if not self.validator.is_valid_id(subscription_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The get_subscription method must be invoked with a non-empty string subscription_id argument."
            )
    
        path = f"services/{service_id}/users/{user_id}/subscriptions/{subscription_id}"
        request = HttpRequest("GET", self.base_url, path)
        return self.http_client.send(request)
