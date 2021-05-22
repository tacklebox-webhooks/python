from .error import *
from .http_request import HttpRequest
from .http_client import HttpClient

class UserApi:
    def __init__(self, config):
        self.base_url = config['base_url']
        self.http_client = HttpClient(config['api_key'])
        self.validator = Validation()

    def create_user(self, service_id, user_data):
        if not self.validator.is_valid_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The create_user method must be invoked with a non-empty string service_id argument."
            )
    
        if not self.validator.is_valid_data(user_data):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The create_user method must be invoked with a non-empty string name argument."
            )
    
        path = f"services/{service_id}/users"
        request = HttpRequest("POST", self.base_url, path, user_data)
        return self.http_client.send(request)
  
    def delete_user(self, service_id, user_id):
        if not self.validator.is_valid_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The delete_user method must be invoked with a non-empty string service_id argument."
            )
    
        if not self.validator.is_valid_id(user_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The delete_user method must be invoked with a non-empty string user_id argument."
            )
    
        path = f"services/{service_id}/users/{user_id}"
        request = HttpRequest("DELETE", self.base_url, path)
        return self.http_client.send(request)
  
    def get_user(self, service_id, user_id):
        if not self.validator.is_valid_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The get_user method must be invoked with a non-empty string service_id argument."
            )
    
        if not self.validator.is_valid_id(user_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The get_user method must be invoked with a non-empty string user_id argument."
            )
    
        path = f"services/{service_id}/users/{user_id}"
        request = HttpRequest("GET", self.base_url, path)
        return self.http_client.send(request)
  
    def list_users(self, service_id):
        if not self.validator.is_valid_id(service_id):
            return new_error(
                ERROR_TYPES['missing_parameter'],
                "The list_users method must be invoked with a non-empty string service_id argument."
            )
    
        path = f"services/{service_id}/users"
        request = HttpRequest("GET", self.base_url, path)
        return self.http_client.send(request)
